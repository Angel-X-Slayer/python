import numpy
n=32
a=[2,4,6,8]
arr=[]

for i in a:
    while n%i==0:
        n=n/i
        arr.append(i)
for i in arr:
    print(i,end=" ")
print("\t")
for i in range(len(arr)-2,int(len(arr)/2)-1,-1):
    prod1=1
    print(*arr[0:i],sep=" ",end=" ")
    prod1=prod1*numpy.prod(arr[i:])
    print(prod1)

for i in range(int(len(arr)/2)):
    prod1=1
    prod2=1
    prod1=prod1*numpy.prod(arr[0:i+1])
    prod2=prod2*numpy.prod(arr[i+1:])
    print(f"{int(prod1)} {int(prod2)}")


    
