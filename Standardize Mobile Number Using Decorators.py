def wrapper(f):
    def fun(l):
        # complete the function
        formatted = []
        #l=sorted(l)
        for number in l:
            number = number[-10:]
            #print(number)
            formatted.append(f"+91 {number[:5]} {number[5:]}")
        formatted=sorted(formatted)
        for i in formatted:
            print(i)

    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


