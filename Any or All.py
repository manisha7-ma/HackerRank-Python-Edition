# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
array=list(map(int,input().split()))
ans=False
for i in array:
    ans=all([i>0])
ans2=False
for i in array:
    ans2=ans2|any([str(i) == str(i)[::-1]])
    
print(ans&ans2)

