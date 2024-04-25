m = 8
b = [1, 1, 2]
a = [2, 1, 1]
maxi = max(a)
idx = a.index(maxi)
if a[0] > b[0]:
    n = m//b[idx]
else:
    pass
print(n*a[idx])
