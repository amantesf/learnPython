'''Practice Problem: Write a function called exponent(base, exp) that returns an integer value of the base raised to the power of the exponent.

Exercise Purpose: Learn about “Accumulator Patterns.” Although Python has a built-in power operator (**), making your own version shows how repeated multiplication works and how functions return results to the main program.

Given Input: base = 2, exp = 5

Expected Output: 2 raises to the power of 5: 32
'''

def exponent(base, exp):
    return base ** exp

print(f'2 raise to the power of 5: {exponent(2,5)}')