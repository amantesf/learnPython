def make_square(n):
    square = n ** 2
    return square

print(make_square(2))
print(make_square(3))
print(make_square(4))
print(make_square(5))

def add_two_nums(a, b):
    sum = a + b
    return sum

print(add_two_nums(10,29))
print(add_two_nums(13,26))
print(add_two_nums(5,20))
print(add_two_nums(15,3))
print(add_two_nums(7,12))
print(add_two_nums(6,13))


def print_full_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name

print(print_full_name('Amanuel', 'Tesfaye'))
print(print_full_name('Cristiano', 'Ronaldo'))
print(print_full_name('Ousmane', 'Dembele'))


def calculate_weight(mass = 50, gravity = 9.81):
    return round(mass * gravity, 1)
print(calculate_weight())
print(calculate_weight(75))
print(calculate_weight(75, 10.2))

def check_number(a):
    if a % 2 == 0:
        return 'even'
    else:
        return 'odd'
    
print(check_number(10))
print(check_number(7))
print(check_number(25))
print(check_number(68))

def add_nums(*args): #*args turns the function into a tuple/ helps if we dont know the num of arguments to pass to function (arbitruary # of args) 
    total = 0
    for i in args:
        total += i
    return total

print(add_nums(1, 2, 3, 4, 5))


def create_groups(team, *args):
    print(team)
    for member in args:
        print(member)

create_groups('Team One', 'Jake', 'Paul', 'Logan', 'Macaster')