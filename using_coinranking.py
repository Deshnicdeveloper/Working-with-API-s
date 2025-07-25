import requests

url = "https://api.coinranking.com/v2/coins"
api_key = "coinranking1ae5fcea386f31f326eddbcf53bda30152471f21bfd9b113"
params = {
    "referenceCurrencyUuid":"yhjMzLPhuIDl",
    "timePeriod":"3h",
    "orderBy":"marketCap",
    "limit" : "10",
    "orderDirection" : "desc",
}

headers = {
    "Content-Type": "application/json",
    'x-access-token': api_key,
}

response = requests.request("GET", url, headers=headers, params=params)

print(response)

data = response.json()
print(data)
results = data["data"]["coins"]
print(results)
# print(response.text)
for coin in results:
    # print(coin)
    print(f"{coin["name"]}({coin["symbol"]}) : {coin['price']}")