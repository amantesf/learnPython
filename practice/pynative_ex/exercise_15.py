'''Practice Problem: Print the following pattern where each row contains a number repeated a specific number of times based on its value.
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
Exercise Purpose: Pattern printing is a classic way to learn “Nested Loops.” You coordinate an outer loop for rows and an inner loop for columns or repetitions. This improves spatial logic and control over output formatting.

Given Input: Range: 1 to 5

Expected Output: (The pattern shown above)'''
rows = 5 #num of rows in pattern
for i in range(rows+1): #outer loop
    for j in range(i): #nested loop
        print(i, end='') #display num per row
        #new line after each row
    print('')