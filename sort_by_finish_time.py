from audioop import reverse
from posixpath import sep
from numpy import sort

def Activity_selection(f,s):
    a=[]
    n = len(f)
    if sum(f)==f[0]*n:
        print ("The following activities are selected ")
        i= 0
        a.append(i)
        for j in range(1,n):
            if s[j]>=f[i]:
                a.append(j)
                i=j
        print(len(a))
    else:

        print ("The following activities are selected ")
        # f=sort(f)
        s=sortbyfinish(f,s)
        # print(s)
        # print(f)
    # The first activity is always selected
        i = 0
        a.append(i)
 
    # Consider rest of the activities
        for j in range(1,n):
 
        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
            if s[j] >= f[i]:
            # print (j,end=' ')
                a.append(j)
                i = j
    # pass
        # print(a)
        for i in a:
            print(i+1,end=" ")


def sortbyfinish(f,s):
    zipped_pairs = zip(f,s)
    # f=sort(f)
    # print(zipped_pairs)
    z = [x for _, x in sorted(zipped_pairs)]
    f=sort(f)
    # print(*z,sep=" ")
    # return(z)
    return(z)
    # print(f)
    # print(*(sort(f)),sep=" ")
 
# s=[1, 3, 2, 5]
# f=[2, 4, 3, 6]

# s = [1 , 3 , 0 ,8 , 5, 5]
# f = [2 , 4 , 6 ,9 , 7, 9]

s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]

# s=[5,3]
# f=[7,5]

Activity_selection(f,s)
# sortbyfinish(f,s)










#################### GFG PROBLEM SOLUTION ##########################


# def activitySelection(self,n,s,f):
#         a=[]
#         n = len(f)
#         if sum(f)==f[0]*n:
#             i= 0
#             a.append(i)
#             for j in range(1,n):
#                 if s[j]>=f[i]:
#                     a.append(j)
#                     i=j
#             return(len(a))
#         else:
#             s=sortbyfinish(f,s)
#             f.sort()
#     # The first activity is always selected
#             i = 0
#             a.append(i)
 
#     # Consider rest of the activities
#             for j in range(n):
 
#         # If this activity has start time greater than
#         # or equal to the finish time of previously
#         # selected activity, then select it
#                 if s[j] >= f[i]:
#                 # print (j,end=' ')
#                     a.append(j)
#                     i = j
#     # pass
#         return(len(a))


# def sortbyfinish(f,s):
#     zipped_pairs = zip(f,s)
#     # print(zipped_pairs)
#     z = [x for _, x in sorted(zipped_pairs)]
     
#     # print(*z,sep=" ")
#     return(z)
