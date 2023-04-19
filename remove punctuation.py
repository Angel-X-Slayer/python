punc = list(map(str, input().split(" ")))
# print(punc)
inp = input()
op = ""
for i in inp:
    if i in punc:
        pass
    else:
        op += i
print(op)
