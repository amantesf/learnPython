'''Practice Problem: Write a program to find all prime numbers up to 20, but only print every second (alternate) prime number found.

Exercise Purpose: This exercise combines “Nested Loops” (to check for primality) with “Step Logic.” It requires the programmer to first identify a subset of data and then apply a secondary filter, a common task in data reporting.

Given Input: Limit = 20

Expected Output: 2, 5, 11, 17
'''

primes = []

for num in range(2, 21):
    for i in range(2, int(num//2) + 1):
        if num % i == 0:
            break
    else:
        primes.append(num)

alternate_primes = primes[::2]
print(alternate_primes)