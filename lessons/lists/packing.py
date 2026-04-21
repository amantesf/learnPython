def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3)) #prints 6 (1 + 2+ 3)
print(sum_all(1, 2, 3, 4, 5, 6, 7)) #prints 28 1 + 2 + 3 ..

def packing_person_info(**kwargs):
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')
    return kwargs

print(packing_person_info(name = 'Amanuel', country = 'US', city = 'Washington, D.C', age = 18))



