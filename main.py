from calendar_functions.read_calendar import *

def main():
    print("Hello world")
    # Testing
    calendar_url = input("Enter the calendar download url: ")

    calendar = Calendar(calendar_url)
    
    calendar.read_calendar_url()

main()