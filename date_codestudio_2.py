def target_sun(arr,target):
    op=[]
    # arr=sorted(arr)
    arr.sort()
    # print(arr)
    
    i=0
    j=len(arr)-1
    while i<j:
        if arr[i]+arr[j]>target:
            if j-1>=0:
                j=j-1
                b=arr[j]
                
                
        if arr[i]+arr[j]<target:
            if i+1<=len(arr)-1:
                i=i+1
                a=arr[i]
                
                
        if arr[i]+arr[j]==target:
            op.append(arr[i])
            op.append(arr[j])
    
            i+=1
    if len(op)==0:
        print("no pair found")
    else:

        print(int(len(op)/2))



arr=list(map(int,input().split(" ")))
target=int(input())
target_sun(arr,target)
