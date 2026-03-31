'''Exercise 20. Nested Loops for Multiplication Tables
Practice Problem: Print a multiplication table from 1 to 10 in a formatted grid.

Exercise Purpose: To master “Matrix Generation.” 
This builds on the nested loop concepts from Exercise 8 and applies them to generate a structured data table. 
This is essential for understanding how to populate 2D arrays or generate spreadsheets.

Given Input: Range: 1 to 10

Expected Output:

1  2  3  4  5  6  7  8  9  10 		
2  4  6  8  10 12 14 16 18 20 		
... (up to 10)
'''
for i in range(1, 11): #iterates from 1 to 10 for rows
    for num in range(1, 11): #iterates from 1 to 10 for columns
        print(i * num, end="\t") #ends the print with tab instead of newline
    print("\n") #after each iteration newline
