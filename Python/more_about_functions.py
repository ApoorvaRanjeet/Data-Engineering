# parameter vs argument

def sample_func(name):  # here name is parameter
    return name

myname=(sample_func("akku"))  # here akku is argument 
print(myname)
print(sample_func("sonu")) 

# default parameter values

def sample_func2(name="chinu"):
    return name

print(sample_func2("mummy"))
print(sample_func2())  # this is calling default parameter as no argument was passed


def num_only():
    return (10,20)

a,b=num_only()
print(a)
print(b)


# if we dont know how many arguments will be passed into your function , add a * before the parameter name
def my_func(*name):
    return(name)

print(my_func("akku","sonu","chinu"))

# *args :->this parameter allows function to accept any number of poitional arguments
# this *args become the tuple containing all the passed arguments

def my_func2(*args):
    return args
print(my_func2(1,2,3,4))

def my_func3(*numbers):
    for i  in numbers:
        print(i)

my_func3(1,7,5,4)

# *kwargs :->this parameter allows function to accept any number of keyword arguments

def my_func4(**myvar):
    print("name ",myvar["name"])
    print("age ",myvar["age"])
    print("all data ",myvar)

my_func4(name="apoorva",age=23)