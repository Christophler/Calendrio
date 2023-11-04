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


class Calendar():
    def __init__(self, calendar_url, event_dict=None):
        """ Class constructor. """
        self.calendar_url = calendar_url
        self.event_dict = event_dict

    
    def set_event_dict(self, value):
        """ Setter for the dictionary that holds all the calendar's event information. """
        self.event_dict = value


    def get_event_dict(self):
        """ Getter for the dictionary that holds all the calendar's event information. """
        return self.event_dict
    


    def read_calendar_url(self):
        """ Reads a calendar using the object's calendar URL.
        Returns a dictionary with all the events and their important information.
        """
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


    def add_event(self, info_list):
        counter = 0
        for key in self.event_dict.keys():
            self.event_dict[key].append(info_list[counter])
            counter += 1