arr = [0, 10, 2, -10, -20]
# arr = [1, 2, 3, 4, 5]
arr = sorted(arr)
counter = 0
# print(arr)
for i in range(len(arr)-1):
    if arr[i] < 0:
        pass
    elif arr[i] == 0:
        t = arr[i+1]-arr[i]
        if t != 1:
            print(1)
            counter += 1
            break
        else:
            continue
    elif arr[i] > 0:
        if arr[i+1] != arr[i]+1:
            print(arr[i]+1)
            counter += 1
            break
        else:
            continue

if counter == 0:
    print("No missing +ve element")
