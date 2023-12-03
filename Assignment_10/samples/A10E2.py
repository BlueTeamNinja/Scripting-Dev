"""
A10E2.py: A Python module to remove multiple instances of a specified string from a list.

This script provides a function:
- remove_str_from_list(): Removes specified string instances from a list, 
  up to a maximum count, and returns the count of instances removed.
"""

def remove_str_from_list(lst, string_to_remove, max=1):
    """
    Remove multiple instances of a specified string from a list.

    Parameters:
    lst (list): The list from which the string will be removed.
    string_to_remove (str): The string to remove from the list.
    max (int, optional): The maximum instances to remove. Defaults to 1.

    Returns:
    int: The count of removed instances.
    """
    count = 0
    for _ in range(max):
        if string_to_remove in lst:
            lst.remove(string_to_remove)
            count += 1
        else:
            break
    return count

# Example usage
if __name__ == "__main__":
    my_list = ['apple', 'banana', 'apple', 'pear']
    print(remove_str_from_list(my_list, 'apple', max=2))  # Should return 2
    print(my_list)  # ['banana', 'pear']
    print(remove_str_from_list(my_list, 'apple'))  # Should return 0
    print(my_list)  # ['banana', 'pear']
