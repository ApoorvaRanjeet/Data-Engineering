'''DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)
subset = specific column 
keep = finds which duplicate to keep : first,last , false(remove all occurence)
inplace =  to modify the original dataframe'''


import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Alice", "David"],
    "Age": [25, 30, 25, 40],
    "City": ["NY", "LA", "NY", "Chicago"]
}

df=pd.DataFrame(data)

print(df)
df=df.drop_duplicates()

print(df)

# keeping the last occurence of duplcates

df=df.drop_duplicates(keep='last')

# dropping all the duplicates

df=df.drop_duplicates(keep=False)

# modifying the original dataframe

df=df.drop_duplicates(inplace=True)

# dropping duplicates base on partially identical columns

data = {
    "Name": ["Alice", "Bob", "Alice", "David", "Bob"],
    "Age": [25, 30, 25, 40, 30],
    "City": ["NY", "LA", "NY", "Chicago", "LA"]
}

df=pd.DataFrame(data)

df=df.drop_duplicates(subset=["Name","city"])