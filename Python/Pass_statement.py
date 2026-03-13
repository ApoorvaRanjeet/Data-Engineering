# somethings about pass

# 1. pass statement is null operation , nothing happens when it executes.It serves as a placeholder
# jab koi as such kaam nhi hai par ya fir syntactically likhna padh gaya of block ya kuch toh pass likh diya kuch update krna tha par baad mein toh tab tak ke liye pass likh diya 
# agar hum khali if block chor denge toh woh error dega , isliye pass use kr skte hain in such conditions 


# also important about for loop if else included in for loop then after break statement else statement is not executed

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
  
for x in range(6):
  print(x)
else:
  print("Finally finished!")

