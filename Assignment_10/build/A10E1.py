"""
A10E1.py: A Python module with functions to analyze a tuple (or list) of integers.

This script provides three functions:
- all_divisible(): Checks if all integers in a tuple are divisible by a given divisor.
- any_divisible(): Checks if any integer in a tuple is divisible by a given divisor.
- difference(): Calculates the difference of integers in a tuple when sorted in descending order.
"""

def all_divisible(numbers, divisor):
    """
    Check if all integers in the tuple are divisible by the divisor.

    Parameters:
    numbers (tuple or list): A tuple or list of integers.
    divisor (int): The divisor to check divisibility.

    Returns:
    bool: True if all integers are divisible by the divisor, False otherwise.
    """
    for num in numbers:
        if num % divisor != 0:
            return False
    return True

def any_divisible(numbers, divisor):
    """
    Check if any integer in the tuple is divisible by the divisor.

    Parameters:
    numbers (tuple or list): A tuple or list of integers.
    divisor (int): The divisor to check divisibility.

    Returns:
    bool: True if any integer is divisible by the divisor, False otherwise.
    """
    for num in numbers:
        if num % divisor == 0:
            return True
    return False

def difference(numbers):
    """
    Calculate the difference of integers in descending order.

    Parameters:
    numbers (tuple or list): A tuple or list of integers.

    Returns:
    int: The result of subtracting all integers in descending order.
    """
    sorted_numbers = sorted(numbers, reverse=True)
    result = sorted_numbers[0]
    for num in sorted_numbers[1:]:
        result -= num
    return result

# Example usage
if __name__ == "__main__":
    nums = (9, 12, 6, 8)
    print(all_divisible(nums, 3))  # Should return True
    print(any_divisible(nums, 4))  # Should return True
    nums = (7, 13, 6, 21)
    print(any_divisible(nums, 4))  # Should return False
    nums = (9, 12, 6, 8)
    print(difference(nums))        # Should return -11
