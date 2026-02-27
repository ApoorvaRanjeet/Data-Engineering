# dictionary is key value pair whereas key is the identifier of the value 

student ={'name':'apoorva','age':'22','courses':['maths','sci']}
print(student)
print(student['age'])
print(student.get('name'))
print(student.get('class')) # instead of throwing error its shows the default none as an output
print(student.get('class','not found')) # instead of none we can get not found or anything as an output
student['class']='gec02 g065' #can add the new value
print(student)
student['age']=23 #can update the existing value
print(student)

# to update the value we can also use update method 
student.update({'name':'reshank','age':'25'})  # we can update multiple value together using update
print(student)

# to remove the value from dictionary we can use del methos , also the pop method it removes the value and return the value
del student['age']
print(student)

age=student.pop('age')
print(age)

print(len(student))

print(student.keys())
print(student.values())
print(student.items()) # to print both keys and values 

for key in student:
    print(key)
    
    
for key,value in student.items():
    print(key,value)