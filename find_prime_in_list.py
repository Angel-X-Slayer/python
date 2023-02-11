def find_prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
        else:
            pass
    if count>2:
        return(-1)
    else:
        return(0)


a=[1,2,3,4,5,6,7,8,9]
count1=0
for i in a:
    k=find_prime(i)
    if k==0:
        count1+=1
print(count1)

