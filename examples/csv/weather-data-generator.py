import pandas as pd
import random
from datetime import datetime, timedelta

# List of example values
countries = ['USA']
import random
from datetime import datetime, timedelta

# List of example values
locations = ['New York', 'Los Angeles', 'Chicago', 'San Francisco']
countries = ['USA']
temperatures = [random.uniform(0, 40) for _ in range(10)]  # Generate random temperatures
humidity = [random.uniform(20, 80) for _ in range(10)]  # Generate random humidity levels
wind_speed = [random.uniform(0, 20) for _ in range(10)]  # Generate random wind speeds
weather_conditions = ['Clear', 'Cloudy', 'Rainy', 'Snowy']
precipitation = [random.uniform(0, 10) for _ in range(10)]  # Generate random precipitation levels
pressure = [random.uniform(980, 1040) for _ in range(10)]  # Generate random atmospheric pressure levels

# Generate dataset
data = []
for i in range(10):
    location = random.choice(locations)
    country = random.choice(countries)
    date_time = (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d %H:%M:%S')
    temperature = round(random.choice(temperatures), 2)
    humidity_level = round(random.choice(humidity), 2)
    wind_speed_value = round(random.choice(wind_speed), 2)
    weather_condition = random.choice(weather_conditions)
    precipitation_level = round(random.choice(precipitation), 2)
    atmospheric_pressure = round(random.choice(pressure), 2)

    row = [location, country, date_time, temperature, humidity_level, wind_speed_value, weather_condition, precipitation_level, atmospheric_pressure]
    data.append(row)

# Create DataFrame
USA = 'USA'
df = pd.DataFrame(data, columns=["location", "country", "date_time", "temperature", "humidity", "wind_speed", "weather_condition", "precipitation", "pressure"])

# Save to CSV
df.to_csv('./examples/csv/weather_data.csv', index=False)

print('Weather dataset generated and saved to weather_data.csv')
cities = ['New York', 'Los Angeles', 'San Francisco']
states = ['NY', 'CA', 'IL']
regions = ['East', 'West', 'Central', 'South']
categories = ['Footwear']
sub_categories = ['Men Shoes', 'Women Shoes']
brands = ['Nike', 'Adidas', "Reebok", "Puma"]
product_names = ['Running Shoes', 'Casual Shoes', 'Formal Shoes']
currencies = ['USD']
addresses = ['123 Main St', '456 Market St', '789 Elm St', '321 Oak St', '100 Pine St']

# Generate dataset
data = []
for i in range(10):
    discount_until = (datetime.now() + timedelta(days=random.randint(0, 364))).strftime('%Y-%m-%d')
    country = random.choice(countries)
    city = random.choice(cities)
    state = random.choice(states)
    postal_code = str(random.randint(10000, 99999))
    region = random.choice(regions)
    product_id = str(random.randint(1000, 9999))
    category = random.choice(categories)
    sub_category = random.choice(sub_categories)
    brand = random.choice(brands)
    product_name = random.choice(product_names)
    currency = random.choice(currencies)
    actual_price = round(random.uniform(50, 200), 0)
    discount_percentage = random.randint(5, 30)
    discount_price = round(actual_price * (1 - discount_percentage / 100), 0)
    address = random.choice(addresses)

    row = [discount_until, country, city, state, postal_code, region, product_id, category, sub_category, brand, product_name, currency, actual_price, discount_price, discount_percentage, address]
    data.append(row)

# Create DataFrame
df = pd.DataFrame(data, columns=["discount_until", "country", "city", "state", "postal_code", "region", "product_id", "category", "sub_category", "brand", "product_name", "currency", "actual_price", "discount_price", "discount_percentage", "address"])

# Save to CSV
df.to_csv('./examples/csv/discounts.csv', index=False)

print('Dataset generated and saved to future_discounts.csv')
