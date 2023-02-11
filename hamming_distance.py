s1=input("enter the string:")
s2=input("enter the string:")
l=len(s1)
k=0
for i in range(l):
    if s1[i]==s2[i]:
        pass
    else:
        k+=1
print("the hamming distance b/w the two strings are",k)