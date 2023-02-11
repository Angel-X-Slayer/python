n=int(input("Enter the number :"))
s=0
while(n!=0):
    r=int(n%10)
    n=int(n/10)
    s=s+r
print(f"The sum is {s}")