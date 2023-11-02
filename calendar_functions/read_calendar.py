# https://www.w3schools.com/python/python_classes.asp
# https://builtin.com/software-engineering-perspectives/python-cls
# https://realpython.com/python-pep8/

# https://stackoverflow.com/questions/3408097/parsing-files-ics-icalendar-using-python
from icalendar import Calendar as cal
from icalendar import Event
from datetime import datetime
from pytz import UTC

# https://www.tutorialspoint.com/downloading-files-from-web-using-python
import requests

from collections import defaultdict


class Calendar():
    print("Test")
    # Class constructor
    def __init__(self, calendar_url, event_dict=None):
        self.calendar_url = calendar_url
        self.event_dict = event_dict

    def read_calendar_url(self):
        # Initializing a dictionary to store all the event important details
        event_dict = {'Summary': [],
                      'Description' : [],
                      'Date Start': [],
                      'Date End': []}

        # Writing the calendar contents to a file called 'calendar.ics'
        r = requests.get(self.calendar_url, allow_redirects=True)
        open('calendar_functions/calendar.ics', 'wb').write(r.content)

        # Opening the file and reading it
        cal_ics_file = open('calendar_functions/calendar.ics', 'rb')
        calendar = cal.from_ical(cal_ics_file.read())

        # Looping through each event in the calendar and adding it to the dictionary
        for component in calendar.walk():
            if component.name == "VEVENT":
                event_dict['Summary'].append(component.get('SUMMARY').strip())
                event_dict['Description'].append(component.get('DESCRIPTION').strip())
                event_dict['Date Start'].append(component.get('DTSTART').dt)
                event_dict['Date End'].append(component.get('DTEND').dt)

        cal_ics_file.close()

        # for key in event_dict.keys():
        #     print("Key: ", key)
        #     for value in event_dict[key]:
        #         print("Value: ", value)

        return event_dict

    # Setting the dictionary
    def set_event_dict(self):
        self.event_dict = self.read_calendar_url()

    def get_event_dict(self):
        self.set_event_dict()
        return self.event_dict