import pandas as pd

df=pd.read_csv('C:/Users/apoor/OneDrive/Documents/data engineer/Python/pandas/data.csv')

print(df)

print(df.to_string()) # to print the entire dataframe

print(pd.options.display.max_rows) # check your systems maximum rows

'''i got the output as 60 which means if the dataframe contains more than 60 rows the print(df) will return only the headers and the first and last 5 rows.
we can change the number of rows to display the entire dataframe'''
