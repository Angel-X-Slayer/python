arr2 = [11, 1, 13, 21, 3, 7]
arr1 = [11, 3, 7, 1]
t = 0
if len(arr2) > len(arr1):

    for i in arr1:
        if i in arr2:
            t += 1
            continue
        else:
            print("no subset present")
            break
    if t == len(arr1):
        print("arr1 is a subset of arr2")
elif len(arr2) < len(arr1):
    for i in arr2:
        if i in arr1:
            t += 1
            continue
        else:
            print("no subset present")
            break
    if t == len(arr2):
        print("arr2 is a subset of arr1")
else:
    for i in arr2:
        if i in arr1:
            t += 1
            continue
        else:
            print("no subset present")
            break
    if t == len(arr2):
        print("1st array is a superset of 2nd array")
