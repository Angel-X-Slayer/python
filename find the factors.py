n=int(input("Enter the number : "))
a=[]
for i in range(1,n+1):
    if(n%i==0):
        a.append(i)
    else:
        continue
print("The factors are")
print(a)