def isSafe(n, row, col):
    # vertical
    for i in range(0, n):
        if result[i][col] == "Q":
            return False
        else:
            pass
    # horizontal
    for j in range(0, n):
        if result[row][j] == "Q":
            return False
        else:
            pass

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if result[i][j] == "Q":
            return False
        else:
            pass

    for i, j in zip(range(row, n), range(col, -1, -1)):
        if result[i][j] == "Q":
            return False
        else:
            pass

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if result[i][j] == "Q":
            return False
        else:
            pass

    for i, j in zip(range(row, n), range(col, n)):
        if result[i][j] == "Q":
            return False
        else:
            pass
    return True


def nqueen(n, result, col):
    if n == col:
        print(result)
        return
    else:
        for i in range(n):
            if isSafe(n, i, col):
                result[i][col] = "Q"
                # Going in the next columbn t oplace the queen
                nqueen(n, result, col+1)
                result[i][col] = "."  # Backtracking stage


n = int(input("enter the value of n:"))
result = [['.'] * n for _ in range(n)]
nqueen(n, result, 0)
