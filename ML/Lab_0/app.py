"""
Cafe Sales Analytics Dashboard - Updated for Quantity Prediction

Interactive Gradio interface for ML model predictions, EDA visualizations, 
and data storytelling using cleaned cafe sales data.

Author: ML Pipeline
Date: 2024
"""

import gradio as gr
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Set non-GUI backend BEFORE importing pyplot
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import json
import os
from datetime import datetime

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 100


class CafeSalesAnalyticsDashboard:
    def __init__(self, model_path='cafe_sales_model.pkl', data_path='cleaned_cafe_sales.csv'):
        """Initialize dashboard with model and data"""
        self.model_path = os.path.join(os.path.dirname(__file__), model_path)
        self.data_path = os.path.join(os.path.dirname(__file__), data_path)
        
        self.load_model()
        self.load_data()
        
    def load_model(self):
        """Load trained model and metadata"""
        try:
            with open(self.model_path, 'rb') as f:
                model_data = pickle.load(f)
            
            self.model = model_data['model']
            self.feature_cols = model_data['feature_cols']
            self.label_encoders = model_data['label_encoders']
            self.model_name = model_data['model_name']
            
            # Load metrics from pickle or JSON
            if 'performance_metrics' in model_data:
                self.metrics = model_data['performance_metrics']
            else:
                metadata_path = self.model_path.replace('.pkl', '_metadata.json')
                if os.path.exists(metadata_path):
                    with open(metadata_path, 'r') as f:
                        metadata = json.load(f)
                        self.metrics = metadata.get('performance', {'test_r2': 0.0, 'test_mae': 0.0})
                else:
                    self.metrics = {'test_r2': 0.0, 'test_mae': 0.0}
                
            print(f"Model loaded: {self.model_name}")
            print(f"Features: {len(self.feature_cols)}")
            print(f"Test MAE: {self.metrics['test_mae']:.2f}")
            
        except Exception as e:
            print(f"Error loading model: {e}")
            raise
    
    def load_data(self):
        """Load cleaned cafe sales data"""
        try:
            self.df = pd.read_csv(self.data_path)
            print(f"Data loaded: {len(self.df)} records")
        except Exception as e:
            print(f"Error loading data: {e}")
            raise
    
    def predict(self, item, price_per_unit, payment_method, location, month, day, month_name, day_of_week, quarter, is_weekend, week_of_year):
        """Make prediction using trained model - predicts QUANTITY"""
        try:
            # Map month name to number
            month_map = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 
                        'May': 5, 'June': 6, 'July': 7, 'August': 8,
                        'September': 9, 'October': 10, 'November': 11, 'December': 12}
            month_num = month_map.get(month, month)
            
            # Create input dataframe with exact feature names expected by model
            input_data = pd.DataFrame({
                'Item_Encoded': [self.label_encoders['Item'].transform([item])[0]],
                'Price Per Unit': [price_per_unit],
                'Payment Method_Encoded': [self.label_encoders['Payment Method'].transform([payment_method])[0]],
                'Location_Encoded': [self.label_encoders['Location'].transform([location])[0]],
                'Month': [month_num],
                'Day_of_Month': [day],
                'Month Name_Encoded': [self.label_encoders['Month Name'].transform([month_name])[0]],
                'Day of Week_Encoded': [self.label_encoders['Day of Week'].transform([day_of_week])[0]],
                'Quarter': [quarter],
                'Is_Weekend': [1 if is_weekend == 'Yes' else 0],
                'Week_of_Year': [week_of_year]
            })
            
            # Make prediction (predicts Quantity, not Total Spent)
            predicted_quantity = self.model.predict(input_data)[0]
            
            # Round to nearest integer
            predicted_quantity_rounded = int(round(predicted_quantity))
            
            # Create result message
            result = f"""
### 📦 Predicted Quantity: {predicted_quantity_rounded} items

**Input Summary:**
- **Item:** {item}
- **Price Per Unit:** ${price_per_unit:.2f}
- **Payment Method:** {payment_method}
- **Location:** {location}
- **Month:** {month_name}
- **Day:** {day}
- **Day of Week:** {day_of_week}
- **Quarter:** Q{quarter}
- **Weekend:** {is_weekend}

**Model Information:**
- Model: {self.model_name}
- Test R² Score: {self.metrics['test_r2']:.4f}
- Mean Absolute Error: {self.metrics['test_mae']:.2f} items

**Note:** The model predicts customer purchase quantity (1-5 items) based on contextual features including price. 
Price can influence quantity - more expensive items may result in lower quantities purchased.
"""
            return result
            
        except Exception as e:
            return f"Error: {str(e)}\n\nPlease check your inputs and try again."
    
    def generate_revenue_analysis(self):
        """Generate revenue analysis visualizations."""
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        # 1. Revenue by Item
        item_revenue = self.df.groupby('Item')['Total Spent'].sum().sort_values(ascending=False)
        axes[0, 0].barh(range(len(item_revenue)), item_revenue.values, color='steelblue')
        axes[0, 0].set_yticks(range(len(item_revenue)))
        axes[0, 0].set_yticklabels(item_revenue.index)
        axes[0, 0].set_xlabel('Total Revenue ($)')
        axes[0, 0].set_title('Revenue by Item', fontweight='bold')
        axes[0, 0].invert_yaxis()
        
        # 2. Revenue by Location (Pie Chart)
        location_revenue = self.df.groupby('Location')['Total Spent'].sum()
        axes[0, 1].pie(location_revenue.values, labels=location_revenue.index, autopct='%1.1f%%',
                       colors=['#ff9999', '#66b3ff'], startangle=90)
        axes[0, 1].set_title('Revenue Distribution by Location', fontweight='bold')
        
        # 3. Monthly Revenue Trend
        self.df['Month_Num'] = pd.to_datetime(self.df['Month Name'], format='%B').dt.month
        monthly = self.df.groupby('Month_Num')['Total Spent'].sum()
        axes[1, 0].plot(monthly.index, monthly.values, marker='o', linewidth=2, 
                       markersize=8, color='green')
        axes[1, 0].set_xlabel('Month')
        axes[1, 0].set_ylabel('Revenue ($)')
        axes[1, 0].set_title('Monthly Revenue Trend', fontweight='bold')
        axes[1, 0].grid(alpha=0.3)
        
        # 4. Day of Week Revenue
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        dow_revenue = self.df.groupby('Day of Week')['Total Spent'].sum().reindex(day_order)
        axes[1, 1].bar(range(len(dow_revenue)), dow_revenue.values, color='purple', alpha=0.7)
        axes[1, 1].set_xticks(range(len(dow_revenue)))
        axes[1, 1].set_xticklabels([d[:3] for d in dow_revenue.index], rotation=0)
        axes[1, 1].set_ylabel('Revenue ($)')
        axes[1, 1].set_title('Revenue by Day of Week', fontweight='bold')
        
        plt.tight_layout()
        return fig
    
    def generate_customer_insights(self):
        """Generate customer behavior analysis."""
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        # 1. Quantity Distribution
        quantity_dist = self.df['Quantity'].value_counts().sort_index()
        axes[0, 0].bar(quantity_dist.index, quantity_dist.values, color='coral', alpha=0.7, edgecolor='black')
        axes[0, 0].set_xlabel('Quantity (items)')
        axes[0, 0].set_ylabel('Frequency')
        axes[0, 0].set_title('Purchase Quantity Distribution', fontweight='bold')
        axes[0, 0].grid(axis='y', alpha=0.3)
        
        # 2. Payment Method Preferences
        payment_counts = self.df['Payment Method'].value_counts()
        axes[0, 1].pie(payment_counts.values, labels=payment_counts.index, autopct='%1.1f%%',
                      colors=['#ff9999', '#66b3ff', '#99ff99'], startangle=90)
        axes[0, 1].set_title('Payment Method Distribution', fontweight='bold')
        
        # 3. Average Transaction Value by Item
        avg_by_item = self.df.groupby('Item')['Total Spent'].mean().sort_values()
        axes[1, 0].barh(range(len(avg_by_item)), avg_by_item.values, color='teal')
        axes[1, 0].set_yticks(range(len(avg_by_item)))
        axes[1, 0].set_yticklabels(avg_by_item.index)
        axes[1, 0].set_xlabel('Average Transaction ($)')
        axes[1, 0].set_title('Average Spend per Item', fontweight='bold')
        
        # 4. Transaction Volume by Hour (if available, else by location)
        if 'Hour' in self.df.columns:
            hourly = self.df.groupby('Hour').size()
            axes[1, 1].plot(hourly.index, hourly.values, marker='o', linewidth=2, color='orange')
            axes[1, 1].set_xlabel('Hour of Day')
            axes[1, 1].set_ylabel('Transaction Count')
            axes[1, 1].set_title('Transaction Volume by Hour', fontweight='bold')
        else:
            location_counts = self.df['Location'].value_counts()
            axes[1, 1].bar(location_counts.index, location_counts.values, color=['skyblue', 'lightcoral'])
            axes[1, 1].set_ylabel('Transaction Count')
            axes[1, 1].set_title('Transaction Volume by Location', fontweight='bold')
        
        plt.tight_layout()
        return fig
    
    def generate_data_story(self):
        """Generate narrative insights from data"""
        # Calculate key metrics
        total_revenue = self.df['Total Spent'].sum()
        avg_transaction = self.df['Total Spent'].mean()
        total_transactions = len(self.df)
        
        top_item = self.df.groupby('Item')['Total Spent'].sum().idxmax()
        top_item_revenue = self.df.groupby('Item')['Total Spent'].sum().max()
        
        peak_month = self.df.groupby('Month Name')['Total Spent'].sum().idxmax()
        
        preferred_payment = self.df['Payment Method'].value_counts().idxmax()
        
        story = f"""
# 📊 Cafe Sales Data Story

## Executive Summary
This analysis covers **{total_transactions:,} transactions** from our cafe, generating a total revenue of **${total_revenue:,.2f}**.

## Key Findings

### 💰 Revenue Insights
- **Total Revenue:** ${total_revenue:,.2f}
- **Average Transaction Value:** ${avg_transaction:.2f}
- **Top-Selling Item:** {top_item} (${top_item_revenue:,.2f} in revenue)
- **Peak Sales Month:** {peak_month}

### 🛍️ Customer Behavior
- **Preferred Payment Method:** {preferred_payment} ({self.df['Payment Method'].value_counts()[preferred_payment]} transactions)
- **Average Quantity:** {self.df['Quantity'].mean():.2f} items per transaction
- **Most Common Quantity:** {self.df['Quantity'].mode()[0]} items

### 📍 Location Analysis
- **In-Store vs Takeaway:** 
  - In-store: {len(self.df[self.df['Location']=='In-store'])} transactions (${self.df[self.df['Location']=='In-store']['Total Spent'].sum():,.2f})
  - Takeaway: {len(self.df[self.df['Location']=='Takeaway'])} transactions (${self.df[self.df['Location']=='Takeaway']['Total Spent'].sum():,.2f})

### 🤖 ML Model Performance
- **Target:** Predicting customer purchase quantity (1-5 items)
- **Best Model:** {self.model_name}
- **Test R² Score:** {self.metrics['test_r2']:.4f}
- **Mean Absolute Error:** {self.metrics['test_mae']:.2f} items

**Important Note:** The negative R² and relatively high MAE indicate that customer purchase quantity is difficult to predict from contextual features alone (item type, location, payment method, temporal features). This reflects the inherent randomness in human purchasing decisions.

## Recommendations

1. **Inventory Management:** Focus on {top_item} - highest revenue generator
2. **Peak Periods:** Prepare for increased demand during {peak_month}
3. **Payment Systems:** Ensure {preferred_payment} infrastructure is optimized
4. **Marketing:** Target customers with promotions based on purchase quantity patterns

---
*Analysis generated from cleaned cafe sales dataset ({total_transactions:,} transactions)*
"""
        return story
    
    def create_interface(self):
        """Create Gradio interface with multiple tabs"""
        
        with gr.Blocks(title="Cafe Sales Analytics Dashboard", theme=gr.themes.Soft()) as interface:
            gr.Markdown("# ☕ Cafe Sales Analytics Dashboard")
            gr.Markdown("Interactive ML predictions and business intelligence insights")
            
            with gr.Tabs():
                # Tab 1: ML Predictions
                with gr.Tab("🤖 ML Predictions"):
                    gr.Markdown("""
                    ## Quantity Prediction Model
                    
                    This model predicts **customer purchase quantity** (number of items) based on transaction context.
                    
                    **Features Used:**
                    - Item type
                    - Payment method
                    - Location (In-store/Takeaway)
                    - Temporal features (month, day, quarter, weekend, etc.)
                    
                    **Model Performance:**
                    - Test R²: ~-0.01 (negative indicates prediction is challenging)
                    - MAE: ~1.17 items
                    
                    **Why is prediction difficult?** Customer purchase quantity has inherent randomness - 
                    people's decisions about how many items to buy are influenced by many factors not 
                    captured in our features (mood, hunger level, budget, etc.).
                    """)
                    
                    with gr.Row():
                        with gr.Column():
                            item = gr.Dropdown(
                                choices=sorted(self.df['Item'].unique().tolist()),
                                label="Item",
                                value=self.df['Item'].iloc[0]
                            )
                            price = gr.Slider(1.0, 10.0, value=5.0, step=0.5, label="Price Per Unit ($)")
                            payment = gr.Dropdown(
                                choices=sorted(self.df['Payment Method'].unique().tolist()),
                                label="Payment Method",
                                value=self.df['Payment Method'].iloc[0]
                            )
                            location = gr.Dropdown(
                                choices=sorted(self.df['Location'].unique().tolist()),
                                label="Location",
                                value=self.df['Location'].iloc[0]
                            )
                            month_name = gr.Dropdown(
                                choices=['January', 'February', 'March', 'April', 'May', 'June',
                                        'July', 'August', 'September', 'October', 'November', 'December'],
                                label="Month",
                                value="January"
                            )
                            day = gr.Slider(1, 31, value=15, step=1, label="Day of Month")
                            
                        with gr.Column():
                            day_of_week = gr.Dropdown(
                                choices=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                                        'Friday', 'Saturday', 'Sunday'],
                                label="Day of Week",
                                value="Monday"
                            )
                            quarter = gr.Slider(1, 4, value=1, step=1, label="Quarter")
                            is_weekend = gr.Radio(["Yes", "No"], label="Is Weekend?", value="No")
                            week_of_year = gr.Slider(1, 52, value=1, step=1, label="Week of Year")
                            
                            predict_btn = gr.Button("🎯 Predict Quantity", variant="primary")
                    
                    prediction_output = gr.Markdown(label="Prediction Result")
                    
                    predict_btn.click(
                        fn=self.predict,
                        inputs=[item, price, payment, location, month_name, day, month_name, 
                               day_of_week, quarter, is_weekend, week_of_year],
                        outputs=prediction_output
                    )
                
                # Tab 2: Revenue Analytics
                with gr.Tab("💰 Revenue Analytics"):
                    gr.Markdown("## Revenue Analysis Dashboard")
                    gr.Markdown("Comprehensive revenue breakdown by item, location, time, and day of week.")
                    
                    revenue_plot = gr.Plot(label="Revenue Analysis")
                    revenue_btn = gr.Button("📊 Generate Revenue Analysis")
                    
                    revenue_btn.click(
                        fn=self.generate_revenue_analysis,
                        outputs=revenue_plot
                    )
                
                # Tab 3: Customer Insights
                with gr.Tab("👥 Customer Insights"):
                    gr.Markdown("## Customer Behavior Analysis")
                    gr.Markdown("Understand customer preferences, purchase patterns, and payment methods.")
                    
                    customer_plot = gr.Plot(label="Customer Analysis")
                    customer_btn = gr.Button("🔍 Generate Customer Insights")
                    
                    customer_btn.click(
                        fn=self.generate_customer_insights,
                        outputs=customer_plot
                    )
                
                # Tab 4: Data Story
                with gr.Tab("📖 Data Story"):
                    gr.Markdown("## Narrative Insights")
                    
                    story_output = gr.Markdown()
                    story_btn = gr.Button("📝 Generate Story")
                    
                    story_btn.click(
                        fn=self.generate_data_story,
                        outputs=story_output
                    )
                
                # Tab 5: About
                with gr.Tab("ℹ️ About"):
                    gr.Markdown(f"""
                    ## About This Dashboard
                    
                    **Dataset:** Cleaned Cafe Sales Data
                    - Records: {len(self.df):,} transactions
                    - Features: {len(self.df.columns)} columns
                    - Date Range: {self.df['Month Name'].iloc[0]} - {self.df['Month Name'].iloc[-1]}
                    
                    **ML Model:**
                    - Algorithm: {self.model_name}
                    - Target Variable: Quantity (1-5 items)
                    - Features: {len(self.feature_cols)} contextual attributes
                    - Test R²: {self.metrics['test_r2']:.4f}
                    - MAE: {self.metrics['test_mae']:.2f} items
                    
                    **Important Note on Model Performance:**
                    This model demonstrates a realistic ML scenario where the target variable 
                    (purchase quantity) is inherently difficult to predict from available features. 
                    The negative R² indicates that predictions are slightly worse than simply 
                    using the mean quantity. This is valid and educational - not all problems 
                    are easily solvable with ML, especially when human behavior involves randomness.
                    
                    **Data Leakage Prevention:**
                    Initial model versions achieved perfect accuracy (MAE=0) due to data leakage - 
                    the target variable (Total Spent) was perfectly calculable from features 
                    (Quantity × Price). The current model predicts Quantity from contextual 
                    features only, avoiding this deterministic relationship.
                    
                    **Technologies:**
                    - Python 3.13
                    - scikit-learn (ML models)
                    - Gradio (Dashboard)
                    - Pandas, NumPy (Data processing)
                    - Matplotlib, Seaborn (Visualizations)
                    
                    **Author:** ML Pipeline
                    **Date:** {datetime.now().strftime('%Y-%m-%d')}
                    """)
        
        return interface


def main():
    """Main function to launch dashboard"""
    print("Initializing Cafe Sales Analytics Dashboard...")
    
    dashboard = CafeSalesAnalyticsDashboard()
    interface = dashboard.create_interface()
    
    print("\n" + "="*70)
    print("Dashboard ready! Launching...")
    print("="*70 + "\n")
    
    interface.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False,
        inbrowser=True
    )


if __name__ == "__main__":
    main()
