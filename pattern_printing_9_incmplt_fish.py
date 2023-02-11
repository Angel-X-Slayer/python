n=int(input("Enter the value of rows : "))
for i in range(n):
    print("*"*(i+1),end="\n")
for i in range(n):
    print("*"*(n-1-i),end="\n")
for i in range(n):
        print(" "*(n-1-i),end="")
        print("*"*(i+1),end="")
        print("*"*i)
for i in range(n):
        print(" "*(i+1),end="")
        print("*"*(n-1-i),end="")
        print("*"*(n-2-i))