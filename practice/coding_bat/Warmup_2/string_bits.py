'''Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
'''

def string_bits(str):
  new_str = ''
  for i in range(len(str)):
    if i % 2 == 0:
      new_str += str[i]
  print(new_str)
  return new_str

string_bits('Hello')
string_bits('Hi')
string_bits('Heeololeo')