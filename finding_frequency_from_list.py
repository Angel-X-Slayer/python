## Find the element with 2nd largest frequency in the array.
## If there are more than one element with 2nd largest frequency then print the minimum of them.


import collections
a=[1,3,2,4,2,1,1,3,2,1,4,5,3]
freq={}
freq=collections.Counter(a)
arr=list(set(freq.values()))
op1=[]
for i in freq.keys():
    if freq[i]==arr[len(arr)-2]: ## we substract "2" because we want the 2nd largest.
        op1.append(i)
print(min(op1))

# print(arr)
