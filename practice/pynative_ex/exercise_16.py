'''Practice Problem: Write a program to check if a given number is a palindrome (reads the same forwards and backwards).

Exercise Purpose: This exercise introduces the idea of “Reversing Logic.” Reversing a string is simple, but reversing an integer takes some math, like using division and modulo, or changing its type. This shows how data types can work differently.

Given Input:

Case 1: number = 121
Case 2: number = 125

Expected Output:

Number 125 is not palindrome number
Number 121 is palindrome number'''

number_one = 121
number_two = 125

str_number_one = str(number_one) #converts num to string
str_number_two = str(number_two)

if str_number_one == str_number_one[::-1]: #checks string to its reverse
    print(f'Number {number_one} is palindrome number')
else:
    print(f'Number {number_one} is not palindrome number')

if str_number_two == str_number_two[::-1]:
    print(f'Number {number_two} is palindrome number')
else:
    print(f'Number {number_two} is not palindrome number')

