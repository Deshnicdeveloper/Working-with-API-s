import requests

url = "https://coinranking1.p.rapidapi.com/coins"

querystring = {
    "referenceCurrencyUuid":"yhjMzLPhuIDl",
    "timePeriod":"24h",
    "tiers":"1",
    "orderBy":"marketCap",
    "orderDirection":"desc",
    "limit":"50",
    "offset":"0"
}

headers = {
    "x-rapidapi-key": "<key>",
    "x-rapidapi-host": "coinranking1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

# Access the list of coins
coins = data["data"]["coins"]

# Loop through the first 5 coins and print details
for coin in coins[:5]:
    name = coin["name"]
    symbol = coin["symbol"]
    price = coin["price"]
    print(f"{name} ({symbol}): ${price}")
