'''
Syntax:
[expression for i in iterable if condition]

'''
language = 'Python'
lst = list(language) #prints string in a list of chars from the string
print(lst)

lst = [i for i in language] #iterates through string for each char without using for loop
print(lst)


numbers = [i for i in range(10)]
print(numbers)

numbers = [i ** 2 for i in range(10)] #multiplication iteration through list of nums
print(numbers)

numbers = [(i, i * i) for i in range(10)] #tuples
print(numbers)

even_numbers = [i for i in range(21) if i % 2 == 0] #even numbers
print(even_numbers)

odd_numbers = [i for i in range(21) if i % 2 != 0] #odd numbers
print(odd_numbers)

numbers = [-8, -8, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)

list_of_lists = [[1,2 ,3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)



