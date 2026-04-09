import pandas as pd

df=pd.DataFrame()

print(df)

# the above is the creation of the empty dataframe.

# creating dataframe from a list

lst=[1,2,3,4,5]

df=pd.DataFrame(lst)
print(df)

# creating dataframe from dictionary

data={
    "name":["apoorva","aadrika","anusha","shobhna"],
    "age":[23,23,26,61]
}

df=pd.DataFrame(data)
print(df)