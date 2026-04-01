"""
Final demo: Show that model now predicts varying quantities
"""
import pickle
import pandas as pd

with open('cafe_sales_model.pkl', 'rb') as f:
    model_data = pickle.load(f)

model = model_data['model']
le = model_data['label_encoders']

print("="*70)
print("FINAL DEMONSTRATION: MODEL NOW PREDICTS VARYING QUANTITIES")
print("="*70)
print(f"Model: {type(model).__name__}")
print(f"Features: {len(model_data['feature_cols'])}")
print()

# Test cases with ACTUAL item prices from the data
# Each item has a fixed price in this dataset
test_scenarios = [
    ("Cookie (cheapest)", "Cookie", 1.0, "Cash", "In-store", "January", "Monday"),
    ("Tea (cheap)", "Tea", 1.5, "Digital Wallet", "Takeaway", "March", "Saturday"),
    ("Coffee (mid)", "Coffee", 2.0, "Credit Card", "In-store", "June", "Wednesday"),
    ("Cake (mid)", "Cake", 3.0, "Cash", "Takeaway", "September", "Friday"),
    ("Juice (mid)", "Juice", 3.0, "Digital Wallet", "In-store", "December", "Sunday"),
    ("Sandwich (high)", "Sandwich", 4.0, "Credit Card", "Takeaway", "February", "Tuesday"),
    ("Smoothie (high)", "Smoothie", 4.0, "Cash", "In-store", "July", "Thursday"),
    ("Salad (highest)", "Salad", 5.0, "Digital Wallet", "Takeaway", "May", "Saturday"),
]

print("Testing with ACTUAL item prices + varying contexts:")
print("-" * 70)

predictions = []
for scenario, item, price, payment, location, month, dow in test_scenarios:
    month_map = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    
    input_df = pd.DataFrame({
        'Item_Encoded': [le['Item'].transform([item])[0]],
        'Price Per Unit': [price],
        'Payment Method_Encoded': [le['Payment Method'].transform([payment])[0]],
        'Location_Encoded': [le['Location'].transform([location])[0]],
        'Month': [month_map[month]],
        'Day_of_Month': [15],
        'Month Name_Encoded': [le['Month Name'].transform([month])[0]],
        'Day of Week_Encoded': [le['Day of Week'].transform([dow])[0]],
        'Quarter': [(month_map[month]-1)//3 + 1],
        'Is_Weekend': [1 if dow in ['Saturday', 'Sunday'] else 0],
        'Week_of_Year': [month_map[month] * 4]
    })
    
    pred = model.predict(input_df)[0]
    rounded = int(round(pred))
    predictions.append(rounded)
    
    stars = "⭐" * rounded
    print(f"{scenario:25s} ${price:.1f} {month[:3]} {dow[:3]:3s} → {pred:.2f} = {rounded} items {stars}")

print()
print("="*70)
print("SUMMARY")
print("="*70)
print(f"Unique predictions: {len(set(predictions))} out of 5 possible")
print(f"Prediction range: {min(predictions)} to {max(predictions)} items")
print(f"All different quantities predicted: {sorted(set(predictions))}")

if len(set(predictions)) == 1:
    print("\n❌ PROBLEM: Model still predicts only one value")
elif len(set(predictions)) < 3:
    print(f"\n⚠️  LIMITED: Model only predicts {len(set(predictions))} different values")
else:
    print(f"\n✅ SUCCESS: Model predicts {len(set(predictions))} different values!")
    print("   Model is now responsive to different inputs!")
