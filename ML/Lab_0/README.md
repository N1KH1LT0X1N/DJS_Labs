# Cafe Sales ML Pipeline

Complete machine learning pipeline for cafe sales prediction with interactive Gradio dashboard.

## 📁 Project Structure

```
Lab_0/
├── Lab_0.ipynb                 # Complete EDA and ML notebook
├── cleaned_cafe_sales.csv      # Cleaned dataset
├── train_model.py              # Standalone training script
├── app.py                      # Gradio interactive dashboard
├── cafe_sales_model.pkl        # Saved ML model
├── model_metadata.json         # Model metadata
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Train the Model

```bash
cd Lab_0
python train_model.py
```

This will:
- Load cleaned data
- Engineer features
- Train multiple ML models
- Save the best model as `cafe_sales_model.pkl`
- Track experiments with MLflow (optional)

### 3. Launch Interactive Dashboard

```bash
python app.py
```

Then open http://localhost:7860 in your browser.

## 📊 Dashboard Features

### 🤖 ML Predictions
- Interactive form to predict transaction revenue
- Real-time predictions using trained model
- Model performance metrics

### 📈 Revenue Analytics
- Revenue by product, location, and time
- Monthly and daily trends
- Visual insights into revenue drivers

### 👥 Customer Insights
- Transaction value distribution
- Payment method preferences
- Purchase behavior patterns

### 📖 Data Story
- Complete narrative from data analysis
- Strategic recommendations
- Actionable business insights

## 🎯 Model Performance

- **Algorithm:** Linear Regression (or best performer)
- **Accuracy (R²):** ~100% (deterministic relationship)
- **MAE:** ~$0.00
- **Features:** 13 engineered features

## 💡 Key Insights

1. **Product Portfolio:** Salad drives 23% of revenue
2. **Channel Balance:** 51% in-store, 49% takeaway
3. **Temporal Patterns:** January is peak month
4. **Payment Trends:** Digital wallet adoption growing

## 🔧 Technical Details

### Features Used
- Item (encoded)
- Quantity
- Price Per Unit
- Payment Method (encoded)
- Location (encoded)
- Month
- Day of Week (encoded)
- Temporal features (day, quarter, weekend)
- Interaction features

### Model Pipeline
1. Data loading and validation
2. Feature engineering
3. Train/test split (80/20)
4. Model training and cross-validation
5. Model selection and evaluation
6. Serialization for deployment

## 📝 Usage Examples

### Making Predictions Programmatically

```python
import pickle

# Load model
with open('cafe_sales_model.pkl', 'rb') as f:
    model_package = pickle.load(f)

model = model_package['model']
feature_cols = model_package['feature_cols']

# Prepare features (simplified example)
X_new = prepare_features(...)  # Your feature engineering logic
prediction = model.predict(X_new)
print(f"Predicted revenue: ${prediction[0]:.2f}")
```

### Training with Custom Parameters

```python
from train_model import CafeSalesModelTrainer

trainer = CafeSalesModelTrainer(
    data_path='cleaned_cafe_sales.csv',
    use_mlflow=True
)

trainer.run_pipeline()
```

## 🎓 Learning Objectives Covered

✅ Data cleaning and validation
✅ Exploratory data analysis (EDA)
✅ Feature engineering
✅ Model training and evaluation
✅ Cross-validation
✅ Model serialization
✅ Interactive dashboard creation
✅ Data storytelling

## 🛠️ Troubleshooting

### Issue: MLflow not tracking
**Solution:** MLflow is optional. Set `use_mlflow=False` in trainer

### Issue: Gradio port already in use
**Solution:** Change port in `app.py`: `demo.launch(server_port=7861)`

### Issue: Model file not found
**Solution:** Run `python train_model.py` first to generate the model

## 📚 Additional Resources

- **Skills Used:** Check `.github/skills/` directory
  - `data-scientist-skill`
  - `ml-engineer-skill`
  - `mlops-engineer-skill`
  - `data-storytelling`

## 🤝 Contributing

This is a learning project. Feel free to:
- Add new features
- Improve visualizations
- Enhance the model
- Extend the dashboard

## 📄 License

Educational purposes only.

---

**Created:** 2026
**Framework:** Scikit-learn + Gradio
**Status:** Production Ready ✅
