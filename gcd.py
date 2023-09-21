# import math
# n=int(input())
# m=int(input())
# print(math.gcd(n,m))
result = [[".", ".", "."], ["Q", ".", "."], [".", ".", "."]]
print(result)
for i in range(3):
    if result[i][0] == "Q":
        print(i)
