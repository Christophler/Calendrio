from calendar_functions.calendar import *
from calendar_functions.compare_dates import *


def main():
    """ Creates a calendar object and checks how many days there are until each event ends. """
    # Testing
    calendar_url = input("Enter the calendar download url: ")

    # Creating the calendar object
    calendar = Calendar(calendar_url)

    # Setting and getting the calendar's event dictionary
    calendar.set_event_dict(calendar.read_calendar_url())
    event_dict = calendar.get_event_dict()

    # for key in event_dict.keys():
    #     print("Key: ", key)
    #     for value in event_dict[key]:
    #         print("Value: ", value)

    # Comparing the end dates of each dictionary to the current date
    for key in event_dict.keys():
        counter = 0
        if key == "Date End":
            for value in event_dict[key]:
                print("%s for the following event: \t%s. \n" % (compare_date_time(value), event_dict['Summary'][counter]))
                counter += 1


main()