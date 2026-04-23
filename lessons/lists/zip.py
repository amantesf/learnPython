from pprint import pprint
fruits = ['apple', 'banana', 'kiwi', 'lemon', 'watermelon']
vegetables = ['cabbage', 'lettuce', 'broccoli', 'carrot', 'squatch']
fruits_and_vegetables = []

for f, v in zip(fruits, vegetables): 
    fruits_and_vegetables.append({'fruit': {f}, 'vegetable': {v}}) #aggregates a fruit with a vegetable into an dictionary

pprint(fruits_and_vegetables)

countries = ['US', 'China', 'UK', 'Russia', 'Japan']
debt = [30, 4, 1, 10, 1]
profile = []
for c, d in zip(countries, debt):
    profile.append({'country': {c}, 'debt': {d}})

pprint(profile)
