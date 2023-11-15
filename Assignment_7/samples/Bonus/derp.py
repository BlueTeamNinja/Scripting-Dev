INCHES_PER_FEET = 12

while True:
    try:
        distance_in_inches = int(input("Enter a distance in inches: "))
        if distance_in_inches < 0:
            distance_in_inches *= -1
            sign = "-"
        else:
            sign = ""
        feet = distance_in_inches // INCHES_PER_FEET
        inches = distance_in_inches % INCHES_PER_FEET
        if sign == "-":
            feet *= -1
        print(f"{sign}{distance_in_inches}\" == {feet}'{inches}\"")
        break
    except ValueError:
        print("Error: Distance in inches must be an integer.")
