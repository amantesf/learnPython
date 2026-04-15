'''Exercise 32. Dictionary of Squares (Mapping Logic)
Practice Problem: Create a dictionary where the keys are numbers from 1 to 10 and the values are the squares of those numbers (e.g., 2: 4, 3: 9).

Exercise Purpose: This exercise explores “Data Mapping.” It demonstrates how dictionaries can be used to store pre-calculated mathematical relationships, essentially acting as a “lookup table” that can replace expensive repetitive calculations.

Given Input: Range: 1 to 10

Expected Output:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
'''
from pprint import pprint

nums = {

}

for i in range(1, 11):
    nums[i] = i **2

pprint(nums)