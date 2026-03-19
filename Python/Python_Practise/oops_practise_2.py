class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def bark(self):
        print(self.name+" says Woof!")

d1=Dog("Buddy",3)
d1.bark()
# if i will print(d1.bark()) it will result in buddy says woof! and None coz my method doesnt return anything it only prints
print(d1.bark())