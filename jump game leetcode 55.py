'''
this code checks if a person can jump from initial point to final point in the arr'''


# def can_jump(arr):
#     right = 0
#     for i, x in enumerate(arr):
#         if i > right:
#             return False
#         right = max(right, i+x)
#     return True

def can_jump(arr):
    reachable = 0
    for idx, val in enumerate(arr):
        if reachable < idx:
            return False
        reachable = max(reachable, (idx+val))
    return (True)


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(can_jump(arr))
