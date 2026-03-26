'''Practice Problem: Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.

Exercise Purpose: This exercise teaches “State Tracking.” In programming, you often need to remember a value from a previous loop iteration to calculate results in the current one. This is the basis for algorithms like Fibonacci sequences or running totals.

Given Input: Range: numbers = range(10)

Expected Output:

Printing current and previous number sum in a range(10)
Current Number 0 Previous Number 0 Sum: 0
Current Number 1 Previous Number 0 Sum: 1
Current Number 2 Previous Number 1 Sum: 3
....
Current Number 8 Previous Number 7 Sum: 15
Current Number 9 Previous Number 8 Sum: 17
'''
#initialize previous and sum
previous_num = 0
sum = 0
print("Printing current and previous number sum in a range(10)")
#iterate for range(10) that adds the previous to the current
for current_num in range(10):
    sum = previous_num + current_num
    #print statement for the expected output
    print(f"Current Number {current_num} Previous Number {previous_num} Sum: {sum}")
    #updates the value of previous for each iteration to be the current
    previous_num = current_num