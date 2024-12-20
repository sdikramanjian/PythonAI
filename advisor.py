import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr


class Advisor:
    #def __init__(self): 
        #yf.pdr_override()

    def recommend_stocks(self,investor_type):
        stocks_list= self.get_list_of_tickers()[:100] # get the top 1000 stocks (for performance reasons)
        string_stocks_list = [str(stock) for stock in stocks_list]
        #stock_data = pdr.get_data_yahoo(string_stocks_list, start="2023-07-01", end="2023-11-30") # from July 1 2023 until Nov 30 2023
        return stocks_list[:10] #placeholder until the logic is done
    
    
    def get_list_of_tickers(self):
        csv_file_path = 'data_sets/nasdaq_data_set.csv' # Specify the path to the nasdaq dataset file
        df = pd.read_csv(csv_file_path) # Read the CSV file into a pandas DataFrame
        ticker_values = df.iloc[:, 1].tolist() # Extract only the Company name
        return ticker_values # Return the list of ticker symbols
      