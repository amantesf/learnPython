list_one = [1, 2, 3]
list_two = [4, 5, 6, 7]
lst = [0, *list_one, *list_two] #upacks both lists to combine into one
print(lst)
country_list_one = ['US', 'China', 'Russia']
country_list_two = ['Japan', 'Germany', 'UK']
power_countries = [*country_list_one, *country_list_two] #upacks both lists to combine into one
print(power_countries)