k="my namely is ishanly mukherjee"
arr=k.split()
arr1=[]
for i in arr:
    if i[len(i)-1]=="y" and i[len(i)-2]=="l":
        arr1.append(i[:len(i)-2])
    else:
        arr1.append(i)
x=" ".join(arr1)
print(x)


