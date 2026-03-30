'''Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''
def string_splosion(str):
  new_str = ''
  for i in range(len(str)):
    new_str += str[:i+1]
  print(new_str)
  return new_str

      

string_splosion('Code')
string_splosion('abc')
string_splosion('ab')