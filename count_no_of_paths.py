def count_paths(i, j, row, coloumn):
    if ((i == row) and (j == coloumn)):
        return (0)
    if ((i == row-1) or (j == coloumn-1)):
        return (1)
    right = count_paths(i, j+1, row, coloumn)
    down = count_paths(i+1, j, row, coloumn)
    return (right+down)


r = int(input("enter number of row : "))
c = int(input("enter column :"))
op = count_paths(0, 0, r, c)
print(f"there are {op} number of paths")
