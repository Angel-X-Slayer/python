arr = [1, 4, 45, 6, 10, 8]
tar = 22
i = 0
j = 1
k = len(arr)-1
arr = sorted(arr)
for a in range(10000):
    if arr[i]+arr[j]+arr[k] == tar:
        print(arr[i], arr[j], arr[k])
        break
    elif arr[i]+arr[j]+arr[k] > tar:
        k -= 1
        continue
    elif arr[i]+arr[j]+arr[k] < tar:
        i += 1
        j += 1
        continue
