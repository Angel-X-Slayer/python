def max_diff(arr):
    mini=arr[0]
    maxi=arr[0]
    for i in range(len(arr)-1):
        if arr[i+1]<mini:
            mini=arr[i+1]
    for i in range(len(arr)-1):
        if arr[i+1]>maxi:
            maxi=arr[i+1]
    print(mini,maxi)
    maxdiff=maxi-mini
    print(maxdiff)

# arr=[80, 2, 6, 3, 100]
arr=[1,2,1,2,1,2,1,2,1,2,1]
max_diff(arr)