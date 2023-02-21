arr=list(map(int,input().split(" ")))
cou=0
i=0
j=len(arr)-1
for i in range(len(arr)):

    for k in range(j,i,-1):

        if arr[i]>=arr[k] and i<j:
            print(arr[i],arr[k])
            cou+=1
        else:
            continue
print(cou)
# print(arr)