x=10

def func_global():
    x=30
    print(x)
func_global()
print(x)
    
a="10"
def func_global_1():
    global a
    a=40
    print(a)
func_global_1()
print(a)
    