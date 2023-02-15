global prefix
prefix=""

def printAllKLength(set1, k,prefix,count):
    l=len(set1)
    if k==0:
        # print(prefix)
        # count+=1
        # print(count)
        count.append(prefix)
        return
    
    
    for i in range(l):
        new=prefix+set1[i]
        printAllKLength(set1,k-1,new,count)

    return(count)


    pass
 
# Driver Code
if __name__ == "__main__":
     
    print("First Test")
    set1 = ['a', 'b','c']
    k = 5
    new=""
    count=[]
    arr=printAllKLength(set1, k,new,count)
    print(len(arr))
     
    # print("\nSecond Test")
    # set2 = ['a', 'b', 'c', 'd']
    # k = 1
    # printAllKLength(set2, k)