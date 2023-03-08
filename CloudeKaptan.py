str = input("enter the string: ")
k = (list(reversed(str)))
for i in k:
    if i == " ":
        k.remove(i)
for i in range(len(str)):
    if str[i] == " ":
        k.insert(i, " ")
print("".join(k))
