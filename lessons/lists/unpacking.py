def sum_of_five_nums(a, b , c, d, e):
    return a + b + c + d + e
lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))


numbers = range(2, 7)
print(list(numbers))


args = [2,7]
numbers = range(*args) #unpacks arguments from list
print(list(numbers))

countries = ['US', 'Russia', 'China', 'Japan', 'Denmark']
us, rus, chi, *rest = countries #unpacks 'US', 'Russia', 'China' individually then the rest increments

print(us, rus, chi, rest)
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers 
print(one, middle, last)

def unpacking_person_info(name, city, state, age):
    return f'{name} lives in {city}, {state}. He is {age} years old.'

dct = {
    'name': 'Amanuel',
    'city': 'Washington',
    'state': 'D.C',
    'age': 18
}
print(unpacking_person_info(**dct)) # using double (**) since it is a dict not tuple/list