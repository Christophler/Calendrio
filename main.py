from calendar_functions.read_calendar import *

def main():
    print("Hello world")
    # Testing
    calendar_url = input("Enter the calendar download url: ")

    calendar = Calendar(calendar_url)

    event_dict = calendar.get_event_dict()

    # for key in event_dict.keys():
    #     print("Key: ", key)
    #     for value in event_dict[key]:
    #         print("Value: ", value)

main()