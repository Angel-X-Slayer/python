def permutation(str, prm, idx, arr):
    if (len(str) == 0):
        print(prm)

    for i in range(len(str)):
        current = str[i]
        newstr = str[0:i]+str[i+1:]
        permutation(newstr, prm+current, idx+1, arr)


arr = []
permutation("ABCDE", "", 0, arr)
