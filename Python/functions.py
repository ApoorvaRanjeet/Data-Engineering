def hello_func():
    pass          #we can leave teh function completely empty, in case we want to fill this function later we wil use this pass keyword 

hello_func()

def sample_func():
    print("hello i started learning functions")

sample_func()

def sample_func1():
    return 'hello world'

print(sample_func1())
print(sample_func1().upper())

#passing an argument in a function

def sample_func2(greeting):
    return greeting

print(sample_func2("hello"))

def sample_func2(greeting,name='apoorva'):
    return '{},{}'.format(greeting,name)

print(sample_func2("hello"))  # here if we didnt pass the second argument it wont throw an error

def sample_func2(greeting,name='apoorva'):
    return '{},{}'.format(greeting,name)

print(sample_func2("hello","aadrika"))

