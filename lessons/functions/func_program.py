#map, filter, reduce
# Map:
# ['Finland', 'Germany', 'France', 'Poland', 'Kosovo', 'Portugal'] -> ['FINLAND', 'GERMANY', 'FRANCE', 'POLAND', 'KOSOVO', 'PORTUGAL']

print([c.upper() for c in ['Finland', 'Germany', 'France', 'Poland', 'Kosovo', 'Portugal']])
 
 #Filter:
 #[1, 2, 3, 4] -> [2, 4] filter out odd
 #[1, 2, 3, 4] -> [1, 3] filter out even

 #Reduce
 #[1, 2, 3, 4] -> 10 Adding up all the items to reduce to one item 10
 #[1, 2, 3, 4] -> 24 Multiplying all the items to reduce to one item 24
 
'''nums = [1, 2, 3, 4]
new_lst = []
for num in nums:
    new_lst.append(num * 2)

print(new_lst)'''
nums = [1, 2, 3, 4]
new_list = list(map(lambda x: x**2, nums)) #maps each num in nums to take the square of and saves in new_list

print(new_list)
 
countries = ['Finland', 'Germany', 'Iceland', 'Poland', 'France', 'Portugal', 'Spain']
new_c_list = list(map(lambda country: country.upper(), countries))
print(new_c_list)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = list(filter(lambda x: x%2 == 0, numbers))
odds = list(filter(lambda x: x%2 != 0, numbers)) 
print(evens)
print(odds)   

countries_end_land = list(filter(lambda country: 'land' in country, countries))
print(countries_end_land)

from functools import reduce

nums = [1, 2, 3, 4, 5]

print(reduce(lambda x, y: x + y, nums))
print(reduce(lambda x, y: x * y, nums))
 