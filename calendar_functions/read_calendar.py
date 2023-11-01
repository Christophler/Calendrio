# https://www.w3schools.com/python/python_classes.asp
# https://builtin.com/software-engineering-perspectives/python-cls
# https://realpython.com/python-pep8/

# https://stackoverflow.com/questions/3408097/parsing-files-ics-icalendar-using-python
from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC

# https://www.tutorialspoint.com/downloading-files-from-web-using-python
import requests

class Calendar():
    print("Test")
    # Class constructor
    def __init__(self, calendar_url):
        self.calendar_url = calendar_url

    def read_calendar_url(self):
        r = requests.get(self.calendar_url, allow_redirects=True)

        open('calendar_functions/calendar.ics', 'wb').write(r.content)



