from array import *

def sum_of_elements(ar):
    sum=0
    for i in ar:
        sum=sum+i
    print(sum)

ar=array('i',[])
n=int(input("enter the lenth of the array :"))
for i in range(n):
    x=int(input("entre the value :"))
    ar.append(x)
sum_of_elements(ar)
