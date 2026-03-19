# polymorphism : we can have mulitple classes with the same method/functions/operators name. often used in class methods
# len() is the example of polymorphism

class Car:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"the name of car is {self.name}")

class Boat:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"the name of boat is {self.name}")
        
a=Car("ford")
b=Boat("cargo")

for x in (a,b):
    x.display()


# we can use polymorphism in inheritance by using the same parent class for all the child classes 

class Vehicle:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
        
class Car(Vehicle):
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"the name of car is {self.name}")

class Boat(Vehicle):
    # def __init__(self,name):
    #     self.name=name
    # def display(self):
    #     print(f"the name of boat is {self.name}")
    pass

x=Vehicle("parent")
y=Car("ford")
z=Boat("child")

x.display()
y.display()
z.display()


# just trying another example 
class Car:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)

class Bike(Car):
    pass

class Boat(Car):
    def __init__(self, name,price):
        super().__init__(name)
        self.price=price
    def display(self,rating):
        self.rating=rating
        print(f"the price of {self.name} is {self.price} and rating is {self.rating}")
        
a=Car("nano")
b=Bike("maruti")
c=Boat("cargo",1000)

a.display()
b.display()
c.display(100)