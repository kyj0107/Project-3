import requests
import json

#key: 9I22O100RNSZ6IPR

def jprint(obj):

    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def get_time_series(number):

    if number == 1:
        return 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=60min&apikey=9I22O100RNSZ6IPR'
    elif number == 2:
        return 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=9I22O100RNSZ6IPR'
    elif number == 3:
        return 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=9I22O100RNSZ6IPR'
    else:
        return 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey=9I22O100RNSZ6IPR'

def main():

    url = ""

    while True:

        try:

            print("\nSelect the Time Series of the chart you want to Generate")
            print("--------------------------------------------------------")
            print("1. Intraday\n2. Daily\n3. Weekly\n4. Monthly\n")
            answer = int(input("Enter the time series option (1, 2, 3, 4): "))

            response = requests.get(get_time_series(answer))
            jprint(response.json())

            run_again = input("Would you like to view more stock data? Press 'y' to continue: ")
            if run_again.lower() != 'y':
                break

        except:

            print("Invalid option. Try again.")
            input()
            continue

main()