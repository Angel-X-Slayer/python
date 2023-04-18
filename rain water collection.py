arr = list(map(int, input().split(" ")))
sum = 0
if arr[0] < arr[len(arr)-1]:
    for i in range(1, len(arr)-1):
        sum += (arr[0]-arr[i])
else:
    for i in range(1, len(arr)-1):
        sum += (arr[len(arr)-1]-arr[i])

print(sum)
