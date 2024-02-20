arr = list(map(int, input("enter the elements").split(" ")))
water = 0
k = arr[1]
for i in range(1, len(arr)-1):
    if arr[i] <= arr[i-1] and arr[i] <= arr[i+1]:
        if arr[i-1] > arr[i+1]:
            water += arr[i-1]-arr[i]
        else:
            water += arr[i+1]-arr[i]
    elif arr[i] <= arr[i-1] and arr[i] >= arr[i+1]:
        water += arr[i-1]-arr[i]
    elif arr[i] >= arr[i-1] and arr[i] <= arr[i+1]:
        if arr[i-1] > arr[i+1]:
            water += arr[i+1]-arr[i]
    elif arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
        pass
print(water)
