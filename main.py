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

    # Testing adding an event, removing an event, and getting specific event info
    # print(calendar.get_event_dict(), "\n\n")
    # calendar.add_event(['Quiz 9000', 'Test quiz', datetime.strptime('2023-11-01 09:30', '%Y-%m-%d %H:%M'), datetime.strptime('2023-11-05 09:30', '%Y-%m-%d %H:%M')])
    # print("\n", calendar.get_event_info('Quiz 9000'), "\n")
    # # calendar.remove_event('Quiz 9000')
    # # print(calendar.get_event_dict(), "\n")
    # event_dict = calendar.get_event_dict()

    # Comparing the end dates of each dictionary to the current date
    for key in event_dict.keys():
        counter = 0
        if key == "Date End":
            for value in event_dict[key]:
                remaining_time = compare_date_time(value)

                # Only display the upcoming events and events that have concluded within the past 24 hours
                if remaining_time != None:
                    print("%s: \t%s. \n" % (compare_date_time(value), event_dict['Summary'][counter]))
                counter += 1




main()