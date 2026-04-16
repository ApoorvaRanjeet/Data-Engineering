import pandas as pd
player_list = [['M.S.Dhoni', 36, 75, 5428000],
               ['A.B.D Villers', 38, 74, 3428000],
               ['V.Kohli', 31, 70, 8428000],
               ['S.Smith', 34, 80, 4428000],
               ['C.Gayle', 40, 100, 4528000],
               ['J.Root', 33, 72, 7028000],
               ['K.Peterson', 42, 85, 2528000]]

df = pd.DataFrame(player_list, columns=['Name', 'Age', 'Weight', 'Salary'])

# selection of columns 
# single column 
# print(df.loc[["Name"]])  this doesnt works kyunki .loc always expects row, column and colum is optional when we say df.loc[[0,3]] it means 0,3 rows and all columns and this particular code fails cozthere is no row with label Name
print(df.loc[0:2,"Name"]) # single column single [] bracket
print(df.loc[0:2,["Name","Age"]]) # double columns toh sqaure bracket ke andar meaning double [] brackets

# selection of rows
print(df.loc[0])  # single row
print(df.loc[[0,3]])  # multiple rows


# When to use [[]] in loc

# Use when selecting:

# multiple columns
# multiple rows
# both rows & columns

print(df.iloc[1:3,[0,2]])