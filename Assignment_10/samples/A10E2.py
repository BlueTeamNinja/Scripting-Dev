def remove_str_from_list(list_of_str, str_to_remove, case_sensitive=True, max=1):
    """
    Remove multiple instances of a specified string from a list.

    Parameters:
    list_of_str (list): The list from which the string will be removed.
    str_to_remove (str): The string to remove from the list.
    case_sensitive (bool, optional): Whether the match should be case sensitive.
    max (int, optional): The maximum instances to remove. Defaults to 1.

    Returns:
    int: The count of removed instances.
    """
    count = 0
    if case_sensitive:
        while str_to_remove in list_of_str and count < max:
            list_of_str.remove(str_to_remove)
            count += 1
    else:
        str_to_remove_lower = str_to_remove.lower()
        i = 0
        while i < len(list_of_str) and count < max:
            if list_of_str[i].lower() == str_to_remove_lower:
                list_of_str.pop(i)
                count += 1
                continue  # Skip incrementing i as the list size has reduced
            i += 1 
    return count

# Example usage
if __name__ == "__main__":
     print(remove_str_from_list(['apple', 'banana', 'apple', 'pear'], 'apple', max=2))

