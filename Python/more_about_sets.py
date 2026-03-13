# 1. unordered , unchangeable , and unindexed
# 2. unchangeable but can remove and add new items in it
# 3. do not allow duplicates
# 4. cannot be referred to by index or key coz they are unordered
# 5. true and 1 are considered as same value in set and are treated as duplicates
# 6. false and 0 are considered as same value in set and are treated as duplicates
# 7. set items can be of any data types

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset={"apple", "banana", "cherry","cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# to get the length of the set 
print(len(thisset))

set1={"1",1,False,1.3}
print(set1)

# to create a set using set constructor
set2=set(set1)
print(set2)

set2=set(("a","b"))
print(set2)

# access items in set 
for x in thisset:
    print(x)
    
print("apple" in thisset)

thisset = {"apple", "banana", "cherry"}
[print(x) for x in thisset if x!="banana"]

# to add items

thisset.add("chiku")
print(thisset)

set1.update(set2)
print(set1)

# we can also add alist , tuples or dictionary using update()
list1=[100,200]
set1.update(list1)
print(set1)

# to remove items
# 1.
thisset.remove("banana")
print(thisset)

# if the item doesnt exit when we use remove it will throw an error

# 2.
set1.discard(100)
print(set1)

# 3.
set1.pop()
print(set1)  # we dont know which element will be popped

# 4.
set1.clear()
print(set1)

# 5.
# del set1
# print(set1)

# loop though sets

for x in thisset:
    print(x)
    
# to join sets remmeber maths wala set : union , intersection,difference here extra update, symmetric difference

# 1.
set3=thisset.union(set2)
print(set3)

# union can also be done using | 
set3=thisset|set2
print(set3)

# can join multiple sets
set4=set3.union(set2,thisset)
print(set4)

set4=set3|set2|thisset
print(set4)

# join set and tuple
tup=(1,2,3)
set5=set4.union(tup)
print(set5)
# cant do the above set and tuple union using | these are only allowed with sets union

# 2. 
set4.update(set5)
print(set4)

# intersection

# 1.
set6=set3.intersection(set5)
print(set6)

# 2.
set6=set3&set5
print(set6)

# it will gives the duplicates , and changes the original set instead of returning new set
set4.intersection(set3)
print(set4)

set7=set4&set5
print(set7)

set7=set4.difference(thisset)
print(set7)

set7=set4-thisset
print(set7)

# to keep the elemenst that are not present in boht the sets
set3=set4.symmetric_difference(thisset)
print(set3)
# you can do the above code by using ^ 
set3=set4^thisset
print(set3)


# set methods
# 1. add()
set3.add("9")
print(set3)

# 2. clear() - removes all the elements from the set
set3.clear()
print(set3)

# 3.copy() return the copy of the set
set3=thisset.copy()
print(set3)

# 4. pop() removes an element 
set3.pop()
print(set3)

# 5. remove() removes the specified element
set3.remove("cherry")
print(set3)


