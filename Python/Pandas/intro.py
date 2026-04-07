'''pandas helps us analyzing the data 
it cleans the messy data sets and make them readable and relevant
'''

# PANDAS DATAFRAME:

'''is a 2D data structure like 2D array or a table with rows and columns'''

import pandas as pd

data={
    "calories":[420,12,13],
    "duration":[10,20,30]
}
df=pd.DataFrame(data)

print(df)


print(df.loc[0]) #pandas use loc attribute to return one or more specified row(s) , this one return pandas series 
print(df.loc[[0,1]]) # returns row 0 and 1, this [] one returns pandas dataframe

# Named indexes

'''with the index argument you can name your indexes'''

df=pd.DataFrame(data,index=["day1","day2","day3"])

print(df)

print(df.loc["day1"])


# load files into the dataframe

df=pd.read_csv('data.csv')
print(df)