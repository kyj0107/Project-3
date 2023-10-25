# This is mostly to refresh on Git commands, but it could also be a starting point.

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

def main():

    print("How about here we print out all the text, and then run the functions?")

main()