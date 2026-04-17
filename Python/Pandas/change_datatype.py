'astype() this method allows you to convert a specific column to a desired data type.'

import pandas as pd

data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'], 
        'Age': [25, 30, 22, 35, 28], 
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 
        'Salary': [50000, 55000, 40000, 70000, 48000]}

df=pd.DataFrame(data)

df['Age']=df['Age'].astype(float)

print(df.dtypes)

# converting a column to a datetime type

df['Join Date'] = ['2021-01-01', '2020-05-22', '2022-03-15', '2021-07-30', '2020-11-11']
df['Join Date'] = pd.to_datetime(df['Join Date'])
print(df.dtypes)

# changing multiple columns data types
df=df.astype({'Age':'Float64','Salary':'str'})

print(df.dtypes)


'''important thing to remember : list → many items
dict → mapping
tuple → position'''