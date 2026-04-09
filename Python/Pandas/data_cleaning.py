'''data cleaning:
bad data is :-> null values, data in wrong format , duplicates, wrong data'''


# 1. empty cells 

# way 1.:-> remove rows thst contain empty cells

import pandas as pd

df=pd.read_csv('C:/Users/apoor/OneDrive/Documents/data engineer/Python/pandas/data.csv')
print(df.info())
new_df=df.dropna()
print(new_df.info())

'''dropna() method returns a new dataframe and will not change the original.
in order to change the origina; one use inplace=True argument'''

df=pd.read_csv('C:/Users/apoor/OneDrive/Documents/data engineer/Python/pandas/data.csv')
df.dropna(inplace=True)

print(df.info())

# inplace=True will not return a new dataframe but it will remove null values from the original dataframe.

# way 2:-> replace empty values (meaning insert new value instead)

# we will use fillna() method allows to replace null values with a value

df=pd.read_csv('C:/Users/apoor/OneDrive/Documents/data engineer/Python/pandas/data.csv')
df.fillna(130,inplace=True)


# replace only for specified columns 
df.fillna({"Calories":130},inplace=True)

# replace using mean median or mode

df=pd.read_csv('C:/Users/apoor/OneDrive/Documents/data engineer/Python/pandas/data.csv')
x=df["Calories"].mean()
df.fillna({"Calories":x},inplace=True)

df=pd.read_csv('C:/Users/apoor/OneDrive/Documents/data engineer/Python/pandas/data.csv')
x=df["Calories"].median()
df.fillna({"Calories":x},inplace=True)

df=pd.read_csv('C:/Users/apoor/OneDrive/Documents/data engineer/Python/pandas/data.csv')
x=df["Calories"].mode()[0]
df.fillna({"Calories":x},inplace=True)

# 2. Data of wrong format 

# either remove those rows or convert into the correct format 

df['Date']=pd.to_datetime(df['Date'],format='mixed')

print(df.to_string())

df.dropna(subset=['Date'],inplace=True)

# fixing wrong data
    # replacing values
df.loc[7,'Duration']=45 # duration column ke 7th row mein value 45 kardo

# looping the dataset and chaning its values
'''To replace wrong data for larger data sets you can create some rules, 
e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.'''
for i in df:
    if df.loc[i,'Duration']>120:
        df.loc[i,'Duration']=120
        
# removing rows that contains the wrong data 

for i in df:
    if df.loc[i,'Duration']>120:
        df.drop(i,inplace=True)   # delete rows where duration is higher than 120


# 3. Removing Duplicates
'''To discover duplicates, we can use the duplicated() method.

The duplicated() method returns a Boolean values for each row:'''

print(df.duplicated())

# to drop the duplicates we use drop_duplicates()

df.drop_duplicates(inplace=True)

# inplcase=True deletes the roes from the existing dataframe instead of returning new daatframe

     