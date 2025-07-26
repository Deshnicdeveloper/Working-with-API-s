import csv
import os

import requests

endpoint = "https://api.coinranking.com/v2/coins"

api_key = "<key>"
method = "GET"
headers = {
    'x-access-token': api_key,
    'content-type': 'application/json'
}

#here we have our parameters
paramaters = {
    "referenceCurrencyUuid":"yhjMzLPhuIDl",
    "timePeriod":"1h",
    "orderBy":"marketCap",
    "limit": "20"
}

response = requests.request(method, endpoint, params=paramaters, headers=headers)

data = response.json()
# print(data)

if os.path.exists('coin.csv'):
    with open("coin.csv", 'w' ,newline="") as file:
        write = csv.writer(file)
        write.writerow(['Name', 'Symbol', 'Price'])

coins = data['data']['coins']
# print(coins)
# print(response.text)
for coin in coins:
    # print(coin)
    print(f"{coin['name']}({coin['symbol']}): {coin['price']}")
    with open("coin.csv", 'a' ,newline="") as file:
        write = csv.writer(file)
        price = f"{coin['price']}"
        write.writerow([coin['name'], coin['symbol'], coin['price']])
