
from operator import itemgetter



def person_lister(f):
    def inner(people):
        #earlier failed cause of sort in the string type
        people.sort(key=lambda x: int(x[2]))
        #print(people)
        array=[]
        for i in people:
            array.append(f(i))
        
        return array

        
    return inner

