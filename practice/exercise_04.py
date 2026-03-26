'''Practice Problem: Write a function to remove characters from a string starting from index 0 up to n and return a new string.

Exercise Purpose: This exercise demonstrates how to truncate data strings, a common data-cleaning task.

Given Input:

remove_chars("pynative", 4)
remove_chars("pynative", 2)
Expected Output:

tive
native
'''

def remove_chars(original_string, x):
    length = x - len(original_string)
    print(original_string[length:])
    return -1

remove_chars("pynative", 4)
remove_chars("pynative", 2)
