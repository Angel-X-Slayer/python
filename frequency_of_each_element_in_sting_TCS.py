import collections
# freq1=()  ##can use freq1 as tuple 
freq1={}   ## can use freq1 as dictionary
str=input()
frqe=[]
vals=[]     ## vals is for VALUES in dictionary 
vals1=[]    ## vals1 is for KEYS in distionary
for i in str:
    frqe.append(str.count(i))
freq1=collections.Counter(str)
for i in freq1.values():
    vals.append(i)
for i in freq1.keys():
    vals1.append(i)
print(frqe)
print(freq1)
print(vals)
print(vals1)