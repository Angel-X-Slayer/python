n=7
capacity=[13,10,10,7,7,3,7]
capacity.sort()
sol=1
# print(capacity)
for i in range(len(capacity)):
    sol=sol*(capacity[i]-i)
    print(i)
print(sol)