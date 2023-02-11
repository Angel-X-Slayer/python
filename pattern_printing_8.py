n=int(input("enter the number of row : "))
for i in range(n):
    print("*"*(n-i),end="")
    print(" "*i,end="")
    print(" "*i,end="")
    print("*"*(n-i),end="\n")
for i in range(n):
    print("*"*(i+1),end="")
    print(" "*(n-1-i),end="")
    print(" "*(n-1-i),end="")
    print("*"*(i+1),end="\n")

