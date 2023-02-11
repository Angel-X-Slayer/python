def find_coprime(n,i):
    if n==0 or i==0:
        return(0)
    if n==i:
        return(n)
    if n>i:
        return(find_coprime(n-i,i))
    else:
        return(find_coprime(n,i-n))



n=4
count=0
for i in range(1,n+1):
    k=find_coprime(n,i)
    if k==1:
        count+=1
    else:
        pass
print(count)



