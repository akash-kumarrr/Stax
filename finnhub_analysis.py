from server import *
from dotenv import load_dotenv
import os
import finnhub 

load_dotenv()

finnhub_key = os.getenv('FINNHUB_KEY')

finnhub_client = finnhub.Client(api_key=finnhub_key)
stock_data = finnhub_client.quote('AAPL')
data ={
    'current_price' : stock_data['c'],
    'high_price' : stock_data['h'],
    'low_price' : stock_data['l'],
    'open_price' : stock_data['o'],
    'previous_close' : stock_data['pc'],
    'timestamp' : stock_data['t'],
    'volume' : stock_data['v']
}

