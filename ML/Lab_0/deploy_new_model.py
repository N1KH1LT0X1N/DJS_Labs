"""Test and deploy new Gradient Boosting model"""
import pickle
import pandas as pd
import shutil

# Load new model
print("Testing new model...")
with open('cafe_sales_model_v2.pkl', 'rb') as f:
    model_data = pickle.load(f)

model = model_data['model']
le = model_data['label_encoders']
print('New model:', type(model).__name__)
print('Features:', model_data['feature_cols'])
print('Performance:')
print(f"  Test R²: {model_data['performance_metrics']['test_r2']:.4f}")
print(f"  Test MAE: {model_data['performance_metrics']['test_mae']:.4f}")

# Test with diverse inputs
test_cases = [
    {'Item': 'Coffee', 'Price': 3.5, 'Payment Method': 'Cash', 'Location': 'In-store'},
    {'Item': 'Salad', 'Price': 7.5, 'Payment Method': 'Credit Card', 'Location': 'Takeaway'},
    {'Item': 'Smoothie', 'Price': 5.0, 'Payment Method': 'Digital Wallet', 'Location': 'In-store'},
    {'Item': 'Cookie', 'Price': 2.0, 'Payment Method': 'Cash', 'Location': 'Takeaway'},
    {'Item': 'Sandwich', 'Price': 6.0, 'Payment Method': 'Digital Wallet', 'Location': 'In-store'},
]

print('\n' + '='*60)
print('TESTING PREDICTIONS WITH NEW MODEL')
print('='*60)

for case in test_cases:
    input_df = pd.DataFrame({
        'Item_Encoded': [le['Item'].transform([case['Item']])[0]],
        'Price Per Unit': [case['Price']],
        'Payment Method_Encoded': [le['Payment Method'].transform([case['Payment Method']])[0]],
        'Location_Encoded': [le['Location'].transform([case['Location']])[0]],
        'Month': [6],
        'Day_of_Month': [15],
        'Month Name_Encoded': [le['Month Name'].transform(['June'])[0]],
        'Day of Week_Encoded': [le['Day of Week'].transform(['Monday'])[0]],
        'Quarter': [2],
        'Is_Weekend': [0],
        'Week_of_Year': [24]
    })
    
    pred = model.predict(input_df)[0]
    item_name = case['Item']
    price = case['Price']
    rounded = int(round(pred))
    print(f'{item_name:10s} (${price:.2f}): {pred:.2f} -> {rounded} items')

# Replace old model
print('\n' + '='*60)
print('DEPLOYING NEW MODEL')
print('='*60)
shutil.copy('cafe_sales_model.pkl', 'cafe_sales_model_old.pkl')
print('✓ Backed up old model to cafe_sales_model_old.pkl')

shutil.copy('cafe_sales_model_v2.pkl', 'cafe_sales_model.pkl')
print('✓ Replaced cafe_sales_model.pkl with new Gradient Boosting model')

# Also update metadata
import json
metadata = {
    'model_name': 'Gradient Boosting',
    'features': model_data['feature_cols'],
    'performance': model_data['performance_metrics'],
    'date_trained': '2026-01-28',
    'notes': 'Gradient Boosting model predicts all 5 quantity values (1-5). Includes Price Per Unit as feature.'
}

with open('model_metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2)
print('✓ Updated model_metadata.json')

print('\n✅ NEW MODEL DEPLOYED SUCCESSFULLY')
print(f'   Model: {type(model).__name__}')
print(f'   Predicts: All 5 quantity values (1-5)')
print(f'   MAE: {model_data["performance_metrics"]["test_mae"]:.2f} items')
