a=[1,2,3,4,5,6]
mid=(len(a)-1)//2
for i in range(mid+1):
    temp=a[mid+1+i]
    a[mid+1+i]=a[i]
    a[i]=temp
print(a)