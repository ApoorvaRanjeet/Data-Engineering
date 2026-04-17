# read_csv()  function in pandas is used to read data from csv files into pandas dataframe.

'''parameters with pd.read_csv()
filepath 
sep :-> separator , by default is ',' 
header 
usercols :-> to retrieve specific columns form csv file
nrows :-> no.of rows to be displayed
'''


import pandas as pd

df=pd.read_csv('C:/Users/apoor/OneDrive/Documents/data engineer/Python/pandas/data.csv')


# read specific columns

df=pd.read_csv('C:/Users/apoor/OneDrive/Documents/data engineer/Python/pandas/data.csv',usecols=["Duration","Pulse"])
# print(df)

# setting the column as an index of the dataframe

df=pd.read_csv('C:/Users/apoor/OneDrive/Documents/data engineer/Python/pandas/data.csv',index_col="Pulse")
# print(df)

# handling missing values

df=pd.read_csv('C:/Users/apoor/OneDrive/Documents/data engineer/Python/pandas/data.csv',na_values=["N/A","Unknown"])
print(df)