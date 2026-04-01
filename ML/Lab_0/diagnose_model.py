"""
Deep diagnosis: Why do all predictions round to 3?
Check if features need scaling or if there's a different issue
"""
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split

# Load data
print("Loading data...")
df = pd.read_csv('cleaned_cafe_sales.csv')

# Parse dates
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

# Create temporal features
print("\nCreating temporal features...")
df['Day_of_Month'] = df['Transaction Date'].dt.day
df['Quarter'] = df['Transaction Date'].dt.quarter
df['Is_Weekend'] = df['Day of Week'].isin(['Saturday', 'Sunday']).astype(int)
df['Week_of_Year'] = df['Transaction Date'].dt.isocalendar().week

# Recreate encoding from notebook
from sklearn.preprocessing import LabelEncoder

categorical_features = ['Item', 'Payment Method', 'Location', 'Month Name', 'Day of Week']
le_dict = {}

print("\nCreating label encoders...")
for col in categorical_features:
    le = LabelEncoder()
    df[f'{col}_Encoded'] = le.fit_transform(df[col])
    le_dict[col] = le
    print(f"  {col}: {len(le.classes_)} classes")

# Features for Quantity prediction
feature_cols = [
    'Item_Encoded', 'Payment Method_Encoded', 'Location_Encoded',
    'Month', 'Day_of_Month', 'Month Name_Encoded',
    'Day of Week_Encoded', 'Quarter', 'Is_Weekend', 'Week_of_Year'
]

X = df[feature_cols]
y = df['Quantity']

print(f"\n{'='*60}")
print("FEATURE STATISTICS")
print(f"{'='*60}")
print(X.describe())

print(f"\n{'='*60}")
print("FEATURE CORRELATION WITH TARGET (Quantity)")
print(f"{'='*60}")
for col in feature_cols:
    corr = df[col].corr(df['Quantity'])
    print(f"{col:30s}: {corr:+.6f}")

print(f"\n{'='*60}")
print("CHECKING IF FEATURES VARY ENOUGH")
print(f"{'='*60}")
for col in feature_cols:
    unique_vals = df[col].nunique()
    value_range = df[col].max() - df[col].min()
    std = df[col].std()
    print(f"{col:30s}: {unique_vals} unique, range={value_range}, std={std:.4f}")

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"\n{'='*60}")
print("TEST 1: RIDGE WITHOUT SCALING")
print(f"{'='*60}")
ridge1 = Ridge(alpha=1.0, random_state=42)
ridge1.fit(X_train, y_train)
y_pred1 = ridge1.predict(X_test)

print(f"Test R²: {r2_score(y_test, y_pred1):.4f}")
print(f"Test MAE: {mean_absolute_error(y_test, y_pred1):.4f}")
print(f"Prediction range: [{y_pred1.min():.4f}, {y_pred1.max():.4f}]")
print(f"Prediction std: {y_pred1.std():.4f}")
print(f"All predictions round to 3? {all(round(p) == 3 for p in y_pred1)}")

print(f"\n{'='*60}")
print("TEST 2: RIDGE WITH STANDARD SCALING")
print(f"{'='*60}")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

ridge2 = Ridge(alpha=1.0, random_state=42)
ridge2.fit(X_train_scaled, y_train)
y_pred2 = ridge2.predict(X_test_scaled)

print(f"Test R²: {r2_score(y_test, y_pred2):.4f}")
print(f"Test MAE: {mean_absolute_error(y_test, y_pred2):.4f}")
print(f"Prediction range: [{y_pred2.min():.4f}, {y_pred2.max():.4f}]")
print(f"Prediction std: {y_pred2.std():.4f}")
print(f"All predictions round to 3? {all(round(p) == 3 for p in y_pred2)}")

print(f"\n{'='*60}")
print("TEST 3: RIDGE WITH LOWER REGULARIZATION")
print(f"{'='*60}")
ridge3 = Ridge(alpha=0.01, random_state=42)  # Much lower alpha
ridge3.fit(X_train, y_train)
y_pred3 = ridge3.predict(X_test)

print(f"Test R²: {r2_score(y_test, y_pred3):.4f}")
print(f"Test MAE: {mean_absolute_error(y_test, y_pred3):.4f}")
print(f"Prediction range: [{y_pred3.min():.4f}, {y_pred3.max():.4f}]")
print(f"Prediction std: {y_pred3.std():.4f}")
print(f"All predictions round to 3? {all(round(p) == 3 for p in y_pred3)}")

print(f"\n{'='*60}")
print("TEST 4: CHECKING ACTUAL VARIANCE IN TARGET")
print(f"{'='*60}")
print(f"Target (Quantity) distribution:")
print(y.value_counts().sort_index())
print(f"\nMean: {y.mean():.4f}")
print(f"Std: {y.std():.4f}")
print(f"Min: {y.min()}")
print(f"Max: {y.max()}")

# Check if target is truly unpredictable
print(f"\n{'='*60}")
print("CONCLUSION")
print(f"{'='*60}")

if y_pred1.std() < 0.2:
    print("✗ PROBLEM: Predictions have very low variance")
    print("  This means features don't distinguish between different quantities")
    print("  The model has learned to predict near the mean for all inputs")
    print("\nRECOMMENDATION:")
    print("  - Try feature scaling")
    print("  - Lower regularization (alpha)")
    print("  - Use different features")
    print("  - Accept that this target may be inherently unpredictable")
