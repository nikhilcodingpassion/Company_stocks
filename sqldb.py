import mysql.connector
import API
from sqlalchemy import MetaData, Table, Column, Date, Float, String
# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="mysql"
)

# Create a Cursor
cursor = conn.cursor()

# Ensure any existing result sets are consumed
for result in cursor.stored_results():
    result.fetchall()

# Create a table to store stock data
metadata = MetaData()
stocks_table = Table(
    "stock_table",
    metadata,
    Column("ticker", String(20)),  # Ticker symbol
    Column("date", Date),
    Column("open", Float),
    Column("high", Float),
    Column("low", Float),
    Column("close", Float),
    Column("volume", Float)
)

# Check if the table already exists
cursor.execute("SHOW TABLES LIKE 'stocks_table'")
if cursor.fetchone():
    print("Table 'stocks' already exists.")
else:
    # Create the table (if not exists)
    cursor.execute(f"CREATE TABLE stocks_table ("
                   f"ticker VARCHAR(20), "
                   f"date DATE, "
                   f"open FLOAT, "
                   f"high FLOAT, "
                   f"low FLOAT, "
                   f"close FLOAT, "
                   f"volume FLOAT"
                   f")")
    print("Table 'stocks' created successfully.")
cursor.execute("DELETE FROM stocks_table")
# Assuming data is a DataFrame containing the stock data
for ticker, df in API.historical_data.items():
    for index, row in df.iterrows():
        date = index.strftime('%Y-%m-%d')
        open_price = row['open']
        high_price = row['high']
        low_price = row['low']
        close_price = row['close']
        volume = row['volume']
        #print(date,open_price,high_price)
        #print("hello world")
        # Insert the values into the database
        cursor.execute(
            """
            INSERT INTO stocks_table(ticker, date, open, high, low, close, volume)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (ticker, date, open_price, high_price, low_price, close_price, volume)
        )

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()


