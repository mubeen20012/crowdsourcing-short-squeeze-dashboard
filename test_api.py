import requests
import json

url = 'http://127.0.0.1:5000/predict'

data = {
    "features": [
        265.00,   # open_price
        483.00,   # high_price
        112.25,   # low_price
        193.60,   # close_price
        58815800, # volume
        193.60,   # adjclose_price
        -26.94,   # daily_return_pct
        370.75,   # price_range
        361.80,   # avg_price
        193.60,   # MA10
        193.60,   # MA50
        193.60    # VWAP
    ]
}

response = requests.post(url, json=data)
print(response.json())
