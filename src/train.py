import pandas as pd
import yfinance as yf
import requests

def fetch_and_save_data():
    # 1. جلب بيانات مالية (S&P 500)
    print("Fetching Financial Data...")
    df_finance = yf.download('^GSPC', start='2020-01-01', end='2025-12-31')
    df_finance.to_csv('data/financial_data.csv')

    # 2. جلب بيانات الطقس
    print("Fetching Weather Data...")
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=51.5074&longitude=-0.1278&start_date=2020-01-01&end_date=2025-12-31&hourly=temperature_2m"
    response = requests.get(url)
    weather_json = response.json()
    df_weather = pd.DataFrame({
        'time': weather_json['hourly']['time'],
        'temp': weather_json['hourly']['temperature_2m']
    })
    df_weather.to_csv('data/weather_data.csv', index=False)
    
    print("✅ All data saved to CSV files in /data folder")

if __name__ == "__main__":
    fetch_and_save_data()
