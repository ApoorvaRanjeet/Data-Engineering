a='apoorva'
print(a)
print(a[0:5])
print(a[:5]) # is same as above
print(a[5:])# from 5th character

print (a.lower())
print(a.upper())

print(a.count('apoorva'))
print(a.count('a'))

print(a.find('r'))
print(a.find('ranjeet'))


a=a.replace('apoorva','ranjeet')
print(a)


greeting ='hello'
b='world'

c=greeting + ' '+b
print(c)


#fstrings 

d=f'{greeting} {b}. morning!'
#d=f'{greeting} {b.upper()}. morning!'
print(d)


print(dir(d))  # what are the functions available 
print(help(str))