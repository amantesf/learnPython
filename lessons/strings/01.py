letters = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
print(letters)
print(len(letters))
print(len(vowels))
print(len(consonants))
print(letters.upper())
print(vowels.upper())
print(consonants.upper())

challenge = '30 Days Of Python'
print(challenge.upper())
print(challenge.title())
print(challenge.swapcase())
print(challenge.find('0'))
print(challenge.find('y'))
print(challenge.find('f'))

language = 'python'
print(language.upper())
print(len(language))
print(language[0:2])
print(language[2:])
print(language[-2:])
print(language[::-1])
print(language.title())
print(language.swapcase())
print(language.isupper())
print(language.islower())
print(language.count('o'))
city = '  mississippi   '
print(city.count('i'))
print(city.count('s'))
print(city.count('p'))
print(city.find('p'))
print(city.rfind('p'))
print(city)
print(city.strip())
print(city.rstrip())
print(list(city))
print(city.index('m'))

country = 'Finland'
print(country.startswith('Fin'))
print(country.startswith('fin'))
print(country.endswith('land'))

skills = ['HTML', 'CSS','JS', 'Python']
print('/'.join(skills))


print('abac'.isalpha())
print('abac1233'.isalpha())
print('abac1233'.isalnum())
print('1233'.isdecimal())
print('1233'.isnumeric())
print('1233'.isdigit())

sentence = 'I like coding.'
print(sentence.replace('like', 'hate'))

a = 6
b = 7
print('%d + %d = %d' %(a, b, a + b))
print(f'{a} + {b} = {a+b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} % {b} = {a%b}')
print(f'{a} ** {b} = {a**b}')
