language='java'

if language=='Python':
    print('the statement is true')
elif language=='c##':
    print('c##')
else:
    print('java')
    
#python doesnt has switch case statement 

a=10
b='True'

if a==10 and b:
    print('yes')
else:
    print('no')
    
if a==10 or b:
    print('yes')
else:
    print('no')
    
if a!=10:
    print('yes')
else:
    print('no')

if not b:
    print('yes')
else:
    print('no')
    
    
#false values
#1.
condition=False

if condition:
    print('true')
else:
    print('false')
    
#2.
condition=None

if condition:
    print('true')
else:
    print('false')
    
#3.
condition=0.0

if condition:
    print('true')
else:
    print('false')
    
#4.
condition=[]   # {} , ''

if condition:
    print('true')
else:
    print('false')
    
# the above cases are just here to make me understand what will evaluate to true and what will evaluate to false so all the above exmaples will result in false