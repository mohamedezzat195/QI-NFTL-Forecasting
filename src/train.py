import pandas as pd
import yfinance as yf
import requests

from model import QINFTLModel 

def get_financial_data():
    
    data = yf.download('^GSPC', start='2015-01-01', end='2025-12-31')
    return data[['Close']]

def get_weather_data():
    
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=51.5074&longitude=-0.1278&start_date=2020-01-01&end_date=2025-12-31&hourly=temperature_2m"
    r = requests.get(url).json()
    df = pd.DataFrame({'Temp': r['hourly']['temperature_2m']})
    return df

def train_model(dataset_name):
    
    print(f"Starting training on {dataset_name} dataset...")
    
    if dataset_name == "finance":
        df = get_financial_data()
    elif dataset_name == "weather":
        df = get_weather_data()
    
    # QI-NFTL
    model = QINFTLModel(n_inputs=5, n_rules=10)
    # model.fit(df) ...
    print(f"Training completed for {dataset_name}!")

if __name__ == "__main__":
   
    train_model("finance")
    train_model("weather")
