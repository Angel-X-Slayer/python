n=int(input("Enter the number of rows : "))
print()
for i in range(n):
    for j in range(n):
        if(i==0 and i==n and j==0 and j==n):
            print("*")
        else:
            print(" ")