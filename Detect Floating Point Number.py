# Enter your code here. Read input from STDIN. Print output to STDOUT

n=input()
ans=[]
for i in range(int(n)):
    a=input()
    try:
        float(a)
        if a.count('.') == 1 and a[-1] in '0123456789':
            ans.append(True)
        else:
            ans.append(False)         
        
    except:
        ans.append(False)
for i in ans:
    print(i)
