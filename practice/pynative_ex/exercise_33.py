'''Exercise 33. Character Replacer (Data Sanitization)
Practice Problem: Ask the user for a sentence. Replace every empty space in that sentence with an underscore (_) and print the final result.

Exercise Purpose: This exercise focuses on “String Sanitization.” In web development and file management, spaces are often problematic 

(especially in URLs or file paths). Learning to replace characters is a critical skill for preparing data for storage or transmission.

Given Input: "I love coding in Python"

Expected Output: I_love_coding_in_Python
'''
'''def char_replace(string):
    new_string = string.replace(' ', '_')
    print(new_string)
    return new_string

char_replace("I love coding in Python")'''


char_replace = lambda str: str.replace(' ', '_')

print(char_replace("I love coding in Python"))

