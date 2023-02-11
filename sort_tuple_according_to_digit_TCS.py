# a=[(3,4,6,723),(1,2),(134,234,34)]
n=int(input())
a=[]
for i in range(n):
    tup=tuple(map(int,input().split(" ")))
    a.append(tup)
dig_count=[]
for i in a:
    count=0
    for j in i:
        if j<10:
            count+=1
        elif j<100 and j>10:
            count+=2
        elif j<1000 and j>100:
            count+=3
        elif j<10000 and j>1000:
            count+=4
        else:
            count+=5
    dig_count.append(count)
dic={}
dic=dict(zip(a,dig_count))
# for i in dic:
#     print(i)
d=sorted(dic.keys(),key=lambda k:(k[1],k[0]))
print(d)
