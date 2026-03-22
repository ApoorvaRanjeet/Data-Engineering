# import math
def one_step(start,end):
    result=[]
    
    for i in range(start,end):
        st=str(i)
        ans=True
        for j in range(len(st)-1):
            if abs(int(st[j])-int(st[j+1]))!=1:
                ans=False
                break
        if ans==True:
            result.append(i)
    
    return result

print(one_step(101,200))