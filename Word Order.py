from collections import OrderedDict
orderObj=OrderedDict()
n=int(input())
for i in range(n):
    s=input()
    if s in orderObj:
        orderObj[s]+=1
    else:
        orderObj[s]=1
        
print(len(orderObj))
for i in orderObj:
    print(orderObj[i],end=" ")
