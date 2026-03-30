'''Practice Problem: Write a program to extract each digit from an integer in the reverse order.

Exercise Purpose: This exercise explores “Mathematical Parsing.” Instead of converting a number to a string, use the modulo operator (%) and floor division (//) to isolate digits. This is common in low-level programming and algorithm challenges where type conversion is restricted.

Given Input: number = 7536

Expected Output: 6 3 5 7'''

number = 7536
reversed_num = 0 #sets reverse num to initial
negative = number < 0 #checker for num being pos/neg

while number != 0: #loops till number is reduced to 0
    reversed_num = reversed_num * 10 + number % 10 #multiplies the last digit to be higher then adds the remainder of the num given divided by 10
    number //= 10 #reduces to the right side

if negative:
    reversed_num = -reversed_num #checks if reversed num is negative

print(reversed_num) #prints result

