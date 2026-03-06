import import_module # or we can write import import_model as im
courses=['history','math','physics','compsci'] 

index=import_module.find_index(courses,'math')
print(index)


# to import the function itself we can do this instead 

from import_module import find_index

courses=['history','math','physics','compsci'] 

index=find_index(courses,'math')
print(index)

# we cant access the variable of import_module if we do from import_modeule iport find_index so simply
# we can do either comlete import of module of from import_module import find_index,test

from import_module import find_index,test

courses=['history','math','physics','compsci'] 

index=find_index(courses,'math')
print(index)
print(test)


#  we can import everything form the module by simply just giving from import_module import *