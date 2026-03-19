# self paramater
# 1. it is used to access properties and methos that belong to the class
# 2. it must be the 1st paramter of any method in the class
# 3. it links the method to the specific object.
# 4. self donot have to be named self 

# 1.
# accessing properties with self 
class Car:
    def __init__(self,name):
        self.name=name
    def display(self):
        return self.name

p1=Car("maruti")
print(p1.display())

# 2.
# calling methods with self (here i will use this instead of name self)

class Person:
    def __init__(this,name,age):
        this.name=name
        this.age=age
    def calculate_age(this):
        this.age+=10
        return this.age
    
    def display(this):
        this.age=this.calculate_age()
        print(f"age of {this.name} in next 10 years {this.age}")

p2=Person("akku",23)
p2.display()