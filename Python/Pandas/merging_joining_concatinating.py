import pandas as pd 

data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

data2 = {'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
         'Age': [17, 14, 12, 52],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

df = pd.DataFrame(data1, index=[0, 1, 2, 3])

df1 = pd.DataFrame(data2, index=[4, 5, 6, 7])

# to concat both of them 

'''Concatenating Dataframe using .concat()'''
frames=[df,df1]

new_df=pd.concat(frames)

print(new_df)
#----------------------------------------------------------------------
'''Concatenating dataframes by setting logic on axes'''


data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd'],
         'Mobile No': [97, 91, 58, 76]}

data2 = {'Name': ['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'],
         'Age': [22, 32, 12, 52],
         'Address': ['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
         'Qualification': ['MCA', 'Phd', 'Bcom', 'B.hons'],
         'Salary': [1000, 2000, 3000, 4000]}

df = pd.DataFrame(data1, index=[0, 1, 2, 3])

df1 = pd.DataFrame(data2, index=[2, 3, 6, 7])

# keeps the common columns
common=pd.concat([df,df1],axis=1,join='inner')

print(common)

# keeps all the commons
uncommon=pd.concat([df,df1],axis=1,join='outer')
print(uncommon)

uncommon_1=pd.concat([df,df1],axis=1,sort=False)
print(uncommon_1)



'''Joining Dataframes
    mainly two types of joins are there :
    1. Joins on columns : you combine dataframe using a common column
    2. Joins on index : pandas matches index values.'''


# joins on columns

import pandas as pd

df1 = pd.DataFrame({
    "id":[1,2,3],
    "Name":["Dhoni","Kohli","Root"]
})

df2 = pd.DataFrame({
    "id":[1,2,4],
    "Salary":[50000,60000,70000]
})

new_df=pd.merge(df2,df2,on="id")
print(new_df)
# types of column joins

print(pd.merge(df1,df2,on="id",how="inner"))
print(pd.merge(df1,df2,on="id",how="outer"))
print(pd.merge(df1,df2,on="id",how="left"))
print(pd.merge(df1,df2,on="id",how="right"))

# join on index

import pandas as pd

data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Key':['K0', 'K1', 'K2', 'K3']}

data2 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']}

df = pd.DataFrame(data1)

df1 = pd.DataFrame(data2, index=['K0', 'K2', 'K3', 'K4'])
res2 = df.join(df1, on='Key')

res2