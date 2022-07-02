import math

result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)
#print(help(math))

print('Hi', 'Mike', sep=',', end='\n')

print('Hi', 'Mike', sep=',', end='.\n')

print('hello')
print('I don\'t know')
print('say "I don\'t know"')

print('hello. \nHow are you?')

print('C:\name\name')
print(r'C:\nam\name')

print("##########")
print("""\
line1
line2
line3\
""")
print("##########")

print("Hi" * 3)

word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print('###########')
print(word[0:2])
print(word[:2])
print('###########')
print(word[2:])
print(word[2:5])

print('###########')
word = 'j' + word[1:]
print(word[:])

n = len(word)
print(n)

s = 'My name is Bob'
print(s)
is_start = s.startswith('My')
print(is_start)
print('###########')
print(s.find('Bob'))
print(s.rfind('Bob'))
print(s.count('Bob'))
print(s.capitalize())
print(s.title())
print(s.upper())


