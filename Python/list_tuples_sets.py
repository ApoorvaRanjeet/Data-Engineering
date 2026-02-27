list=['history','physics','maths']
print(list)
print(len(list))
print(list[0:2])
print(list[1:])
print(list[:1])

list.append('art')
print(list)

#if we use insert then theres 2 arguments first is position where we have to insert and the value what we have to insert
list.insert(4,'biology')
print(list)

courses=['cse','ai']
list.insert(0,courses)
print(list)

courses_2=['gaming']
list.extend(courses_2)
print(list)

list.remove('biology')
print(list)

list.pop()
print(list)

list.reverse()
print(list)

courses.sort()
print(courses)

courses.sort(reverse=True)  #in descending order
print(courses)

print(list.index('art'))


print('art' in list)

list.remove(courses)
for i in list:
    print(i)
    
for index,course in enumerate(list):  #enumerate func helps to keep track of both index and value
    print(index,course)
    
for index,course in enumerate(list,start=1):
    print(index,course)

#when we want to change the list into string iwth comma separated value 

str_list=' , '.join(list)
print(str_list)

# convert the string to list 

new_list=str_list.split(' , ')
print(new_list)

#the difference between tuples and list is that we cant modify tuples
#list are mutable and tuples are not mutable
 
list1=['a','b','c']
list2=list1
print(list1)
print(list2)
list1[0]='d'
print(list1)
print(list2)

#changes i made to list1 also reflects in list2 this is becuase of mutable feature

# tuple1=(1,2,3,4)
# tuple2=tuple1
# print(tuple1)
# print(tuple2)
# tuple1[0]=10
# print(tuple1)
# print(tuple2)
#same thing is impossible with tuple coz tuples are immutable
#we can append or remove and the features that demonsta=rtaes mutability are not supported in tuples

#sets are unordered and donot contains duplicates
set_1={1,2,3}
print(set_1)

set_2={1,2,3,3,4}
print(set_2)

print(1 in set_2)

#to find out the common values between two sets we can use intersection method

print(set_1.intersection(set_2))

#to find out uncommon values between these two sets we can use difference method
print(set_2.difference(set_1))
#to combine both the sets we can use combine method
print(set_1.union(set_2))


#how to create empty list,tuple,set
#empty list
empty_list=[]
empty_list=list() #can do this also to create empty list
print(empty_list)

#empty tuples
empty_tuple=()
empty_tuple=tuple()  #can do this also to create empty tuple
print(empty_tuple)

#empty set
empty_set={} # this is wrong cant do this 
empty_set=set() #need to use this inbuilt function 
