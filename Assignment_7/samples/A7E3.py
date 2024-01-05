# Constants
SEC_PER_MIN = 60
SEC_PER_HOUR = 3600


# Main Body
def main():
    """ Main Body of Script """
    # Get command line arguments
    hours = sys.argv[1]
    minutes = sys.argv[2]
    seconds = sys.argv[3]
   
    # Calculate total seconds
    total_seconds = calc_total_seconds(hours, minutes, seconds)

# Functions
def calc_total_seconds(hours, minutes, seconds):
    """ Calculate total seconds from hours, minutes, and seconds """
    try:
        # Choose one of the math methods to solve this - you can even do it all on one line if you want
        hours_to_seconds = int(hours) * SEC_PER_HOUR
        minutes_to_seconds = int(minutes) * SEC_PER_MIN
        # Make sure seconds gets converted, too, in case some smartass prof tests with the value 'bananas'
        seconds = int(seconds)
        total_seconds = hours_to_seconds # + the rest of the math
        return total_seconds
    except:
        return None

# Main script
if __name__ == "__main__":
    main()