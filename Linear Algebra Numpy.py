import numpy

n=int(input())
A1=[]
for i in range(n):
    t=list(map(float,input().split()))
    A1.append(t)
array=numpy.array(A1)
print(round(numpy.linalg.det(array),2))

