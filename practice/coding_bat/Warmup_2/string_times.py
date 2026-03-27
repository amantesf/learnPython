'''Given a string and a non-negative int n, return a larger string that is n copies of the original string.


string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
'''


def string_times(str, n): 
    new_string = [] 
    for i in range(n): 
        new_string.append(str) 
    return ''.join(new_string)

print(string_times('Hi', 2))
print(string_times('Hi', 3))
print(string_times('Hi', 1))
