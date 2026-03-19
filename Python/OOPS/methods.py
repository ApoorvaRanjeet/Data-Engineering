# methods accesing properties

class Car:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)

p1=Car("ford")
p1.display()

# methods modifying properties
class Car:
    def __init__(self,name):
        self.name=name
    def modify(self):
        self.name="hemlp"
    def display(self):
        print(self.name)

p1=Car("ford")
p1.modify()
p1.display()

# __str__() method
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("a",1)
print(p1)

# with __str__ method

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} {self.age}"
p1=Person("a",1)
print(p1)


# delete methods 

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} {self.age}"
    def greet(self):
        print(f"hello {self.name}")
        

p1=Person("a",1)
p1.greet()
del Person.greet

p1.greet()