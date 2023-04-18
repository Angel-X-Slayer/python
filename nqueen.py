# global N
# N = int(input())
# board = [[0]*N for _ in range(N)]

# def is_attack(i, j):
#     #checking if there is a queen in row or column
#     for k in range(0,N):
#         if board[i][k]==1 or board[k][j]==1:
#             return True
#     #checking diagonals
#     for k in range(0,N):
#         for l in range(0,N):
#             if (k+l==i+j) or (k-l==i-j):
#                 if board[k][l]==1:
#                     return True
#     return False

# def N_queen(col):
#     #if col is 0, solution found
#     if col<0:
#         print("enter legit value")
#         return True
#     for i in range(0,N):
#         for j in range(0,N):
#             '''checking if we can place a queen here or not
#             queen will not be placed if the place is being attacked
#             or already occupied'''
#             if (not(is_attack(i,j))) and (board[i][j]!=1):
#                 board[i][j] = 1
#                 #recursion
#                 #wether we can put the next queen with this arrangment or not
#                 if N_queen(col-1)==True:
#                     return True
#                 board[i][j] = 0

#     return False

# N_queen(N)
# for i in board:
#     print (i)

def isSafe(board, row, col):
    for i in range(len(board[0])):  # vertical check
        if board[i][col] == "Q":
            return False
    for j in range(len(board[0])):  # horizontal check
        if board[row][j] == "Q":
            return False
    # for i, j in range(len(board[0])), range(len(board[0])):
    #     if board[i-1][j-1] == "Q":
    #         return False
    # for i, j in range(len(board[0])), range(len(board[0])):
    #     if board[i-1][j+1] == "Q":
    #         return False
    # for i, j in range(len(board[0])), range(len(board[0])):
    #     if board[i+1][j-1] == "Q":
    #         return False
    # for i, j in range(len(board[0])), range(len(board[0])):
    #     if board[i+1][j+1] == "Q":
    #         return False
    # for i in range(len(board[0])):
    #     for j in range(len(board[0])):
    #         if i+j == row+col or i-j == row-col:
    #             return False
    # for r in range(r, -1, -1):
    #     for c in range(c, -1, -1):
    #         if board[row][col] == board[r][c] and board[row][col] == "Q":
    #             return False
    r = row
    c = col
    while (r-1 > 0 and c-1 > 0):
        if board[r-1][c-1] == "Q":
            return False
        else:
            c -= 1
            r -= 1

    r = row
    c = col
    while (r-1 < len(board[0]) and c-1 < len(board[0])):
        if board[r-1][c-1] == "Q":
            return False
        else:
            c += 1
            r += 1

    r = row
    c = col
    while (r-1 > 0 and c-1 < len(board[0])):
        if board[r-1][c-1] == "Q":
            return False
        else:
            c += 1
            r -= 1

    r = row
    c = col
    while (r-1 < len(board[0]) and c-1 > 0):
        if board[r-1][c-1] == "Q":
            return False
        else:
            c -= 1
            r += 1
    # for r in range(len(board[0])):
    #     for c in range(c, -1, -1):
    #         if board[row][col] == board[r][c] and board[row][col] == "Q":
    #             return False

    # for r in range(r, -1, -1):
    #     for c in range(len(board[0])):
    #         if board[row][col] == board[r][c] and board[row][col] == "Q":
    #             return False

    # for r in range(len(board[0])):
    #     for c in range(len(board[0])):
    #         if board[row][col] == board[r][c] and board[row][col] == "Q":
    #             return False
    return True


def nqueen(board, col, mainboard):
    if (col == len(board[0])):
        mainboard.append(board)
        # i=row

        # col=column
    for row in range(len(board[0])):
        if isSafe(board, row, col):
            board[row][col] = "Q"
            nqueen(board, col+1, mainboard)
            board[row][col] = "."


n = int(input("enter the lenth of the chess board :"))
board = [[""]*n]*n
mainboard = []
op = nqueen(board, 0, mainboard)
print(op)
