'''Practice Problem: Iterate through a given list of numbers and print only those numbers which are divisible by 5.

Exercise Purpose: This exercise teaches the use of the modulo operator (%) and loop filtering. In data processing, you often need to sift through large datasets to extract subsets that meet mathematical criteria.

Given Input: num_list = [10, 20, 33, 46, 55]
Expected Output:

Divisible by 5:
10, 20, 55
'''
print('Divisible by 5:')

num_list = [10, 20, 33, 46, 55]
for i in num_list:
    if i % 5 == 0: #modulo operator checks divisibility by 5
        print(i)
