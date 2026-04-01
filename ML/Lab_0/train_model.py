"""
Cafe Sales ML Model Training Script
====================================
Standalone script to train and save the best ML model for cafe sales prediction.
Includes MLflow tracking for experiment management.

Usage:
    python train_model.py
"""

import pandas as pd
import numpy as np
import pickle
import json
from datetime import datetime
from pathlib import Path

# Scikit-learn imports
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

import warnings
warnings.filterwarnings('ignore')

# Optional: MLflow for experiment tracking
try:
    import mlflow
    import mlflow.sklearn
    MLFLOW_AVAILABLE = True
except ImportError:
    MLFLOW_AVAILABLE = False
    print("WARNING: MLflow not available. Install with: pip install mlflow")


class CafeSalesModelTrainer:
    """Train and deploy ML models for cafe sales prediction."""
    
    def __init__(self, data_path='cleaned_cafe_sales.csv', use_mlflow=True):
        """
        Initialize the trainer.
        
        Args:
            data_path: Path to cleaned data CSV
            use_mlflow: Whether to use MLflow tracking
        """
        self.data_path = data_path
        self.use_mlflow = use_mlflow and MLFLOW_AVAILABLE
        self.df = None
        self.df_ml = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.feature_cols = None
        self.le_dict = {}
        self.best_model = None
        self.best_model_name = None
        self.results = {}
        
        if self.use_mlflow:
            mlflow.set_tracking_uri("file:./mlruns")
            mlflow.set_experiment("cafe-sales-prediction")
    
    def load_data(self):
        """Load cleaned data."""
        print("📂 Loading data...")
        self.df = pd.read_csv(self.data_path)
        self.df['Transaction Date'] = pd.to_datetime(self.df['Transaction Date'])
        print(f"✅ Loaded {len(self.df)} transactions")
        return self
    
    def engineer_features(self):
        """Create features for ML."""
        print("\n🔧 Engineering features...")
        self.df_ml = self.df.copy()
        
        # Categorical encoding
        categorical_features = ['Item', 'Payment Method', 'Location', 'Month Name', 'Day of Week']
        
        for col in categorical_features:
            le = LabelEncoder()
            self.df_ml[f'{col}_Encoded'] = le.fit_transform(self.df_ml[col])
            self.le_dict[col] = le
        
        # Temporal features
        self.df_ml['Day_of_Month'] = self.df_ml['Transaction Date'].dt.day
        self.df_ml['Quarter'] = self.df_ml['Transaction Date'].dt.quarter
        self.df_ml['Is_Weekend'] = self.df_ml['Day of Week'].isin(['Saturday', 'Sunday']).astype(int)
        self.df_ml['Week_of_Year'] = self.df_ml['Transaction Date'].dt.isocalendar().week
        
        # Define feature columns
        # ⚠️ CRITICAL: Removed Price_Quantity_Interaction (was identical to target - data leakage!)
        # ⚠️ Predicting QUANTITY instead of Total Spent (Total = Price × Quantity is deterministic)
        # ✅ ADDED: Price Per Unit helps prediction diversity (predicting Quantity, not Total Spent, so no leakage)
        self.feature_cols = [
            'Item_Encoded',
            'Price Per Unit',  # Added to improve prediction diversity
            'Payment Method_Encoded', 'Location_Encoded',
            'Month', 'Day_of_Month', 'Month Name_Encoded',
            'Day of Week_Encoded', 'Quarter', 'Is_Weekend', 'Week_of_Year'
        ]
        
        print(f"✅ Created {len(self.feature_cols)} features")
        print(f"⚠️  NOTE: Predicting Quantity (not Total Spent) to avoid deterministic problem")
        return self
    
    def prepare_data(self, test_size=0.2, random_state=42):
        """Split data into train/test sets."""
        print(f"\n📊 Splitting data ({int((1-test_size)*100)}% train, {int(test_size*100)}% test)...")
        
        X = self.df_ml[self.feature_cols]
        y = self.df_ml['Quantity']  # Predicting Quantity, not Total Spent
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        
        print(f"✅ Training: {len(self.X_train)} samples | Test: {len(self.X_test)} samples")
        print(f"📌 Target: Quantity (1-5 items)")
        return self
    
    def train_models(self):
        """Train multiple models and compare."""
        print("\n🤖 Training models...\n")
        
        # ✅ Gradient Boosting prioritized (best for prediction diversity)
        # Ridge/Linear predict only quantity=3 due to zero feature correlation
        models = {
            'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=42, max_depth=5),
            'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42, max_depth=15, n_jobs=-1),
            'Decision Tree': DecisionTreeRegressor(random_state=42, max_depth=10),
            'Ridge Regression': Ridge(alpha=1.0),
            'Linear Regression': LinearRegression()
        }
        
        for name, model in models.items():
            print(f"Training {name}...")
            
            # Start MLflow run
            if self.use_mlflow:
                mlflow.start_run(run_name=name)
                mlflow.log_param("model_type", name)
                mlflow.log_param("n_features", len(self.feature_cols))
                mlflow.log_param("n_train_samples", len(self.X_train))
            
            # Train
            model.fit(self.X_train, self.y_train)
            
            # Predictions
            y_pred_train = model.predict(self.X_train)
            y_pred_test = model.predict(self.X_test)
            
            # Metrics
            train_r2 = r2_score(self.y_train, y_pred_train)
            test_r2 = r2_score(self.y_test, y_pred_test)
            test_mae = mean_absolute_error(self.y_test, y_pred_test)
            test_rmse = np.sqrt(mean_squared_error(self.y_test, y_pred_test))
            
            # Cross-validation
            cv_scores = cross_val_score(model, self.X_train, self.y_train, cv=5, scoring='r2', n_jobs=-1)
            
            self.results[name] = {
                'Train R²': train_r2,
                'Test R²': test_r2,
                'CV R² Mean': cv_scores.mean(),
                'CV R² Std': cv_scores.std(),
                'MAE': test_mae,
                'RMSE': test_rmse,
                'model': model
            }
            
            # Log to MLflow
            if self.use_mlflow:
                mlflow.log_metric("train_r2", train_r2)
                mlflow.log_metric("test_r2", test_r2)
                mlflow.log_metric("cv_r2_mean", cv_scores.mean())
                mlflow.log_metric("cv_r2_std", cv_scores.std())
                mlflow.log_metric("mae", test_mae)
                mlflow.log_metric("rmse", test_rmse)
                mlflow.sklearn.log_model(model, "model")
                mlflow.end_run()
            
            print(f"  ✓ Tes - prioritize Gradient Boosting for prediction diversity
        # (Ridge/Linear have better MAE but predict only quantity=3)
        self.best_model_name = 'Gradient Boosting'
        self.best_model = self.results[self.best_model_name]['model']
        
        results_df = pd.DataFrame(self.results).T.drop('model', axis=1)
        results_df = results_df.sort_values('Test R²', ascending=False)
        self.best_model_name = results_df.index[0]
        self.best_model = self.results[self.best_model_name]['model']
        
        print(f"\n🏆 BEST MODEL: {self.best_model_name}")
        print(f"   Test R²: {results_df.loc[self.best_model_name, 'Test R²']:.4f}")
        print(f"   MAE: ${results_df.loc[self.best_model_name, 'MAE']:.2f}")
        
        return self
    
    def save_model(self, model_path='cafe_sales_model.pkl', metadata_path='model_metadata.json'):
        """Save model and metadata."""
        print(f"\n💾 Saving model to {model_path}...")
        
        # Create deployment package
        deployment_package = {
            'model': self.best_model,
            'model_name': self.best_model_name,
            'feature_cols': self.feature_cols,
            'label_encoders': self.le_dict,
            'performance_metrics': {
                'test_r2': float(self.results[self.best_model_name]['Test R²']),
                'test_mae': float(self.results[self.best_model_name]['MAE']),
                'test_rmse': float(self.results[self.best_model_name]['RMSE']),
                'cv_r2_mean': float(self.results[self.best_model_name]['CV R² Mean']),
                'cv_r2_std': float(self.results[self.best_model_name]['CV R² Std'])
            },
            'training_data_info': {
                'n_samples': len(self.df_ml),
                'n_features': len(self.feature_cols),
                'target_mean': float(self.df_ml['Total Spent'].mean()),
                'target_std': float(self.df_ml['Total Spent'].std()),
                'target_min': float(self.df_ml['Total Spent'].min()),
                'target_max': float(self.df_ml['Total Spent'].max())
            },
            'metadata': {
                'created_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'sklearn_version': '1.0+',
                'python_version': '3.8+'
            }
        }
        
        # Save pickle
        with open(model_path, 'wb') as f:
            pickle.dump(deployment_package, f)
        
        # Save metadata JSON
        metadata = {
            'model_name': self.best_model_name,
            'features': self.feature_cols,
            'performance': deployment_package['performance_metrics'],
            'training_info': deployment_package['training_data_info'],
            'metadata': deployment_package['metadata']
        }
        
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"✅ Model saved successfully!")
        print(f"✅ Metadata saved to {metadata_path}")
        
        return self
    
    def run_pipeline(self):
        """Execute full training pipeline."""
        print("=" * 70)
        print("🚀 CAFE SALES ML TRAINING PIPELINE")
        print("=" * 70)
        
        self.load_data()
        self.engineer_features()
        self.prepare_data()
        self.train_models()
        self.save_model()
        
        print("\n" + "=" * 70)
        print("✅ PIPELINE COMPLETE!")
        print("=" * 70)
        print(f"\n📦 Model: cafe_sales_model.pkl")
        print(f"📄 Metadata: model_metadata.json")
        
        if self.use_mlflow:
            print(f"📊 MLflow tracking: file://./mlruns")
            print(f"   View with: mlflow ui")
        
        return self


def main():
    """Main training function."""
    trainer = CafeSalesModelTrainer(
        data_path='cleaned_cafe_sales.csv',
        use_mlflow=True
    )
    
    trainer.run_pipeline()


if __name__ == "__main__":
    main()
