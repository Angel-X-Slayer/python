arr=list(map(int,input().split(" ")))
high=len(arr)
low=high
for i in arr:
    if i<low and i>0:
        low=i
# print(high,low)
k1=(2*low)
k2=(high-1)
sum1=int((high*(k1+k2))/2)
# print(sum1)
s=0
for i in arr:
    if i<0:
        pass
    else:
        s=s+i
op=sum1-s
print(op)


