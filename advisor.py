import yfinance as yf
from pandas_datareader import data as pdr

class Advisor:
    def __init__(self):
        yf.pdr_override()

    def recommend_stocks(self,investor_type):
        data = pdr.get_data_yahoo("AAPL", start="2017-01-01", end="2023-09-30") # from Jan 1 2017 until Sept 30 2023
        return ['AAPL', 'GOOG', 'MSFT']