# 1 
def greet(name):
    return 'hello',name

print(greet('akku'))

# 2
def greet(name):  # f-string is the best way to do this 
    return f"hello {name}"

print(greet('akku'))

# 3
def greet(name):
    return "hello " + name

print(greet('didi'))

# 4

def greet(name):
    return "hello {}".format(name)
print(greet('mummy'))

