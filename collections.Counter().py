from collections import Counter 
n=int(input())
array=list(map(int,input().split()))
L=Counter(array)
count=int(input())
earned=0
#print(L)
for i in range(count):
    size,price=map(int,input().split())
    #print(size,price)
    if L[size]>=1:
        L[size]-=1
        earned+=price
     #   print(earned)
    

print(earned)
