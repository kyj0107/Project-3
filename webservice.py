# This is mostly to refresh on Git commands, but it could also be a starting point.
import requests
import json
import pygal
from datetime import datetime
import webbrowser


def get_chart():
    while True:
        chart_type = ''
        try: 
            print("\nChart Types\n---------------\n 1. Bar \n 2. Line\n")
            chart = input("Enter the chart type you want (1,2): ")
            if chart == "1":
                chart_type = 'Bar'
                break
            elif chart == "2":
                chart_type = 'Line'
                break
            else:
                print("Invalid Chart Type! Try Again!")
        except Exception as error:
            print("Invalid Chart Type! Try Again!")
    return chart_type

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
    
start_date = input("Enter the beginning date in YYYY-MM-DD format: ")
end_date = input("Enter the end date in YYYY-MM-DD format: ")
# Validate the dates
try:
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")
    exit()

if end_date_obj < start_date_obj:
    print("End date cannot be before the start date.")
    exit()

def main():

    while True:

        try:

            print("\nSelect the Time Series of the chart you want to Generate")
            print("--------------------------------------------------------")
            print("1. Intraday\n2. Daily\n3. Weekly\n4. Monthly\n")
            answer = int(input("Enter the time series option (1, 2, 3, 4): "))

            if answer > 4 or answer < 0:

                print("Invalid input. Please enter a number between 1 and 4.")
                input()
                continue

            values = get_time_series(answer)

            url = 'https://www.alphavantage.co/query?function=TIME_SERIES_{}&symbol=IBM&interval={}&apikey=9I22O100RNSZ6IPR'.format(values[0], values[1])

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