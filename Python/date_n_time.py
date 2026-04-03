import datetime

x=datetime.datetime.now()

print(x)
print(x.year)
print(x.strftime("%A"))

# creating date objects 
'''it requires three parameters to create a date: year,month,day.'''

c=datetime.datetime(2003,11,8)

print(c)

print(c.strftime("%A"))
print(c.strftime("%w"))
print(c.strftime("%d"))
print(c.strftime("%B"))