'''Given a string, return a string where for every char in the original, there are two chars.


double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
'''
def double_char(str):
  new_string = ''
  for i, char in enumerate(str):
    new_string += 2 * str[i]
  print(new_string)
  return new_string

double_char('The')
double_char('AAbb')
double_char('Hi-There')