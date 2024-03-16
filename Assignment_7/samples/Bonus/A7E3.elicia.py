"""

-------

Author: Elicia Ramitt

-------



-------------

Name of File: A7E3.py (Assignment 7 Exercise 3)

-------------



------------

Description:  We will be converting hours, minutes, and seconds into seconds

------------ 



-------------------------------

Command to run Script from CLI:  python3 A7E3.py hr min sec

-------------------------------



------------------------------


Description of the Parameters: A7E3.py = this is the name of the file and is technically the first parameter

                               hr = this is the number of hour(s) that will be converted to seconds
                               min = this is the number of minute(s) that will be converted to seconds
                               sec = this is the number of second(s) that will be added to

------------------------------

"""

# Import argv file
from sys import argv
# Import date from datetime do get those sweet, sweet bonus marks
# import datetime for the datetime.datetime
import datetime
from datetime import datetime
# Get today's date and time

try:
    currentState = datetime.now()
    # Start of my favourite class (aka Scripting Fundamentals :P)
    #startOfClassStr = "2023/09/05 17:00:00"

    # Start of my favourite class (aka Scripting Fundamentals :P)
    #startOfClassStrToObj = datetime.datetime(2023, 9, 11, 17, 0, 0)

    # Start of class object
    startOfClassObj = datetime.fromisoformat('2023-09-11T17:00:00')

    # Difference between now and start of class
    #diff = currentState - startOfClassObj

    diff = currentState - startOfClassObj
    # Hours
    diffHours = diff.days // 24



    # days = time_diff.days
    # seconds = time_diff.seconds
    # hours = days * HOURS_PER_DAY + seconds // SECONDS_PER_MINUTE // MINUTES_PER_HOUR
    # minutes = (seconds // SECONDS_PER_MINUTE) % MINUTES_PER_HOUR
    # seconds = seconds % SECONDS_PER_MINUTE

    # Seconds
    diffSeconds = diff.seconds

    # Minutes
    #diffMins = diff.min 

    diffMins = (diff.seconds // 60) % 60
except:
    None

# calc_total_seconds function
def calc_total_seconds(hrs=diffHours, mins=diffMins, secs=diffSeconds):
    # Some constants
    SEC_PER_MIN = 60
    SEC_PER_HR = 3600

    # Try statement
    try:
        # Hrs to seconds
        total = int(hrs * SEC_PER_HR)
        total += int(mins * SEC_PER_MIN)
        total += int(secs)
    # Except statement
    except:
        return None
    return total

# Define main
def main():
    
    # Try statement
    try:
        # Hrs arg
        hrs = int(argv[1])
        # Min arg
        mins = int(argv[2])
        # Secs arg
        secs = int(argv[3])
        
        allSecs = calc_total_seconds()
        print(f"{hrs} hr {mins} min {secs} sec == {allSecs} sec")
    # Except statement
    except:
        allSecs = calc_total_seconds()
        print(f"{allSecs} sec")

        return None
    # Call function

    return allSecs


"""# Run Main"""
if __name__ == "__main__":
    main()