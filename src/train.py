import yfinance as yf
import pandas as pd

def download_data():
    print("Downloading financial data from Yahoo Finance...")
    #  S&P 500
    df = yf.download('^GSPC', start='2015-01-01', end='2025-12-31')
    
    
    df[['Close']].to_csv('data/financial_data.csv')
    print("Data saved to data/financial_data.csv")

if __name__ == "__main__":
    download_data()
