#  Python If-Else
# Language: Python

 
        #!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

c=n%2
if c!=0:
    print("Weird")
elif c==0 and n>=2 and n<=5 :
    print("Not Weird")
elif c==0 and n>=6 and n<=20 :
    print("Weird")
elif c==0 and n>20:
    print("Not Weird")

        