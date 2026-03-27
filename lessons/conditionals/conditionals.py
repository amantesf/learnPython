name = 'Bob'
value = 'Very long name' if len(name) > 7 else 'short name'

print(value)

nums = range(1, 100, 2)

print(list(nums))

countries = ['Russia', 'China', 'Japan', 'Italy', 'Germany']
if 'Russia' in countries:
    print(countries.index('Russia'))

score = 78
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(grade)