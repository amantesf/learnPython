'''Practice Problem: Display only those characters which are present at an even index number in given string.

Exercise Purpose: Understand how data is stored in memory using zero-based indexing. In most languages, the first character is at position 0, the second at 1, and so on. Mastering indexing is vital for data parsing.

Given Input: String: "pynative"

Expected Output:

Original String is  pynative
Printing only even index chars
p
n
t
v
'''
original_string = "pynative"
print("Original String is", original_string)
print("Printing only even index chars")
for index, char in enumerate(original_string):
    if index % 2 == 0:
        print(char)