rows = 3

for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    

for i in range(rows + 1, 0, -1):
    for j in range(0, i - 2):
        print("*", end=' ')
    

# for i in range(4,0,-1):
#     print(i)