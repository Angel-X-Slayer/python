n=int(input())
a=[]
b=[]
for i in range(n+1):
    if (i%2==0):
        a.append(i)
    else:
        b.append(i)

print("The even serise is :",end=" ")
print(a)
print("the odd serise is :",end=" ")
print(b)