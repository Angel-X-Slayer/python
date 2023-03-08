from collections import *
a = []
b = []
first = 0
second = 0
inp = list(input())
for i in range(len(inp)):
    if inp[i] == "(":
        first += 1
        a.append(i)
    elif inp[i] == ")":
        second += 1
        b.append(i)
    else:
        pass
if first > second:
    k = first-second
    for i in range(k):
        for j in range(len(inp)):
            if inp[j] == "(":
                inp.pop(i)
                break
elif second > first:
    k = second-first
    for i in range(k):
        for j in range(len(inp)):
            if inp[j] == ")":
                inp.remove(inp[j])
                break
else:
    pass

print("".join(inp))
