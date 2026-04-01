"""Test model predictions to find why it always predicts 3"""
import pickle
import pandas as pd
import numpy as np

# Load model
print("Loading model...")
with open('cafe_sales_model.pkl', 'rb') as f:
    model_data = pickle.load(f)

model = model_data['model']
feature_cols = model_data['feature_cols']
label_encoders = model_data['label_encoders']

print('='*60)
print('MODEL INSPECTION')
print('='*60)
print('Model type:', type(model).__name__)
print('Feature columns:', feature_cols)
print('\nModel coefficients:')
if hasattr(model, 'coef_'):
    for feat, coef in zip(feature_cols, model.coef_):
        print(f'  {feat}: {coef:.6f}')
print('\nModel intercept:', model.intercept_ if hasattr(model, 'intercept_') else 'N/A')

# Check coefficient variance
if hasattr(model, 'coef_'):
    coef_var = np.var(model.coef_)
    coef_std = np.std(model.coef_)
    print(f'\nCoefficient variance: {coef_var:.10f}')
    print(f'Coefficient std: {coef_std:.10f}')
    if coef_std < 0.001:
        print("WARNING: Coefficients are nearly zero - model predicts constant!")

# Test predictions
print('\n' + '='*60)
print('TESTING PREDICTIONS WITH DIFFERENT INPUTS')
print('='*60)

test_cases = [
    {'Item': 'Coffee', 'Payment Method': 'Cash', 'Location': 'In-store', 
     'Month Name': 'January', 'Day of Week': 'Monday', 'Month': 1, 'Day': 15, 
     'Quarter': 1, 'Weekend': 0, 'Week': 4},
    {'Item': 'Salad', 'Payment Method': 'Credit Card', 'Location': 'Takeaway', 
     'Month Name': 'June', 'Day of Week': 'Saturday', 'Month': 6, 'Day': 20, 
     'Quarter': 2, 'Weekend': 1, 'Week': 24},
    {'Item': 'Smoothie', 'Payment Method': 'Digital Wallet', 'Location': 'In-store', 
     'Month Name': 'December', 'Day of Week': 'Friday', 'Month': 12, 'Day': 10, 
     'Quarter': 4, 'Weekend': 0, 'Week': 50},
    {'Item': 'Cookie', 'Payment Method': 'Cash', 'Location': 'Takeaway', 
     'Month Name': 'March', 'Day of Week': 'Wednesday', 'Month': 3, 'Day': 5, 
     'Quarter': 1, 'Weekend': 0, 'Week': 10},
]

predictions = []
for i, case in enumerate(test_cases, 1):
    input_data = pd.DataFrame({
        'Item_Encoded': [label_encoders['Item'].transform([case['Item']])[0]],
        'Payment Method_Encoded': [label_encoders['Payment Method'].transform([case['Payment Method']])[0]],
        'Location_Encoded': [label_encoders['Location'].transform([case['Location']])[0]],
        'Month': [case['Month']],
        'Day_of_Month': [case['Day']],
        'Month Name_Encoded': [label_encoders['Month Name'].transform([case['Month Name']])[0]],
        'Day of Week_Encoded': [label_encoders['Day of Week'].transform([case['Day of Week']])[0]],
        'Quarter': [case['Quarter']],
        'Is_Weekend': [case['Weekend']],
        'Week_of_Year': [case['Week']]
    })
    
    pred = model.predict(input_data)[0]
    predictions.append(pred)
    
    print(f'\nTest {i}: {case["Item"]}, {case["Location"]}, {case["Month Name"]}')
    print(f'  Encoded input: {input_data.values[0]}')
    print(f'  Predicted Quantity: {pred:.10f}')
    print(f'  Rounded: {int(round(pred))}')

print('\n' + '='*60)
print('PREDICTION ANALYSIS')
print('='*60)
print(f'All predictions: {[f"{p:.6f}" for p in predictions]}')
print(f'Mean prediction: {np.mean(predictions):.6f}')
print(f'Std prediction: {np.std(predictions):.6f}')
print(f'Min prediction: {np.min(predictions):.6f}')
print(f'Max prediction: {np.max(predictions):.6f}')

if np.std(predictions) < 0.01:
    print('\nCONCLUSION: Model predicts nearly constant value!')
    print('This means the model has learned to predict the mean (no meaningful patterns)')
else:
    print('\nCONCLUSION: Model shows some variance in predictions')

# Load actual data and check
print('\n' + '='*60)
print('CHECKING TRAINING DATA')
print('='*60)
df = pd.read_csv('cleaned_cafe_sales.csv')
print(f'Actual Quantity distribution:')
print(df['Quantity'].value_counts().sort_index())
print(f'\nMean Quantity: {df["Quantity"].mean():.4f}')
print(f'Std Quantity: {df["Quantity"].std():.4f}')
