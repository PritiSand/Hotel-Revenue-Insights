import pandas as pd

# Load CSV files
bookings = pd.read_csv('data/fact_bookings.csv')
rooms = pd.read_csv('data/dim_rooms.csv')
hotels = pd.read_csv('data/dim_hotels.csv')
dates = pd.read_csv('data/dim_date.csv')

# Merge step-by-step
merged = bookings.merge(rooms, on='room_id', how='left')
merged = merged.merge(hotels, on='property_id', how='left')
merged = merged.merge(dates, on='check_in_date', how='left')

# Save merged file
merged.to_csv('outputs/merged_data.csv', index=False)
print("Successfully merged data and saved to outputs/merged_data.csv")
