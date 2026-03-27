countries = ['Russia', 'China', 'Japan', 'Canada', 'Germany', 'Finland', 'Thailand', 'Greenland']
list_of_list = []
for country in countries:
    list_of_list.append([country, country.upper(), country.upper()[::-1]])
print(list_of_list)

nums = [1, 2, 3, 4, 5, 6, 7]
for num in nums:
    print(num)

for i in range(0, 101, 10):
    print(i)



countries_with_land = []
for country in countries:
    if 'land' in country:
        countries_with_land.append(country)
print(countries_with_land)


countries_without_land = []
for country in countries:
    if 'land' not in country:
        countries_without_land.append(country)
print(countries_without_land)


nums = [1, 2, 3, -4, 5, 6, -7]
for num in nums:
    if num < 0:
        continue
    print(num)

nums = [1, -2, 3, -4, 5, 6, -7]
for num in nums:
    if num < 0:
        break
    print(num)

data = [[0, 1, 2, 'Finland'], [3, 5, 'Norway', 'China'], ['US', -5, 3], ['Russia', 'Australia', 9, 11]]
numer = []
for list in data:
    for item in list:
        print(item)