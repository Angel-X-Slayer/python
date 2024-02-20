from collections import Counter

arr = list(map(int, input("enter the elements").split(",")))
dic = Counter(arr)
dic = sorted(dic.items(), key=lambda x: x[1])
print(dic[len(dic)-1][0])
