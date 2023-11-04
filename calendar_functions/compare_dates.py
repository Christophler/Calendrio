from datetime import datetime
import pytz


def compare_date_time(comparisondt):
    """  Returns the number of days in between the given datetime object and the current datetime.

    Arguments:
    comparisondt - The datetime object that is being compared 
    """
    # Setting both of the datetime objects to aware to compare them
    utc = pytz.UTC
    now = utc.localize(datetime.now())

    # Comparing the passed datetime object to the current time
    if comparisondt > now:
        time_diff = str(comparisondt - now).split(' ', 1)
        behind_or_left = "left"
    elif comparisondt < now:
        time_diff = str(now - comparisondt).split(' ', 1)
        behind_or_left = "behind"
    else:
        return("You have no time left. It's due NOW!")
    
           
    # Checking if the time is under 24 hours
    if ":" in time_diff[0]:
        time_diff = time_diff[0].split(':', 2)
        return("You only have %s hours and %s minutes %s" % (time_diff[0], time_diff[1], behind_or_left))

    # Checking if there's only one day remaining
    if time_diff[0] == "1":
        return("You have %s more day %s" % (time_diff[0], behind_or_left))
    
    return("You have %s more days %s" % (time_diff[0], behind_or_left))