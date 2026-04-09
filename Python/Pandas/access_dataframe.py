import pandas as pd

data={
    "Name":["aadrika","apoorva","anusha","shobhna"],
    "age":[23,23,26,61],
    "gender":["female","female","female","female"]
}

df =pd.DataFrame(data)
# print(df) # this is basic way of accessing the dataframe 

# accessing columns form the dataframe

print(df["Name"])

# accessing rows by index 
''' iloc is for positional indexing and loc is for label based indexing '''
data={
    "name":["aadrika","apoorva","anusha","shobhna"],
    "age":[23,23,26,61]
}
df=pd.DataFrame(data,index=["a","b","c","d"])

print(df)

print(df.loc["a"])
print(df.iloc[1])

# accessing multiple row or column

'''loc → includes end and iloc → excludes end'''

data={
    "Name":["aadrika","apoorva","anusha","shobhna"],
    "age":[23,23,26,61],
    "gender":["female","female","female","female"]
}

df=pd.DataFrame(data)

subset=df.loc[0:2,["Name","age"]]

print(subset)

# same thing we can do using iloc but we will use positions not names
# column positions : Name:-0 , age:-1 , gender:-2
# loc  → column names
# iloc → column index

subset=df.iloc[0:3,[0,1]]   # 0:3 3 coz in iloc end is excluded and in loc end is included 

# accessing rows based on conditions

new_df=df[df["age"]>25]
print(new_df)