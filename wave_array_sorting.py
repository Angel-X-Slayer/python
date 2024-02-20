def swap(ki, lj):
    temp = ki
    ki = lj
    lj = temp
    return (ki, lj)


arr = list(map(int, input("enter the elements :").split(",")))
arr.sort()
# for i in range(1, len(arr)-1, 2):  ##   Greater--smaller--greater--smaller.......
for i in range(0, len(arr)-1, 2):  # Smaller--greater--smaller--greater.......
    k, l = swap(arr[i], arr[i+1])
    arr[i] = k
    arr[i+1] = l
print("the wave array is :", arr)
