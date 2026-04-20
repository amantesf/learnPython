'''
    syntax:
    try:
        code in this block if things go well
    except:
        code in this block run if things go wrong
'''

try:
    print(10 + '5') #'5' is a string cannot add to an int
except:
    print('Something wrong') # instead this prints out


try:
    name = input('What is your name: ')
    year_born = input('What year were you born: ')
    age = 2019 - year_born
    print(f'You are {name} and you are {age} years old.')
except:
    print('Something is wrong.')



try:
    name = input('What is your name: ')
    year_born = input('What year were you born: ')
    age = 2019 - year_born
    print(f'You are {name} and you are {age} years old.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('Zero Division error occured')
else:
    print('I usually run with the try block')
finally:
    print('I always run')


try:
    name = input('What is your name: ')
    year_born = input('What year were you born: ')
    age = 2019 - year_born
    print(f'You are {name} and you are {age} years old.')
except Exception as e:
    print(e)