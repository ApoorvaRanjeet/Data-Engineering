# 1.lists are ordered
# 2. changeable
# 3. allow duplicates
# 4. list item can be of any data type 
# 5. list can have values of different data type
# 6 we can use the list constructor to create a list like x=list((1,2,3))
# 7. list is ordered meaning that the items have a defined order and that order will not change if we add new element then it will be placed in the end of the list

a=["ap",1,1.20]
print(a)

x=list(("ap","df"))
print(x)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

for i in thislist:
    if i is "apple":
        print("yes")
        break
    
        
if "apple" in thislist:
    print("yay")
    
    
# change the items of list 
thislist[1:3]=["aadrika","anusha"]
print(thislist)

thislist[1:3]=["aadrika","anusha","Shobhna"]
print(thislist)

thislist[1:3]=["apoorva"]
print(thislist)

# insert the items to list
thislist.insert(2,"aadrika")
print(thislist)

# append the items to list
thislist.append("anusha")
print(thislist)

# extend list 
another=["a","b"]
thislist.extend(another)


another_tuple=('aa','bb')
thislist.extend(another_tuple)
print(thislist)

# in extend we dont only need to append elements from list we can also append other iterable objects like tuples,set dictioneries etc.
print(thislist)
# to remove item from the list

thislist.remove("apoorva")
print(thislist)

# if there are more item similar to the item need to be removed then remove methid removes the first occurenece

# in order to remove the element from specific index then we use POP
thislist.pop(1)
print(thislist)

# if we do not specify the index the pop method removes the element from the last 
# del keyword also removes the specified index item , alos it can delete the complete list
del thislist[0]
print(thislist)

del thislist
print(thislist)

# clear method empties the list unlike del keyword 
thislist.clear()
print(thislist)



# loop though lists 
thislist = ["apple", "banana", "cherry"]
for i in thislist:
    print(i)

# loop through index 

for i in range(len(thislist)):
    print(thislist[i])
    
# using while loop

i=0
while i<len(thislist):
    print(thislist[i])
    i+=1

# looping using list comprehension

[print(x) for x in thislist]

# list comprehension
newlist=[]
for x in thislist:
    if "apple" in x:
        newlist.append(x)
print(newlist)

#list comprehension version of the above code
newlist=[x for x in thislist if "cherry" in x]
print(newlist)

newlist=[x for x in range(10)]
print(newlist)

newlist=[x for x in thislist if x!="apple"]
print(newlist)

newlist=[x for x in range(10) if x>0 and x<5 and x!=4]
print(newlist)

newlist=[x.upper() for x in thislist]
print(newlist)

newlist=["hello" for x in thislist]  # setting all the values to hello in the new list
print(newlist)

newlist=[x if x!="cherry" else "orange" for x in thislist]
print(newlist)

# sort list 
newlist.sort()

list=[100,24,23,45,75]
list.sort()
print(list)

list.sort(reverse=True)
print(list)

case_sensitive=['a','A','b','C']
case_sensitive.sort()
print(case_sensitive)

# inorder to sort irrespective of cases ignoring case sensitivity
case_insensitive=['a','A','b','C']
case_insensitive.sort(key=str.lower)
print(case_insensitive)

case_insensitive.sort(reverse=True)
print(case_insensitive)


# to copy a list 
# 1
mylist=case_insensitive.copy()
print(mylist)

# 2
mylist=list(case_insensitive)
print(mylist)

# 3
mylist=case_insensitive[:]
print(mylist)

# join two lists
# 1
list3=case_sensitive+case_insensitive
print(list3)

# 2
for x in case_sensitive:
    case_insensitive.append(x)
print(case_insensitive)

# 3
case_sensitive.extend(case_insensitive)
print(case_sensitive)