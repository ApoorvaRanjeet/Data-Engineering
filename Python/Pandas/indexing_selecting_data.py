'''1. selecting a single column
single column access krne ke liye simple column name use krte
'''

import pandas as pd 

data={
    "Name":["aadrika","apoorva","anusha","shobhna"],
    "age":[23,23,26,61],
    "gender":["female","female","female","female"]
}

df=pd.DataFrame(data,index=["a","b","c","d"])

# print(df)

# print(df["age"])

'''2. selecting multiple columns
1st way is to give list of column names inside []'''

print(df[["Name","age"]])


# indexing with .loc[]

print(df.loc["a"])   

#always remember loc , iloc mein humlog index se related kaam kr rhe 
# multiple rows by label
# print(df.loc[["apoorva","anusha"]]) # yeh isliye error de rha hai kyunki instead of giving index labels im giving values from column 

print(df.loc[["a","c"]])

'''print(df.loc[["apoorva","anusha"]]) if we did wanted to do this we can do it by making the name column as an index
df=df.set_index("Name")
print(df.loc[["apoorva","anusha"]])'''

# selecting specific rows and columns 
print(df.loc["a":"b",["Name","age"]])


# selecting all rows and specific columns
'''.loc expects a list of columns when selecting multiple
Single column
df.loc[:, "Name"]

No list needed.

Multiple columns
df.loc[:, ["Name","gender"]]

List required.

❌ This is wrong
df.loc[:, "Name","gender"]

Because Pandas thinks you passed 3 arguments, but .loc only accepts:

rows , columns

Not:
rows , col1 , col2'''
print(df.loc[:,["Name","gender"]])


# indexing with .iloc[]
# selcting single row by position
print(df.iloc[0:2])  # we dont need index labels coz iloc works with numbers thats why this wont thow an error


#selecting multiple rows by position
print(df.iloc[[0,2,3]])

# selecting specific rows and columns by position
print(df.iloc[0,1],[1,2])