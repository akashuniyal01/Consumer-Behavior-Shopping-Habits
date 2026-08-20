import streamlit as st
import joblib
import numpy as np

# Load the trained model (assumed to be saved as 'linear_regression_model.pkl')
model = joblib.load('linear_regression_model.pkl')

# App title
st.title('Purchase Prediction App')

# Q1: Age
age = st.slider('Age', 1, 100, 25)

# Q2: Gender
gender = st.radio('Gender', ['Male', 'Female'])

# Q3: Item Purchased
item_purchased = st.selectbox('Item Purchased', [
    'Blouse', 'Jewelry', 'Pants', 'Shirt', 'Dress', 'Sweater', 'Jacket', 'Belt',
    'Sunglasses', 'Coat', 'Sandals', 'Socks', 'Skirt', 'Shorts', 'Scarf', 'Hat',
    'Handbag', 'Hoodie', 'Shoes', 'T-shirt', 'Sneakers', 'Boots', 'Backpack',
    'Gloves', 'Jeans'])

# Q4: Category
category = st.selectbox('Category', ['Clothing', 'Accessories', 'Footwear', 'Outerwear'])

# Q5: Location
location = st.selectbox('Location', [
    'Montana', 'California', 'Idaho', 'Illinois', 'Alabama', 'Minnesota',
    'Nebraska', 'New York', 'Nevada', 'Maryland', 'Delaware', 'Vermont',
    'Louisiana', 'North Dakota', 'Missouri', 'West Virginia', 'New Mexico',
    'Mississippi', 'Indiana', 'Georgia', 'Kentucky', 'Arkansas', 'North Carolina',
    'Connecticut', 'Virginia', 'Ohio', 'Tennessee', 'Texas', 'Maine',
    'South Carolina', 'Colorado', 'Oklahoma', 'Wisconsin', 'Oregon', 'Pennsylvania',
    'Washington', 'Michigan', 'Alaska', 'Massachusetts', 'Wyoming', 'Utah',
    'New Hampshire', 'South Dakota', 'Iowa', 'Florida', 'New Jersey', 'Hawaii',
    'Arizona', 'Kansas', 'Rhode Island'])

# Q6: Size
size = st.radio('Size', ['M', 'L', 'S', 'XL'])

# Q7: Color
color = st.selectbox('Color', [
    'Olive', 'Yellow', 'Silver', 'Teal', 'Green', 'Black', 'Cyan', 'Violet',
    'Gray', 'Maroon', 'Orange', 'Charcoal', 'Pink', 'Magenta', 'Blue', 'Purple',
    'Peach', 'Red', 'Beige', 'Indigo', 'Lavender', 'Turquoise', 'White', 'Brown', 'Gold'])

# Q8: Season
season = st.selectbox('Season', ['Spring', 'Fall', 'Winter', 'Summer'])

# Q9: Review Rating
review_rating = st.slider('Review Rating', 0.0, 5.0, 4.0)

# Q10: Subscription Status
subscription_status = st.radio('Subscription Status', ['Yes', 'No'])

# Q11: Shipping Type
shipping_type = st.selectbox('Shipping Type', [
    'Free Shipping', 'Standard', 'Store Pickup', 'Next Day Air', 'Express', '2-Day Shipping'])

# Q12: Discount Applied
discount_applied = st.radio('Discount Applied', ['Yes', 'No'])

# Q13: Promo Code Used
promo_code_used = st.radio('Promo Code Used', ['Yes', 'No'])

# Q14: Previous Purchases
previous_purchases = st.slider('Previous Purchases (USD)', 0, 60, 30)

# Q15: Payment Method
payment_method = st.selectbox('Payment Method', [
    'PayPal', 'Credit Card', 'Cash', 'Debit Card', 'Venmo', 'Bank Transfer'])

# Q16: Frequency of Purchases
frequency_of_purchases = st.selectbox('Frequency of Purchases', [
    'Every 3 Months', 'Annually', 'Quarterly', 'Monthly', 'Bi-Weekly', 'Fortnightly', 'Weekly'])

# Mapping categorical variables to numerical values
gender_map = {'Male': 0, 'Female': 1}
item_map = {item: idx for idx, item in enumerate([
    'Blouse', 'Jewelry', 'Pants', 'Shirt', 'Dress', 'Sweater', 'Jacket', 'Belt',
    'Sunglasses', 'Coat', 'Sandals', 'Socks', 'Skirt', 'Shorts', 'Scarf', 'Hat',
    'Handbag', 'Hoodie', 'Shoes', 'T-shirt', 'Sneakers', 'Boots', 'Backpack',
    'Gloves', 'Jeans'])}
