from dataclasses import replace
import string


def dec2bin(n):
    a=[]
    while n!=0:
        r=int(n%2)
        n=int(n/2)
        a.append(r)
    print(*a[::-1],sep='')

n=int(input("enter the number u want to change :"))
dec2bin(n)