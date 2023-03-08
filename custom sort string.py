from collections import *
a = []
b = []
order = input(" enteer oredr :")
str = input("enter the string :")
dic = (dict(Counter(str)))
for i in order:
    if i in dic.keys():
        a.append(i*dic[i])
        dic.pop(i)
for i in dic.keys():
    a.append(i*dic[i])
print("".join(a))
