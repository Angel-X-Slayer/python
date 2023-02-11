def freqn(arr):
    freq={}
    for i in arr:
        if i not in freq.keys():
            freq[i]=1
        else:
            freq[i]+=1
    
    # for i in freq.keys():
    #     print(f"{i} {freq[i]}")
if __name__=="__main__":
    arr=list(map(int,input("enter the values :").split(",")))
    freqn(arr)
