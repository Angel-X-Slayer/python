n=10
a=0
b=1
if n>0:
    if n==1:
        print(b)
    else:
        print(a,b,end=" ")
        for i in range(n-2):
            c=a+b
            print(c, end=" ")
            a=b
            b=c