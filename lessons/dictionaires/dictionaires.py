
from pprint import pprint #import for pretty printing
first_name = 'Amanuel'
last_name = 'Tesfaye'
age = 18
country = 'U.S'

my_data = {'Amanuel', 'Tesfaye', '18', 'U.S'} #dictionairy {}
'''print(my_data)'''

spanish_to_english = { 
    'Hola':'Hello', #maps key to value
    'Buenos Dias': 'Good Morning',
    'Como estas': 'How are you',
    'Adios': 'Goodbye'

}

'''print(spanish_to_english)'''

person = {
    'first_name': 'Amanuel',
    'last_name': 'Tesfaye',
    'age': 18,
    'country': 'U.S',
    'skills': ['Python', 'Java', 'C++'],
    'address': { #nested dictionairy
        'city': 'Washington, D.C',
        'street_name': '37 O St NW',
        'zip': 20010
    }

}

pprint(person)
pprint(person['age'])
pprint(person['skills'])
pprint(person['address'])
person['nationality'] = 'Ethiopian'
pprint(person)
person['schools'] = ['CHEC', 'Georgetown']
pprint(person)
person['hobbies'] = ['Sports', 'Politics', 'Music', 'Gaming']
person['schools'].append('Takoma')
# person.pop('hobbies')
#del person['hobbies']

person_data_copied = person.copy()
pprint(person_data_copied)

if 'hobbies' in person:
    pprint(person)

print(len(person))

print(spanish_to_english.keys())
print(spanish_to_english.values())
print(spanish_to_english.items())

for item in spanish_to_english.items( ): #loops for each item to print the key + value
    print(item, item[0], item[1])


for key in person: 
    print(key, person[key]) 

'''spanish_to_english.clear()
print(spanish_to_english)'''

'''del spanish_to_english
print(spanish_to_english)'''