import pandas as pd

# Load merged data
df = pd.read_csv('outputs/merged_data.csv')

# Convert dates to datetime format
df['check_in_date'] = pd.to_datetime(df['check_in_date'], format='%d-%m-%Y')
df['checkout_date'] = pd.to_datetime(df['checkout_date'], format='%d-%m-%Y')
df['booking_date'] = pd.to_datetime(df['booking_date'], format='%d-%m-%Y')

# Add stay length (in days)
df['stay_length'] = (df['checkout_date'] - df['check_in_date']).dt.days

# Add lead time (in days before arrival)
df['lead_time'] = (df['check_in_date'] - df['booking_date']).dt.days

# Mark if booking was made for weekend (from day_type column)
df['is_weekend'] = df['day_type'].apply(lambda x: 1 if x == 'Weekend' else 0)

# Create binary cancellation flag
df['is_cancelled'] = df['booking_status'].apply(lambda x: 1 if x == 'Cancelled' else 0)

# Use revenue_realized if available, else revenue_generated
df['net_revenue'] = df['revenue_realized'].fillna(df['revenue_generated'])

# Save model-ready dataset
df.to_csv('outputs/model_ready.csv', index=False)
print("✅ Feature engineered data saved to outputs/model_ready.csv")
