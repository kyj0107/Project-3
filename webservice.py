import requests
import json

print("Stock Data Visualizer\n")

symbol = input("Enter the stock symbol you are looking for: ")

query = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + symbol + "&interval=5min&apikey=ZMES1H6BDGAXBBSH"

response = requests.get(query)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())
