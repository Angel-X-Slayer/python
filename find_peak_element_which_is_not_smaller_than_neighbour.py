arr = list(map(int, input("enter the elements").split(" ")))
# print(arr)
for i in range(1, len(arr)-1):
    if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
        print(arr[i])
