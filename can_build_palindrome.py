import collections
str=input()
frq={}
frq=collections.Counter(str)
s=sum(frq.values())
if len(set(frq.values()))==1:
    print("palindrome not possible")
else:
    if len(str)%2!=0:
        k=len(str)//2
        if len(str)%k==1:
            print("palindrome possible")
        else:
            print("palindrome not possible")
    else:
        if s%2==0:
            print("palindrome possible")
        else:
            print("palindrome not possible")

