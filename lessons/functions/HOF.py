#functions that returns other function/function that passes an function as parameter

def make_square(n):
    return n**2

def make_cube(func, n):
    return func(n) * n

print(make_square(2) * 2)

print(make_cube(make_square, 2))
print(make_cube(make_square, 3))
print(make_cube(make_square, 4))

def do_some_math(n):
    def add_ten():
        return n + 10
    return add_ten

print(do_some_math(5)())
print(do_some_math(120)())