def crease(n, x):
    k=0
    if(n%2==0):
        m=n/2
        if(m%2==0):
            k=m/2
    else:
        print("no")
    if(k==x):
        print("yes")

t=int(input("entre the number of test cases :"))
n1=int(input("enter the number of n for the 1st case :"))
x1=int(input("enter the number of x for the 1st case :"))
n2=int(input("enter the number of n for the 2nd case :"))
x2=int(input("enter the number of x for the 2nd case :"))
crease(n1,x1)
crease(n2,x2)
