def gcd(n,i):
    if (n==0 or i==0):
        return 0
    if n==i:
        return(n)
    if n>i:
        return(gcd(n-i,i))
    else:
        return(gcd(n,n-i))



n=4
o=0
for i in range(1,n+1):
    k=gcd(n,i)
    if k==1:
        o+=1
    else:
        pass
print(o)

    
for i in range(n):
    hcf=1
    for j in range(1,n+1):
        if n%j==0 or i%j==0:
            hcf=j
if hcf==1:
    print("co")
else:
    print("not")
