arr=list(map(int,input().split(" ")))
high=max(arr)
low=min(arr)
sum=int((high-low)/2)(high+low)
s=0
for i in arr:
    if i<0:
        pass
    else:
        s=s+i
op=sum-s
print(op)