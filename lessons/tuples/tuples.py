print(())
print(type(()))
t = tuple()
print(t)
print(type(t))

years = (2020, 2021, 2023, 2023, 2023, 2025, 2026) #ordered, unchangeable (immutable), can be accessed by index
start_year = 2019
print(years[0])
print(years[-1])
print(3 in years)
print(2030 in years)
print(years.count(2023))
for year in years:
    print(year - start_year)

tp = (1, 2, 3, 4, 5)
tp2 = (6, 7, 8, 9, 10)
print(tp + tp2)

countries = ('Russia', 'Belgium', 'Croatia', 'France', 'Germany', 'Denmark')

first_countries = countries[3:]
print(first_countries)

print(list(countries))
del countries