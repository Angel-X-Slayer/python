str=input()
str1=[]
for i in range(len(str)):
    str1.append(int(str[i]))
count=0
zer=[]
ons=[]
op=[]
dic={}
for i in range(0,len(str1),2):
    if i!=len(str1)-1:
        zer.append(str1[i])
        ons.append(str1[i+1])
    else:
        zer.append(str1[i])


## if starts with zero

for i in range(len(zer)):
    if zer[i]!=0:
        zer[i]=0
        count+=1
for i in range(len(ons)):
    if ons[i]!=1:
        ons[i]=1
        count+=1
k=max(len(zer),len(ons))
for i in range(k):
    if i>len(zer) or i>len(ons):
        l=0
        break
    else:
        op.append(zer[i])
        op.append(ons[i])
    l=1
if l==0 and len(zer)>len(ons):
    op.append(zer[len(zer)-1])
elif l==0 and len(zer)<len(ons):
    op.append(ons[len(ons)-1])
dic.__setitem__(count,op)

##if starts with one

ons=[]
zer=[]
op=[]
for i in range(0,len(str1),2):
    zer.append(str1[i])
    ons.append(str1[i+1])
count=0
op=[]
for i in range(len(zer)):
    if zer[i]==0:
        zer[i]=1
        count+=1
for i in range(len(ons)):
    if ons[i]==1:
        ons[i]=0
        count+=1
k=max(len(zer),len(ons))
for i in range(k):
    if i>len(zer) or i>len(ons):
        l=0
        break
    else:
        op.append(zer[i])
        op.append(ons[i])
    l=1
if l==0 and len(zer)>len(ons):
    op.append(zer[len(zer)-1])
elif l==0 and len(zer)<len(ons):
    op.append(ons[len(ons)-1])
dic.__setitem__(count,op)
print(*dic[min(dic.keys())],sep="")