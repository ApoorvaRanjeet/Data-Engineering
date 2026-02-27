nums=[1,2,3,4,5]

for num in nums:
    if num==3:
        print('found')
        break
    print(num)
    
for num in nums:
    if num==3:
        print('found')
        continue
    print(num)
    
for num in nums:
    for letter in 'abc':
        print(num,letter)

for i in range(10):
    print(i)

for i in range(1,10):
    print(i)
    
x=1
while x<=10:
    print(x)
    x+=1

while x<=10:
    if x==5:
        break
    print(x)
    x+=1
    
while True:
    if x==5:    #if we remove the break statement then it will be infinite loop 
        break
    print(x)
    x+=1