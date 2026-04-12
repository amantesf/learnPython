'''Practice Problem: Write a program that takes two separate dictionaries and merges them into one single dictionary.

Exercise Purpose: This introduces “Key-Value Consolidation.” Merging dictionaries is a common task when combining configuration files or user profiles. It also teaches you about “Key Overwriting”—what happens when both dictionaries share the same key.

Given Input:

dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}
Expected Output:

{'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Engineer'}
'''
from pprint import pprint

dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}

merged_dict = dict1 | dict2 # '|' merges both dictionaries with the later dictionary prevailing if similar keys present
pprint(merged_dict)