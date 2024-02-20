def left_ratation(arr):
    temp = arr[len(arr)-1]
    for i in range(len(arr)-2, -1, -1):
        arr[i+1] = arr[i]
        arr[i] = arr[i-1]
    arr[0] = temp

    return (arr)


arr = list(map(int, input("enter the elements").split(" ")))
k = int(input("enter the amount of left rotation: "))
for i in range(k):
    arr = left_ratation(arr)
print(arr)
