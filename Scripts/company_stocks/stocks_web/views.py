# stocks/views.py
import matplotlib
matplotlib.use('Agg')
from django.shortcuts import render
from .models import Stock
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import json

def index(request):
    return render(request, 'stocks/index.html')

def stock_detail(request):
    if request.method == 'POST':
        ticker = request.POST.get('ticker')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        # Retrieve stock data from the database based on user input
        stocks = Stock.objects.filter(ticker=ticker, date__range=[start_date, end_date])
        
        # Extract dates, open prices, high prices, low prices, and close prices
        dates = [stock.date.strftime("%Y-%m-%d") for stock in stocks]
        open_prices = [stock.open for stock in stocks]
        high_prices = [stock.high for stock in stocks]
        low_prices = [stock.low for stock in stocks]
        close_prices = [stock.close for stock in stocks]
        
        # Convert data to JSON format
        data = {
            'dates': dates,
            'open_prices': open_prices,
            'high_prices': high_prices,
            'low_prices': low_prices,
            'close_prices': close_prices
        }
        data_json = json.dumps(data)
        
        # Plotting
        # Plotting
        plt.figure(figsize=(20, 6))  # Increase width to accommodate more x-axis labels
        plt.plot(dates, close_prices, marker='o', linestyle='-')
        plt.title('Stock Graph')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.grid(True)

        # Rotate x-axis labels by 45 degrees
        plt.xticks(rotation=45)

        # Adjust layout to prevent clipping of labels
        plt.tight_layout()

        # Save or display the plot

        
        # Convert the plot to a bytes object
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        
        # Encode the bytes object as base64
        plot_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()
        
        # Fetch other details
        # Example: Fetching other details like cursor and table
        cursor = []
        for i in range(len(dates)):
            cursor.append({
                'date': dates[i],
                'open_price': open_prices[i],
                'high_price': high_prices[i],
                'low_price': low_prices[i],
                'close_price': close_prices[i]
            })

        # Render the template with all the data
        return render(request, 'stocks/stock_detail.html', {'plot_data': plot_data, 'data': data_json, 'cursor': cursor})
