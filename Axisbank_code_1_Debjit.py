def calculation(i, j, arr):
    t = j
    temp = 0
    while i <= t:
        temp += arr[i][j]
        i += 1
        j -= 1
    return (temp)


def takeinputs(arr):
    i = 0
    j = len(arr)-1
    op = []
    while (j > -1):
        k = calculation(i, j, arr)
        op.append(k)
        j -= 1
    print(min(op))


n = int(input())
ip = []
for i in range(n):
    arr = list(map(int, input().split(",")))
    ip.append(arr)
takeinputs(ip)


# def calculation(i, j, arr):
#     t = j
#     temp = 0
#     while i <= t:
#         temp += arr[i][j]
#         i += 1
#         j -= 1
#     return (temp)

#     pass


# def takeinputs(arr):
#     i = 0
#     j = len(arr)-1
#     op = []
#     while (j > -1):
#         k = calculation(i, j, arr)
#         op.append(k)
#         j -= 1
#     print(min(op))


# arr = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]
# takeinputs(arr)
