'''Practice Problem: Write a program to print the first 15 terms of the Fibonacci series. 
The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.

Exercise Purpose: The Fibonacci sequence is a classic way to learn about state management in loops. 
You keep track of two changing variables at once to find the next number, which helps you see how data moves through each step.

Given Input: Terms = 15

Expected Output: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

'''
def fibonacci_sequence(terms):
    num_one = 0
    num_two = 1
    for i in range(15):
        print(num_one, end=' ')
        next_num = num_one + num_two
        num_one = num_two
        num_two = next_num

fibonacci_sequence(15)
    
