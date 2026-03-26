shopping_list = ['bread', 'coffee', 'milk', 'eggs', 'cereal', 'rice']
print(shopping_list)
print(len(shopping_list))

nums = [1, 2, 3, 4, 5, 6]
people = ['James', 'Curry', 'Durant', 'Nash', 'Antetokounmpo']
countries = ['Ethiopia', 'USA', 'Eritrea', 'Kenya', 'Russia']
ex = [0, 1, True, 'Cash', ['Bill', 'Frank']]
print(ex)

print(nums[0])
last_index = len(nums) - 1
print(nums[last_index])
print(nums[-1])
print(nums[-2])
print(nums[-3])
print(nums[-4])

#slicing
print(nums[0:3])
print(nums[2:5])
print(nums[2:last_index])
print(nums[::-1])
print(nums[::-2])
print(nums[:3])
print(nums[-3:-1])

#modifying

nums[0] = 7

#remove
nums.pop(2)

nums.insert(1, 22)
print(nums)

print('Russia' in countries)
print('2' in [3, 4, 5, 6])

shopping_list.append('Meat')
print(shopping_list)

#removing
shopping_list.remove('Meat')
print(shopping_list)


fruits = ['mango', 'banana', 'kiwi', 'apple', 'coconut']
del fruits[0]
print(fruits)
fruits.clear()
print(fruits)

positive_nums = [1, 2, 3, 4, 5]
zero = [0]
negative_nums = [-1, -2, -3, -4, -5]
integers = negative_nums[::-1] + zero + positive_nums
print(integers)

ages = [22, 19, 23, 24, 24, 25, 26]
print(ages.count(19))
print(ages.count(24))
print(ages.index(22))
print(ages[::-1]) #ages.remove() mutates (not ideal)
print(ages)

'''ages.sort()
print(ages)'''

sorted_age = sorted(ages) #sorted(ages, reverse=True) (sorts and reverses)
print(sorted_age)
