############ Take all the numbers into an array and reshape the array using reshape the method #####################







# Activity = [[5, 9], [1, 2], [3, 4], [0, 6],[5, 7], [8, 9]]
# Activity = [['a', 2, 100],  # Job Array
#        ['b', 1, 19],
#        ['c', 2, 27],
#        ['d', 1, 25],
#        ['e', 3, 15]]
# Activity=[[1,2,100],[2,1,19],[3,2,27],
#         [4,1,25],[5,1,15]]
# Activity=[[1,4,20],[2,1,10],[3,1,40],
#         [4,1,30]]
import numpy as npp
# # from openpyxl import NUMPY


p=int(input("enter the number of rows :"))
a=[]

for i in range(p*3):
        k=int(input("enter the number :")) 
        a.append(k)
Activity=npp.reshape(a,(4,3))
Activity=list(Activity)
# print(Activity)
# from argparse import Action


# Activity=[[1,4,20],[2,1,10],[3,1,40],[4,1,30]]
n=len(Activity)
k=0
prof=0
# print(Activity)
Activity.sort(key = lambda x : x[2],reverse=True)
# print(Activity)
# print(Activity)
t=len(Activity[0])
profit=[False]*t
seq=[-1]*t
# for i in range(n):
#     for j in :
#            if Activity[i][2]>Activity[i+1][2]:
#                   if seq[Activity[i][1]]!=-1:
#                          seq[i+1]=
for i in range(len(Activity)):
 
        # Find a free slot for this job
        # (Note that we start from the
        # last possible slot)
        for j in range(min(t - 1, Activity[i][1] - 1), -1, -1):
 
            # Free slot found
            if profit[j] is False:
                profit[j] = True
                seq[j] = Activity[i][0]
                break
 
    # print the sequence
# print(*seq,sep=" ")
for i in seq:
    if i!=(-1):
        k+=1
for i in range(len(seq)):
    if seq[i]!=(-1):
        for j in range(len(Activity)):
            if seq[i]==Activity[j][0]:
                prof+=Activity[j][2]
    else:
        pass
print(k, prof)
