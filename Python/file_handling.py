# File handling

# open() function takes two paramters : filename and mode
# "r": reads the file , thows errorif file doent exist
# "a": appends in file , creates a file if doesnt exist
# "w": writes in file , creates a file of doesnt exist
# "x": create the file , reaturns error if the file exists

f=open("file1.txt")

#  "t":text mode
#  "b": binary mode

#  1.
#  open file

print(f.read())

#  using with statement
with open("file1.txt") as f:
     print(f.read())

#  2. to close a file
# '''always remember is you are not using with statement then its a best practise to close a file'''
f.close()

#  read only parts of the file

with open("file1.txt") as f:
     print(f.read(5))
    
#  readlines : you can return one line by using the readline() method
with open("file1.txt") as f:
     print(f.readline())

with open("file1.txt")as f:
     print(f.readline())
     print(f.readline())
     # will return two lines
    
    
#  looping thorugh the line of the file you can read the whole file line by line

with open("file1.txt") as f:     
     for x in f:
         print(x)
    
# write to an existing file 

''' a will append to the end of the file
    w  will overwrite to an existing content
'''
 
with open("C:/Users/apoor/OneDrive/Documents/data engineer/Python/file1.txt","a") as f:
    f.write(f"adding more content to the file using {"a"} ")
with open("C:/Users/apoor/OneDrive/Documents/data engineer/Python/file1.txt") as f:
    print(f.read())

# overwite an existing file

with open("C:/Users/apoor/OneDrive/Documents/data engineer/Python/file1.txt","w") as f:
    f.write("woops i accidently deleted the existing content!")
    
with open("C:/Users/apoor/OneDrive/Documents/data engineer/Python/file1.txt") as f:
    print(f.read())
    
# to create a new file 

'''use open() with any of these parameters:
    "x" : create a file , throws an error if file doesnt exists
    "a" : will create a file if specified file doesnt exists
    "w" : will create a file if specified file doesnt exists
'''
    
f = open("new_file.txt","x")


# to delete a file 

''' import os module and run this '''

import os
os.remove("new_file.txt")

    # before deleting we can check if file exists or not

if os.path.exists("new_file.txt"):
    os.remove("new_file.txt")
else:
    print("file doesnt exists")
    

# to delete a folder 

os.rmdir("myfolder") # note : we can only remove empty folders
    








