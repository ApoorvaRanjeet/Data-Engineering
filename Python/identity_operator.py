x=10
y=10

print(x is y)
print(x is not y)

print(x==y)

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

# x=10 and y=10 ke case mein x is y true aaya 
# but x = [1, 2, 3] y = [1, 2, 3] ke case mein false 
# python reuses small integers like 10 internally to save memory this is called integer caching/interning
# so python stores 10 once in memory and both variables point to it.
# in case of list they are mutable objects so python creates two different objects, even they ook same they are different objects 

# if 
x=[1,2,3]
y=x
print(x is y)

# then in this case the output will be true coz bith are pointing to the same memory object 

x=1000
y=1000

print(x is y)