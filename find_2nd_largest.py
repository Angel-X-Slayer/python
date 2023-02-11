def secnd_largest(arr,n):
    i,maxi,p,c=0,0,0,0
    while i<n:
        if arr[i]>maxi:
            maxi=arr[i]
        i+=1
# print(maxi)
    max2=maxi
    for i in range(n):
        if arr[i]==maxi:
            pass
        else:
            p=maxi-arr[i]
            if p<max2:
                max2=p
                c=arr[i]
    print(c)




n=5
arr=[1,2,3,4,5]
for i in range(n):
    num=int(input("enter the number in the array"))
    arr.append(num)
secnd_largest(arr,n)
# print(arr)
