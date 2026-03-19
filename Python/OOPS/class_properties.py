# everything about class

# 1. class -> blueprint/template :
            # it defines attributes(data),methods
# 2. object -> is an instance of the class : basically the actual entity that holds data and can use methods defined in class
# toh we dont ue data to access the properties of the class it actually conatins data and behaviour

# 3. attributes/properties -> variables inside classlike self.name
# 4. functions -> methods defined withing the class
# 5. features of the class -> attributes+methods


# 1. access properties : using dot notation

class Car:
    def __init__(self,name):
        self.name=name

c1=Car("Ford")
print(c1.name)


# 2. modify properties 

class Car:
    def __init__(self,name):
        self.name=name

c1=Car("Ford")
print(c1.name)

c1.name="Maruti"
print(c1.name)

# 3. delete properties 

del c1.name
# print(c1.name)

# 4. class property vs object/instance property

class Person:
    species="lizard"  # class property
    def __init__(self,name,age):
        self.name=name # instance property
        self.age=age
    
p1=Person("akku",23)
p2=Person("sonu",22)

print(p1.name)
print(p2.name)
print(p1.species)

# 5. modifying class property

Person.species="snake"
print(p1.species)
print(p2.species)

p1.species="lion"
print(p1.species)

print(p2.species)

# 6. adding properties to an object

p1.city="bishrampur"

print(p1.city)

print(p2.city)  # this will throw an error coz adding properties to an object using the baove method will only add property to the specific object not to all objects of the class 
