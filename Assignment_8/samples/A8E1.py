def the_difference(a, b):
    """
    Subtracts the smaller number from the larger number and returns the result.
    Returns None if either input is not an integer.
    """
    try: 
        a = int(a)
        b = int(b)
    except:
        return None

    if a > b:
        return a - b
    elif b > a:
        return b - a
    else:
        return 0

def main():
    print(the_difference(13, 28))
    print(the_difference(123, 45))
    print(the_difference(52, 52))
    print(the_difference(-45, 12))
    print(the_difference(-67, -112))
    print(the_difference(5, 'Chuck Norris'))

# Python incantation
if __name__ == "__main__":
    main()
    