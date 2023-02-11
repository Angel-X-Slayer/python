str=input()
op=[]
for i in str:
    if i.isnumeric():
        pass
    else:
        op.append(i)
print("".join(op))
