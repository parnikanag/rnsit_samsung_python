#Accept a number and find the next smallest possible bigger number that must have all digits as in the input number

import random

def fact(n):
    if n==0 or n==1 :
        return 1
    else:
        return n*fact(n-1)
    
n = input("Enter a Number: ")

nlist = list(n)

tlist=[]

for i in range (fact(len(n))):
    random.shuffle(nlist)
    temp=''.join(nlist)
    if int(temp)>int(n):
        tlist.append(temp)
        
tlist.sort()

print(tlist[0])
