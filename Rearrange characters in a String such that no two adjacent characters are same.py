# check permutattion_of_string.py for more details.
# i just take all the possible combinations and pass them under the if statement, to
# check if all the adjecent letters are differenet, then appended into a list.
# then typecasted the list into set, then printed the set.


def check(prm):
    c = 0
    for i in range(len(prm)-1):
        if prm[i] != prm[i+1]:
            c += 1
        else:
            pass
    if c == len(prm)-1:
        return (True)
    else:
        return (False)


def permutation(str, prm, idx, arr):
    if (len(str) == 0):
        k = check(prm)
        if k == True:
            arr.append(prm)

    for i in range(len(str)):
        current = str[i]
        newstr = str[0:i]+str[i+1:]
        permutation(newstr, prm+current, idx+1, arr)

    return (arr)


arr = []
op = permutation("aaaaaabbbbc", "", 0, arr=[])
op = set(op)
if len(op) > 0:
    for i in op:
        print(i, end="\n")
else:
    print("No string found")
