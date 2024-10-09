import pandas as pd

# Use the raw link for the CSV file
data = pd.read_csv('https://raw.githubusercontent.com/saikumar1624/gold_price_dataset/main/gold_prices.csv')

# Check the first few rows to confirm it loaded successfully
print(data.head())
