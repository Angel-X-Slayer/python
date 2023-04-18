from collections import *


def freqn(arr):
    dic = dict(Counter(arr))
    arr1 = sorted(arr)
    print(arr1)
    # freq={}
    # for i in arr:
    #     if i not in freq.keys():
    #         freq[i]=1
    #     else:
    #         freq[i]+=1

    # for i in freq.keys():
    #     print(f"{i} {freq[i]}")
    arr1 = sorted(arr1, key=lambda x: dic[x], reverse=True)
    print(arr1)


if __name__ == "__main__":
    arr = list(map(int, input("enter the values :").split(" ")))
    freqn(arr)
