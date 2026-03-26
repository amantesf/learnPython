'''Practice Problem: Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.

Exercise Purpose: This exercise introduces “Collection Indexing” and “Boolean Flags.” Comparing data structure boundaries is common in pattern matching and data integrity checks.

Given Input:

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
Expected Output:

Given list: [75, 65, 35, 75, 30] | result is False
Given list: [10, 20, 30, 40, 10] | result is True
'''

def same_elements(given_list):
    same = False #boolean initialize
    if given_list[len(given_list)-1] == given_list[0]: #last element same as first
        same = True #set True
        print(f'Given list: {given_list} | result is {same}')
    else: 
        print(f'Given list: {given_list} | result is {same}') #keep False

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

same_elements(numbers_x)
same_elements(numbers_y)
