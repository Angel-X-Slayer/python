import collections
import string
op = ""
str = "welcome to geeksforgeeks"
dic = dict(collections.Counter(str))
print(dic)
dic = dict(sorted(dic.items(), key=lambda x: x[0]))
# print(dic)

for i in string.ascii_lowercase:
    if i in dic.keys():
        pass
    else:
        op += i

print(op)
