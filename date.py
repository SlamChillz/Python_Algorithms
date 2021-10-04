# A function to output date differnce in days. Date format must be 'YYYY-MM-DD'

from datetime import *

def dayDifference(dayOne, dayTwo):
    try:
        dayOne = date.fromisoformat(str(dayOne))
        dayTwo = date.fromisoformat(str(dayTwo))
    except ValueError:
        return("Error! Ensure the date format is 'YYYY-MM-DD'")
    else:
        diff =abs((dayOne-dayTwo).days)
        return("The difference between {} and {} in day(s) is: {}".format(dayOne, dayTwo, diff))
