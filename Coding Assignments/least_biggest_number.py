import random

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
    
num=input("Enter a Number: ")
num_list=list(num)

temp_list=[]

for n in range (fact(len(num))):
    i=num_list[ : ]
    random.shuffle(i)
    temp="".join(i)
    if temp > num:
        temp_list.append(temp)
        
temp_list.sort()
if temp_list:
    print(temp_list[0])
else:
    print("Not Possible")