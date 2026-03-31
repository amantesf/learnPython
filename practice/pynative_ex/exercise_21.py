'''Exercise 21. Downward Half-Pyramid Pattern
Practice Problem: Print a downward half-pyramid pattern using stars (*).

Exercise Purpose: Learn about reverse indexing. Controlling loop boundaries in reverse is important for algorithms that process data from end to beginning.

Given Input: Rows: 5

Expected Output:

* * * * * 
* * * * 
* * * 
* * 
* '''

def pyramid_pattern(rows):
    for i in range(rows, 0, -1):
        for j in range(1, i+1):
            print('*', end=' ')
        print('\n')



pyramid_pattern(5)
#pyramid_pattern(10)