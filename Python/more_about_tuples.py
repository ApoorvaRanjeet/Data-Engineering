# 1. tuples are immutable - they cant be changes meaning we can add or remove elements from tuple once they are created 
# 2. they are ordered 
# 3. they allow duplicates
# 4. tuples items can be of any data type and can contain different data types like list
# 5. just like lists tuples are also indexed , items are indexed from 0 here 

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

print(len(thistuple))

# to create tuple with one item you have to remember to add the comma otherwise python wont remember it as tuple 
single_tuple=("apple",)
print(single_tuple)
print(type(single_tuple))

single_tuple=("apple")
print(single_tuple)
print(type(single_tuple))

tuple_2=(1,False)
print(tuple_2)

# we can use tuple() constructor to make a tuple
tuple_3=tuple((1,2,3))
print(tuple_3)

tuple_3=tuple(tuple_2)
print(tuple_3)


# to access the tuples items
print(thistuple[0])
print(thistuple[-1])
print(thistuple[1:3])
print(thistuple[-3:-1])
print(thistuple[:4])
print(thistuple[2:])

# check if item exists in tuple
print("apple" in thistuple)

for i in thistuple:
    if "cherry" in i:
        print("yes")
        break
    
# we cannot really change the tuple so inorder to change it 
# we can change the tuple into list and then after all the updation we can change it back to tuple

list_1=list(thistuple)
list_1.append("kiwi")
thistuple=tuple(list_1)
print(thistuple)

# we can use the same workaround to remove the items from tuple like we did above


# to add tuple to a tuple

y=()
y+=thistuple
print(y)

# del keyword will delte the whole tuple

del y
print(y)

#unpacking a tuple
fruits = ("apple", "banana", "cherry") # this is called packing a tuple

a,b,c=fruits # this is called unpacking a tuple
print(a)
print(b)
print(c)

# 2. using astrisk
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
a,b,*c=fruits
print(a)
print(b)
print(c)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
a,b,*c=fruits
print(a)
print(b)
print(c)

# loop through tuple
# 1.
for i in fruits:
    print(i)

# 2.
for i in range(len(fruits)):
    print(fruits[i])

# 3.
i=0
while(i<len(fruits)):
    print(fruits[i])
    i+=1
    

#just trying something
tuple_2=fruits[:]
print(tuple_2)

# join tuples
# 1.
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# 2.

tuple_4=fruits*2
print(tuple_4)


# tuple methods
# 1. count()
print(tuple_4.count('apple'))
# 2. index()
print(tuple_4.index('cherry'))
