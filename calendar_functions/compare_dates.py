from datetime import datetime
import pytz


def compare_date_time(comparisondt):
    """  Returns the number of days in between the given datetime object and the current datetime only if it is not over 24 hours past in the past.

    Arguments:
    comparisondt - The datetime object that is being compared 
    """
    # Setting both of the datetime objects to aware to compare them
    utc = pytz.UTC
    now = utc.localize(datetime.now())
    # Checking if the comparison datetime object is naive. If it is, make it aware.
    if comparisondt.tzinfo == None or comparisondt.tzinfo.utcoffset(comparisondt) == None:
        comparisondt = utc.localize(comparisondt)

    # Comparing the passed datetime object to the current time
    if comparisondt > now:
        time_diff = str(comparisondt - now).split(' ', 1)
        behind_or_left = ["have", "left until"]
    elif comparisondt < now:
        time_diff = str(now - comparisondt).split(' ', 1)
        behind_or_left = ["are", "behind for"]
    else:
        return("You have no time left. It's due NOW!")
    
           
    # Checking if the time is under 24 hours
    if ":" in time_diff[0]:
        time_diff = time_diff[0].split(':', 2)
        return("You %s %s hours and %s minutes %s" % (behind_or_left[0], time_diff[0], time_diff[1], behind_or_left[1]))

    # Checking if there's only one day remaining
    if int(time_diff[0] == 1):
        return("You %s 1 day %s" % (behind_or_left[0], behind_or_left[1]))
    
    # Checking if there's more than one day has passed since the due date
    if int(time_diff[0]) > 1 and "behind" not in behind_or_left[1]:
        return("You %s %s more days left until" % (behind_or_left[0], time_diff[0]))
    else:
        return(None)