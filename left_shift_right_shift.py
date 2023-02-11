def rotateLeft_right(d, arr):
    n=len(arr)
    ##left shift
    arr1=arr[d:]+arr[:d]
    ##right shift
    arr2=arr[n-d:]+arr[:n-d]
    return(arr1,arr2)

if __name__=="__main__":
    # arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    arr=[1,2,3,4,5,6]
    d=5

    print(rotateLeft_right(d,arr))

