def filter_even(number):
    even_list=[]
    for i in number:
        if i%2==0:
            even_list.append(i)
    return even_list

print(filter_even([1,2,3,4,5,6]))


#to insert values in list we have 3 methods :
 # 1. append()  add one item to the end of the list
 # 2. insert()  adds an item at a specific index list.insert(1,'cherry')
 # 3. extend()  adds multiple items like one list to another list.extend(list1)    