'''Practice Problem: Calculate income tax for a given income based on these rules:

First $10,000: 0% tax
Next $10,000: 10% tax
Remaining income: 20% tax
Exercise Purpose: This exercise introduces “Tax Brackets” logic, a classic example of complex conditional branching. It shows how to calculate values cumulatively instead of applying a single percentage to the entire amount.

Given Input: income = 45000

Expected Output: Total income tax to pay is 6000
'''

income = 45000
income_tax = 0
if income <= 10000:
    income_tax = 0
elif income <= 20000:
    income_tax = (income - 10000) * 10 / 100 #next 10,000 tax 10%
else:
    income_tax = 0 + (10000 * 10 / 100) 
    income_tax += (income - 20000) * 20 / 100 #remaining income

print(f'Total income tax to pay is {income_tax}')




