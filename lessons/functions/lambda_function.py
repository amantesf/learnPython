'''def name_of_function():
    print('I am a function')

name_of_function()
'''


'''
def quadratic_equation(x):
    return x**2'''

quadratic_equation = lambda x,y,z: x**2 + 2*y + z

print(quadratic_equation(2, 3, 4))
print(quadratic_equation(10, 2, 3))