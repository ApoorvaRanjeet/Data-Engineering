import pandas as pd

player_list = [['M.S.Dhoni', 36, 75, 5428000],
               ['A.B.D Villers', 38, 74, 3428000],
               ['V.Kohli', 31, 70, 8428000],
               ['S.Smith', 34, 80, 4428000],
               ['C.Gayle', 40, 100, 4528000],
               ['J.Root', 33, 72, 7028000],
               ['K.Peterson', 42, 85, 2528000]]

df = pd.DataFrame(player_list, columns=['Name', 'Age', 'Weight', 'Salary'])
print(df)


# slicing using iloc[] (integer based indexing)

# slicing rows 
df1=df.iloc[0:3]
print(df1)

# slicing columns
df2=df.iloc[:,0:2]
print(df2)



# pratcise 

print(df.loc[:,"Name"])

print(df.iloc[0:4])

print(df.loc[:,["Name","Salary"]])

print(df.loc[1])
print(df.iloc[1])

print(df.loc[0:3,["Name","Age"]])

print(df[df["Age"]>35])

print(df[df["Salary"]>5000000])

