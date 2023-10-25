import requests
import json

#key: 9I22O100RNSZ6IPR

def jprint(obj):

    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def get_time_series(number):

    if number == 1:
        return ['INTRADAY', '60min']
    elif number == 2:
        return ['DAILY', 'null']
    elif number == 3:
        return ['WEEKLY', 'null']
    else:
        return ['MONTHLY', 'null']

def main():

    while True:

        try:

            print("\nSelect the Time Series of the chart you want to Generate")
            print("--------------------------------------------------------")
            print("1. Intraday\n2. Daily\n3. Weekly\n4. Monthly\n")
            answer = int(input("Enter the time series option (1, 2, 3, 4): "))

            url = 'https://www.alphavantage.co/query?function=TIME_SERIES_{}&symbol=IBM&interval={}&apikey=9I22O100RNSZ6IPR'.format(get_time_series(answer))

            response = requests.get(url)
            jprint(response.json())

            run_again = input("Would you like to view more stock data? Press 'y' to continue: ")
            if run_again.lower() != 'y':
                break

        except:

            print("Invalid option. Try again.")
            input()
            continue

main()