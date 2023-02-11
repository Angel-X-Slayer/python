def fibo(k):
    if(k==1):
        return 0
    elif(k==2):
        return 1
    else:
        return (fibo(k-1) + fibo(k-2))


n=int(input("enter the limit : "))
if (n<=0):
    print("enter a appropiate limit")
else:
    print("the required serise is :",end=" ")
    for i in range(1,n+1):
        print(fibo(i),end=" ")
    print(" ")

## end of fibonacci serise ##









## start of factotial ##

def fact(n):
    if n==1:
        return(1)
    else:
        return(n*fact(n-1))
n=int(input("enter the number:"))
d=fact(n)
print(f"the factorial of {n} is :",d)
