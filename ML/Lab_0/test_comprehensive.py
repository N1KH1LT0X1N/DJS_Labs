"""Test model with MORE diverse inputs including extreme cases"""
import pickle
import pandas as pd
import numpy as np

# Load model
with open('cafe_sales_model.pkl', 'rb') as f:
    model_data = pickle.load(f)

model = model_data['model']
le = model_data['label_encoders']
features = model_data['feature_cols']

print('='*70)
print('COMPREHENSIVE MODEL TESTING')
print('='*70)
print(f'Model: {type(model).__name__}')
print(f'Features: {features}')

# Generate many diverse test cases
np.random.seed(42)
# Use only items that exist in training data
items = list(le['Item'].classes_)
payments = list(le['Payment Method'].classes_)
locations = list(le['Location'].classes_)
months = list(range(1, 13))
days = [1, 15, 28]

print(f'Available items: {items}')
print(f'Available payments: {payments}')
print(f'Available locations: {locations}')

predictions = []
test_inputs = []

print('\nGenerating 50 test cases...\n')

for i in range(50):
    item = np.random.choice(items)
    payment = np.random.choice(payments)
    location = np.random.choice(locations)
    month = np.random.choice(months)
    day = np.random.choice(days)
    
    # Vary price significantly
    price = np.random.uniform(1.5, 9.0)
    
    # Get month name
    month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    month_name = month_names[month-1]
    
    # Get day of week
    day_of_week = np.random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                                    'Friday', 'Saturday', 'Sunday'])
    
    input_df = pd.DataFrame({
        'Item_Encoded': [le['Item'].transform([item])[0]],
        'Price Per Unit': [price],
        'Payment Method_Encoded': [le['Payment Method'].transform([payment])[0]],
        'Location_Encoded': [le['Location'].transform([location])[0]],
        'Month': [month],
        'Day_of_Month': [day],
        'Month Name_Encoded': [le['Month Name'].transform([month_name])[0]],
        'Day of Week_Encoded': [le['Day of Week'].transform([day_of_week])[0]],
        'Quarter': [(month-1)//3 + 1],
        'Is_Weekend': [1 if day_of_week in ['Saturday', 'Sunday'] else 0],
        'Week_of_Year': [month * 4]
    })
    
    pred = model.predict(input_df)[0]
    rounded = int(round(pred))
    
    predictions.append(pred)
    test_inputs.append((item, price, rounded))
    
    if i < 10:  # Print first 10
        print(f'{i+1:2d}. {item:10s} ${price:5.2f} -> {pred:.3f} = {rounded} items')

print('\n' + '='*70)
print('PREDICTION ANALYSIS')
print('='*70)

predictions = np.array(predictions)
rounded_preds = np.round(predictions).astype(int)

print(f'Prediction statistics:')
print(f'  Min: {predictions.min():.3f}')
print(f'  Max: {predictions.max():.3f}')
print(f'  Mean: {predictions.mean():.3f}')
print(f'  Std: {predictions.std():.3f}')

print(f'\nRounded prediction distribution:')
unique, counts = np.unique(rounded_preds, return_counts=True)
for val, count in zip(unique, counts):
    pct = count / len(rounded_preds) * 100
    bar = '█' * int(pct / 2)
    print(f'  {val} items: {count:2d} ({pct:5.1f}%) {bar}')

print(f'\nUnique rounded predictions: {len(unique)} out of 5 possible')

if len(unique) < 3:
    print('\n❌ MODEL STILL PREDICTS TOO NARROWLY')
    print('   Even with diverse inputs, predictions cluster around mean')
else:
    print(f'\n✓ Model predicts {len(unique)} different values')
