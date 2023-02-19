def highestSum(arr):
    i=0
    j=len(arr)-1
    sum1=max(arr)
    while i<j:
        if sum(arr[i:j+1])>sum1:
            sum1=sum(arr[i:j+1])
            j-=1
        if sum(arr[i:j+1])<sum1:
            j-=1
        if sum(arr[i:j+1])==sum1:
            j-=1
    if sum1<0:
        print(0)
    else:
        print(sum1)

arr=list(map(int,input().split(" ")))
highestSum(arr)