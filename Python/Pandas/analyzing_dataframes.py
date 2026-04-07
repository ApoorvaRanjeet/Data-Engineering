import pandas as pd

df=pd.read_csv('C:/Users/apoor/OneDrive/Documents/data engineer/Python/pandas/data.csv')

print(df.head())
print(df.tail())

# info about that data we use info()

print(df.info())