def minion_game(string):
    '''
    dictionary=dict()
    dictionary[string]=1
    for i in range(1,len(string)):
        for j in range(0,len(string)-i+1):
            current=string[j:j+i]
            if current in dictionary:
                dictionary[current]+=1
            else:
                dictionary[current]=1
    kevin=0
    stuart=0
    for i in dictionary:
        word=i
        if word[0] in 'AEIOU':
            kevin+=dictionary[i]
        else:
            stuart+=dictionary[i]
    ans=''
    if kevin<stuart:
        ans= "Stuart "+str(stuart)
    elif kevin==stuart:
        ans="Draw"
    else:
        ans= "Kevin "+str(kevin)
    print(ans)
    '''
    #OPTIMISED APPROACH
    length=len(string)
    kevin=0
    stuart=0
    for i in range(length):
        if string[i] in 'AEIOU':
            kevin+=length-i
        else:
            stuart+=length-i
    ans=''
    if kevin<stuart:
        ans= "Stuart "+str(stuart)
    elif kevin==stuart:
        ans="Draw"
    else:
        ans= "Kevin "+str(kevin)
    print(ans)
          
    
      
     
    

if __name__ == '__main__':
    s = input()
    minion_game(s)
