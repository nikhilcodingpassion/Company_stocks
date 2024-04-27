from yahoo_fin.stock_info import get_data
import pandas as pd
# List of tickers for 25 companies
df=pd.read_excel("C:\\Users\\nyala\\Downloads\\500 companies.xlsx",sheet_name='basics')
print(df)
ticker_list = df['Symbol']
print(ticker_list)  # Add more tickers

# Dictionary to store historical data for each company

# Fetch historical data for each ticker and store it in the dictionary
def stock_table():
    ticker_list = df['Symbol'] 
    for ticker in ticker_list:
        try:
            historical_data[ticker] = get_data(ticker, start_date = "01/01/2023", end_date = "02/17/2024", index_as_date = True, interval = "1d")
            print(ticker)
        except:
            pass
    return historical_data
# Dictionary to store historical data for each company
historical_data = {}
# Print the historical data for a specific company (e.g., AAPL)
print(stock_table())
