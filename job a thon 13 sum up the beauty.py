from collections import Counter


def sublists(lst):
    sublists_list = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublists_list.append(lst[i:j])
    return sublists_list


# arr = [1, 1]
arr = [2, 4, 2]
sub = sublists(arr)
print(sub)
track = 0
for i in sub:
    dic = Counter(i)
    for i in dic.values():
        if i == 1:
            track += 1
        else:
            pass

print(track)
