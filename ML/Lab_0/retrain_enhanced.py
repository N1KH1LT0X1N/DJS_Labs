"""
Retrain model with Price Per Unit included as a feature
This doesn't leak info - we're predicting Quantity, and price might influence how many items customers buy
"""
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split, cross_val_score

# Load and prepare data
print("="*70)
print("RETRAINING MODEL WITH BETTER FEATURES")
print("="*70)

df = pd.read_csv('cleaned_cafe_sales.csv')
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

# Temporal features
df['Day_of_Month'] = df['Transaction Date'].dt.day
df['Quarter'] = df['Transaction Date'].dt.quarter
df['Is_Weekend'] = df['Day of Week'].isin(['Saturday', 'Sunday']).astype(int)
df['Week_of_Year'] = df['Transaction Date'].dt.isocalendar().week

# Label encoding
categorical_features = ['Item', 'Payment Method', 'Location', 'Month Name', 'Day of Week']
le_dict = {}

for col in categorical_features:
    le = LabelEncoder()
    df[f'{col}_Encoded'] = le.fit_transform(df[col])
    le_dict[col] = le

# ENHANCED FEATURES - include Price Per Unit
# Rationale: Price might predict quantity (expensive items = buy fewer?)
feature_cols = [
    'Item_Encoded', 
    'Price Per Unit',  # NEW: Price might predict quantity
    'Payment Method_Encoded', 
    'Location_Encoded',
    'Month', 'Day_of_Month', 'Month Name_Encoded',
    'Day of Week_Encoded', 'Quarter', 'Is_Weekend', 'Week_of_Year'
]

target_col = 'Quantity'

print(f"\nFeatures ({len(feature_cols)}):")
for f in feature_cols:
    corr = df[f].corr(df[target_col])
    print(f"  {f:30s}: corr={corr:+.4f}")

# Prepare data
X = df[feature_cols]
y = df[target_col]

# Check correlation
print(f"\n{'='*70}")
print("CORRELATION WITH TARGET")
print(f"{'='*70}")
print(f"Price Per Unit correlation with Quantity: {df['Price Per Unit'].corr(df['Quantity']):.4f}")

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"\nTraining: {len(X_train)} | Test: {len(X_test)}")

# Train multiple models
models = {
    'Ridge (alpha=0.1)': Ridge(alpha=0.1, random_state=42),
    'Ridge (alpha=1.0)': Ridge(alpha=1.0, random_state=42),
    'Random Forest': RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42),
    'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, max_depth=5, random_state=42)
}

results = {}
print(f"\n{'='*70}")
print("TRAINING MODELS")
print(f"{'='*70}\n")

for name, model in models.items():
    model.fit(X_train, y_train)
    
    y_pred_test = model.predict(X_test)
    y_pred_train = model.predict(X_train)
    
    test_r2 = r2_score(y_test, y_pred_test)
    test_mae = mean_absolute_error(y_test, y_pred_test)
    test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
    
    # Check prediction variance
    pred_std = y_pred_test.std()
    pred_min = y_pred_test.min()
    pred_max = y_pred_test.max()
    
    # Count how many unique rounded predictions
    rounded_preds = np.round(y_pred_test).astype(int)
    unique_preds = len(np.unique(rounded_preds))
    pred_dist = pd.Series(rounded_preds).value_counts().sort_index()
    
    results[name] = {
        'model': model,
        'test_r2': test_r2,
        'test_mae': test_mae,
        'test_rmse': test_rmse,
        'pred_std': pred_std,
        'pred_range': (pred_min, pred_max),
        'unique_rounded': unique_preds,
        'pred_distribution': pred_dist
    }
    
    print(f"{name}")
    print(f"  Test R²: {test_r2:.4f}")
    print(f"  Test MAE: {test_mae:.4f}")
    print(f"  Prediction range: [{pred_min:.2f}, {pred_max:.2f}]")
    print(f"  Prediction std: {pred_std:.4f}")
    print(f"  Unique rounded predictions: {unique_preds} (target has 5)")
    print(f"  Prediction distribution:\n{pred_dist}")
    print()

# Select best model based on unique predictions (want variety)
best_name = max(results.keys(), key=lambda k: results[k]['unique_rounded'])
best_model = results[best_name]['model']

print(f"{'='*70}")
print(f"BEST MODEL: {best_name}")
print(f"{'='*70}")
print(f"Test R²: {results[best_name]['test_r2']:.4f}")
print(f"Test MAE: {results[best_name]['test_mae']:.4f}")
print(f"Unique predictions: {results[best_name]['unique_rounded']}/5")

# Save if predictions are better
if results[best_name]['unique_rounded'] > 1:
    print(f"\n✓ Model makes {results[best_name]['unique_rounded']} different predictions")
    print("  Saving new model...")
    
    # Package model
    model_package = {
        'model': best_model,
        'feature_cols': feature_cols,
        'label_encoders': le_dict,
        'model_name': best_name,
        'performance_metrics': {
            'test_r2': results[best_name]['test_r2'],
            'test_mae': results[best_name]['test_mae'],
            'test_rmse': results[best_name]['test_rmse']
        }
    }
    
    with open('cafe_sales_model_v2.pkl', 'wb') as f:
        pickle.dump(model_package, f)
    
    print("  ✓ Saved to cafe_sales_model_v2.pkl")
    
else:
    print(f"\n✗ Model still only predicts {results[best_name]['unique_rounded']} unique value(s)")
    print("  NOT saving - predictions still too narrow")

print(f"\n{'='*70}")
print("CONCLUSION")
print(f"{'='*70}")
if results[best_name]['unique_rounded'] == 1:
    print("❌ Adding Price Per Unit didn't help")
    print("   Quantity is genuinely unpredictable from available features")
    print("   This is a limitation of the dataset, not the model")
elif results[best_name]['unique_rounded'] < 5:
    print("⚠️  Predictions improved but still limited")
    print(f"   Only predicts {results[best_name]['unique_rounded']} out of 5 possible quantities")
else:
    print("✅ Model now predicts all 5 quantity values!")
    print("   This is a significant improvement")
