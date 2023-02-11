# a=[2,16]
# b=[]
# c=[]
# for i in range(len(a)):
#     b.append(a[i])
#     while a[i]!=0:
#         a[i]=int(a[i]/2)
#         b.append(a[i])
    
#     c+=b
#     b=[]

# c.sort()
# # for i in range
# # for i in range(len(c)):
# #     if c[i]==0:
# #         c.remove(c[i])

# print(c)

import numpy as np
a=[2,16]
b=[]
c=[]
for i in range(len(a)):
    b.append(a[i])
    while a[i]!=0:
        a[i]=int(a[i]/2)
        b.append(a[i])
    
    c+=b
    b=[]

c.sort()
