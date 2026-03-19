#   inheritance : 

# allowed us to create a class that inherits  all the properties and methods form another class 

# 1.
# creating parent class
class Parent:
    def __init__(self,city,country):
        self.city=city
        self.country=country
    
    def display(self):
        print(f"here are the city and country this family belongs to {self.city} , {self.country}")
        
# create a child class

# to inherit from the another class : create a class and add anothers class name in its parameter
class Child(Parent):
    pass # use pass keyword when i dont want to add any other properties or methods to the class.

# x=Child("bishrampur","Chhattisgarh")
# x.display()



# 2.
# add the init function : instead of using pass keyword what happens when we add init method 

class Child(Parent):
    def __init__(self,city,country):
        self.city=city+" near amobikapur"
        self.country=country+" was the best country in the world"


x=Child("bishrampur","India")
x.display()  
    
#  when we add the init function inside the child class it will no oonger inherit the parent's inherit method
# inorder to use the parent's inherit method but without using pass keyword we can do it like this :

class Child(Parent):
    def __init__(self, city, country):
        Parent.__init__(self,city,country)
        
x=Child("bishrampur","India")
x.display()  




# 3. super()  : this makes the child class inherit all the methods properties from its parent.
# we dont have to ue the Parent name
class Child(Parent):
    def __init__(self, city, country):
        super().__init__(city, country)



# 4. add properties 
class Child(Parent):
    def __init__(self, city, country):
        super().__init__(city, country)
        self.name="Apoorva"

    def about_child(self):
        print(f"coming from {self.city}, {self.country} and the name is {self.name}")

x=Child("bishrampur","india")
x.about_child()
x.display()

class Child(Parent):
    def __init__(self,city,country,name):
        super().__init__(city,country)
        self.name=name

x=Child("bishrampur","india","Anusha")
x.display()



# add methods : if  we add method in the child class with same name as that of parent class then the parent class method will be overridden

class Child(Parent):
    def __init__(self,city,country,name):
        super().__init__(city,country)
        self.name=name
    def display(self):
        print(f"{self.name}, {self.city}, {self.country}")
    
x=Child("delhi","India","Kirti")
x.display()