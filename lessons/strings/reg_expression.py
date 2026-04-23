import re
'''
Syntax:
re.match(substring, string, re.I) 
'''

txt = 'I code in Python'
match = re.match('I code in', txt, re.I)

print(match) #returns only if the code starts with 'I code in'

span = match.span() #returns the start, end pos of the match as tuple

print(span)

start, end = span
print(start, end)
substring = txt[start:end]
print(substring)

'''
Syntax:
re.search(substring, string, re.I)
'''

txt = '''Python is a very easy to learn programming language.
         To learn python all you need is commitment and an open mind.
         However, C++ is not so easy to learn for a programming language.
        '''

match = re.search('language', txt, re.I)

print(match)

span = match.span()

print(span)

start, end = span

substring = txt[start:end]
print(substring)


matches = re.findall('language', txt, re.I)
print(matches)

matches = re.findall('Python|python', txt, re.I) # can also do re.findall('[Pp]ython, txt)
print(matches)

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I) #same here ^
print(match_replaced)

''' txt = %I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?

matches = re.sub('%', '', txt)
print(matches)'''

print(re.split('\n', txt))
