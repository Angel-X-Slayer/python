k=input("enter the data :")
m=len(k)
dat=[]
for i in range(m):
    dat.append(k[i])
dat=list(map(int,dat))
for i in range(m):
    if m+i+1<=pow(2,i):
        break
    else:
        pass
r=i
total=[None]*(m+r)
for i in range(r):
    if (m+r)-pow(2,i)==(m+r-1):
        total[m+r-1]=0
    else:
        total=total[:(m+r)-pow(2,i)]+[0]+total[(m+r)-pow(2,i)+1:]

i=0
j=0
while i<(len(dat)) and j<len(total):
    if total[j]==None:
        total[j]=dat[i]
        i+=1
        j=+1
    else:
        j+=1
sum=0
r0=[]
sol=[]
for i in range (r):
    k=pow(2,i)
    i1=0
    l=k
    while l<r+m:
        if i1<k:
            r0.append(1)
            i1+=1
            l+=1
        elif i1==k:
            for i1 in range(k-1,-1,-1):
                l+=1
    for q in r0:
        sum+=total[q]
    if q%2==0:
        sol.append(0)
    else:
        sol.append(1)
    
    r0=[]
print(*sol,sep="")