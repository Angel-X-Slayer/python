def min_jump(arr):
    reahcable = 0
    furthest_jump = 0
    desti = len(arr)-1
    total = 0
    if len(arr) == 1:
        return (0)
    if arr[0] != 1:
        for i, x in enumerate(arr):
            reahcable = max(reahcable, (i+x))
            if i <= reahcable:
                furthest_jump = reahcable
                total += 1

                if reahcable >= desti:
                    return (total)
    else:
        for i, x in enumerate(arr):
            reahcable = max(reahcable, (i+x))
            if i <= reahcable:
                furthest_jump = reahcable
                total += 1

                if reahcable >= desti:
                    return (total-1)

    return (total)


# arr = [2, 3, 1, 1, 4]
# arr = [1]

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# print(max(arr[0:5]))
print(min_jump(arr))
