from itertools import combinations_with_replacement

n,m= input().split()
n=list(n)
n.sort()
m=int(m)
L=list(combinations_with_replacement(n,m))
#L.sort()
for i in L:
    print(''.join(i))
   
