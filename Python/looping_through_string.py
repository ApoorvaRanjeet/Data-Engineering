print("hello 'apoorva'")
print("it's alright 'apoorva'")


# multiline 
a=""" lorem impsum dolor 
s doron doron main vekha tennu soneyo """
print(a)

a='''lorem ispum dolor sit amet , doron doron 
new vartanam'''
print(a)

# looping though s string 

sent="its a banana"
# for x in sent:
#     print(x)

print( "banana" in sent)

print("banana" not in sent)

b = "Hello, World!"
print(b[-5:-2])

print(b.upper())
print(b.lower())

# removes white space 
print(b.strip())

#replace string
print(b.replace('l','p'))
# we can use double quote as well istead of single quote

#split string 
print(b.split(","))

# String concatenation
a="hello"
b="world"
c=a+b
print(c)
# to add space 
c=a+" "+b
print(c)

# format strings 

i=1
# str="every month start with "+ i
# print(str)
# this will throw an error cant concatentae string with integer with + operator 

# using f string is the best way to that 
str=f"every month start with {i}"
print(str)

# another method 

str="every month starts with {}".format(i)
print(str)

str=f"every month start with {i*10}"
print(str)

str=f"every month start with {i:.2f}"
print(str)


# ESCAPE CHARACTERS 
txt="we are so called \"vinkings\" from the north."
print(txt)
txt="we are so called \'vinkings\'from the north."
print(txt)
txt="we are so called \\from the north"
print(txt)
txt="we are so called \nfrom the north"
print(txt)
txt="we are so called \tfrom the north"
print(txt)

#String methods 

# convert the first letter to capital letter 
a="apoorva"
print(a.capitalize())
print("HELLO".casefold())
print("apoorva".center(10))
print("apoorva".count('a'))
print("apoorva".encode())
print("apoorva".endswith('a'))
print("apoorva".find('o'))
print("apoorva".replace('o','O'))
print("apoorva".index('o'))
print("apoorva".isalnum())
print("apoorva".isalpha())
print("apoorva".isascii())
print("1.2".isdecimal())
print("1234".isdigit())
print("apoorva".islower())
print("12".isnumeric())
print("  ".isspace())
print("apoorva".isupper())
print("apoorva".rfind('a'))
print("apoorva".rindex('o'))
print("hello this is apoorva".swapcase())