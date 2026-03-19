# __init__  method in python is just like constructor in java 
# it is used to initialize the attributes 
# init method is called when the class is being initiated , when the object of the class is being created 

# 1.
class Person:
    def __init__(self,name,age):  # init method creation (parametrized constructor)
        self.name=name   
        self.age=age

p1=Person("apoorva",23)  #  object creation
print(p1.name)
print(p1.age)
   

# 2.     
        
# default init method by python is 
# def __init__(self):
#     pass               it does nothing just allow object creation


# 3.
# class withoit init method

class Person2:
    pass

p2=Person2()
p2.name="Tobi"
p2.age=23

print(p2.name)
print(p2.age)

# so basically the init method makes it easier to create object with initial values

# 4.
# default values in init method

class Person3:
    def __init__(self,name,age=23):
        self.name=name
        self.age=age

p3=Person3("akku")

print(p3.name)
print(p3.age)  # in this case the object used the default value of age as actual values werent passed

p4=Person3("akku",24)
print(p4.name,p4.age)

# 5. multiple parameters

class Person5:
    def __init__(self,name,age,place,country):
        self.name=name
        self.age=age
        self.place=place
        self.country=country

p5=Person5("a",21,"bishrampur","India")

print(p5.name,p5.age,p5.place,p5.country)