category_map = {'Clothing': 0, 'Accessories': 1, 'Footwear': 2, 'Outerwear': 3}
location_map = {location: idx for idx, location in enumerate([
    'Montana', 'California', 'Idaho', 'Illinois', 'Alabama', 'Minnesota',
    'Nebraska', 'New York', 'Nevada', 'Maryland', 'Delaware', 'Vermont',
    'Louisiana', 'North Dakota', 'Missouri', 'West Virginia', 'New Mexico',
    'Mississippi', 'Indiana', 'Georgia', 'Kentucky', 'Arkansas', 'North Carolina',
    'Connecticut', 'Virginia', 'Ohio', 'Tennessee', 'Texas', 'Maine',
    'South Carolina', 'Colorado', 'Oklahoma', 'Wisconsin', 'Oregon', 'Pennsylvania',
    'Washington', 'Michigan', 'Alaska', 'Massachusetts', 'Wyoming', 'Utah',
    'New Hampshire', 'South Dakota', 'Iowa', 'Florida', 'New Jersey', 'Hawaii',
    'Arizona', 'Kansas', 'Rhode Island'])}
size_map = {'M': 0, 'L': 1, 'S': 2, 'XL': 3}
color_map = {color: idx for idx, color in enumerate([
    'Olive', 'Yellow', 'Silver', 'Teal', 'Green', 'Black', 'Cyan', 'Violet',
    'Gray', 'Maroon', 'Orange', 'Charcoal', 'Pink', 'Magenta', 'Blue', 'Purple',
    'Peach', 'Red', 'Beige', 'Indigo', 'Lavender', 'Turquoise', 'White', 'Brown', 'Gold'])}
season_map = {'Spring': 0, 'Fall': 1, 'Winter': 2, 'Summer': 3}
subscription_status_map = {'Yes': 1, 'No': 0}
shipping_type_map = {stype: idx for idx, stype in enumerate([
    'Free Shipping', 'Standard', 'Store Pickup', 'Next Day Air', 'Express', '2-Day Shipping'])}
discount_applied_map = {'Yes': 1, 'No': 0}
promo_code_used_map = {'Yes': 1, 'No': 0}
payment_method_map = {method: idx for idx, method in enumerate([
    'PayPal', 'Credit Card', 'Cash', 'Debit Card', 'Venmo', 'Bank Transfer'])}
frequency_of_purchases_map = {freq: idx for idx, freq in enumerate([
    'Every 3 Months', 'Annually', 'Quarterly', 'Monthly', 'Bi-Weekly', 'Fortnightly', 'Weekly'])}

# Converting inputs to numeric format
gender_num = gender_map[gender]
item_num = item_map[item_purchased]
category_num = category_map[category]
location_num = location_map[location]
size_num = size_map[size]
color_num = color_map[color]
season_num = season_map[season]
subscription_status_num = subscription_status_map[subscription_status]
shipping_type_num = shipping_type_map[shipping_type]
discount_applied_num = discount_applied_map[discount_applied]
promo_code_used_num = promo_code_used_map[promo_code_used]
payment_method_num = payment_method_map[payment_method]
frequency_of_purchases_num = frequency_of_purchases_map[frequency_of_purchases]

# Prepare the feature array for prediction
input_features = np.array([
    age, gender_num, item_num, category_num, location_num, size_num,
    color_num, season_num, review_rating, subscription_status_num,
    shipping_type_num, discount_applied_num, promo_code_used_num,
    previous_purchases, payment_method_num, frequency_of_purchases_num
]).reshape(1, -1)


    
# Prediction
if st.button('Predict Purchase Amount'):
    prediction = model.predict(input_features)

    # Purchase amount predicted by the model in USD
    purchase_usd = prediction[0]

    # USD to INR conversion
    usd_to_inr = 95
    purchase_inr = purchase_usd * usd_to_inr

    # Display prediction
    st.success("Purchase Prediction")

    st.write(f"💵 Purchase Amount in USD: **${purchase_usd:.2f}**")
    st.write(f"🇮🇳 Purchase Amount in INR: **₹{purchase_inr:,.2f}**")