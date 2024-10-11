from datetime import datetime, timedelta

# Define start and end dates
start_date = datetime(2025, 4, 1)
end_date = datetime(2025, 12, 31)

# Create dictionary comprehension with date format 'YYYY-MM-DD'
dates_dict = {(start_date + timedelta(days=i)).strftime('%Y-%m-%d'): 1 for i in range((end_date - start_date).days + 1)}

# Print the result (optional)
print(dates_dict)
