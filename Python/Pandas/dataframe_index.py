'''the index in pandas dataframe shows the label given to each row, helps in accessing the data and can be either default numeric values or custom-defined labels'''

# to view the existing index we  can use .index

import pandas as pd

data={
    'Name': ['Jake', 'Eve', 'Charlie'],
        'Age': [ 22, 35, 28],
        'Gender': [ 'Male', 'Female', 'Male'],
        'Salary': [40000, 70000, 48000]
}

df=pd.DataFrame(data)
print(df)
print(df.index)

