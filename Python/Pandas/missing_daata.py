# checking missing values in pandas

'''1. using isnull() :-> returns dataframe of boolean values where true represent missing data'''
import pandas as pd
import numpy as np

d = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}

df=pd.DataFrame(d)

# print(df.isnull())

# filtering the data based on missing values
'here we will apply isnull() on specific column to find out the null values in that column'

df=pd.read_csv('C:/Users/apoor/OneDrive/Documents/data engineer/Python/pandas/data.csv')

null_values=pd.isnull(df['Calories'])
missing_calories=df[null_values]
print(missing_calories)

# the above code can also be written as :

missing_calories=df[df['Calories'].isnull()]
print(missing_calories)

'''explanation :  isnull() returns True/False values.
Passing that to df selects rows where value is True.'''


'2. isna() does the same thing returns dataframe of boolean values where true indicates the missing data'
print(df.isna())

'3. checking for non missing values using notnull()  , here notnull() returns a dataframe of boolean values where truw indicates non-missing data'

print(df.notnull())

# filtering data with non missing values
non_missing=df[df['Calories'].notnull()]
print(non_missing)

'Filling missing values in Pandas'

# 1. using fillna()
'fillna() used to replace missing values with a given value'

df=df.fillna(0) 
# or we can do df.fillna(0,inplace=True)
print(df.isnull().sum())

'''Most pandas functions return new DataFrame:

df.fillna()
df.dropna()
df.sort_values()
df.rename()

They don't change original unless:

assign back
or use inplace=True
'''

#fill with previous value(forward fill)
# the pad method is used to fill the missing value with its previous value.

df.fillna(method='pad',inplace=True)

# fill with next value backward fill

df.fillna(method='bfill',inplace=True)

# fill specific row with specific value

df['Calories'].fillna(0.1,inplace=True)

'2. using replace() : replace NaN or any values with specific value'
df=df.replace(to_replace=np.nan,value=-99)

'3. using interpolate() : used to fill missing values(NaN) using estimated  values based on sorrounding data.'
df['Calories'].interpolate()

# interpolate only works for numeric columns 

'''the difference in fillna and interpolate is that fillna fills constant value
When to use interpolate

Use when:

numeric data
time series
gradual changes
sensor data
missing middle values

Example:

temperature
stock price
calories
time-based data'''



'Dropping missing values in Pandas'

# 1. dropping rows with at least one null value
dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score': [52, 40, 80, 98],
        'Fourth Score': [np.nan, np.nan, np.nan, 65]}
df = pd.DataFrame(dict)

df.dropna()

# 2. dropping rows with all null values

dict = {'First Score': [100, np.nan, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score': [52, np.nan, 80, 98],
        'Fourth Score': [np.nan, np.nan, np.nan, 65]}
df = pd.DataFrame(dict)

df.dropna(how='all')

# 3. dropping columns with at least one null value
dict = {'First Score': [100, np.nan, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score': [52, np.nan, 80, 98],
        'Fourth Score': [60, 67, 68, 65]}
df = pd.DataFrame(dict)

df.dropna(axis=1)