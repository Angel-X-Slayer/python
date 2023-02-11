from os import sep


def solution(arr,arr1,div1,c):
    rem=[]
    if len(arr)==len(div1):
        print(*arr[1:],sep="")
        
    else:
        for i in range(len(arr)):
            if arr[0]==0:
                arr.pop(0)
            else:
                break
        for i in range(len(div1)):
            if arr[i]==div1[i]:
                rem.append(0)
                c+=1
            else:
                rem.append(1)
                c+=1
        for i in range(c,len(arr1),1):
            rem.append(arr1[i])
        solution(rem,arr1,div1,c)

arr1=[]
# arr=[]
# div1=[]



arr=list(map(int,input("enter data : ").split(' ')))
div1=list(map(int,input("enter divisor : ").split(' ')))




# array1=list(int(input("enter data : ")))
# division1=list(int(input("enter divisior :")))
# # array1=list(array1)
# # division1=list(division1)
# for i in array1:
#     arr.append(i)
# for j in division1:
#     div1.append(j)



for i in range(len(div1)-1):
    arr.append(0)
for i in arr:
    arr1.append(i)

c=0


# print(arr)
# print(div1)

        

solution(arr,arr1,div1,c)








# n=input("enter the number :")
# for i in n:
#     arr.append(i)
# div=input("enter the divisor :")
# for i in div:
#     div1.append(i)
# for i in range(len(arr)):
#     arr1.append(arr[i])




# arr=[]
# div1=[]
# k=list(int(input("emter the numbert : ")))
# k=[1,1,0,1,1,1,1]

# # for i in k:
# #     arr.append(i)
# print(k)
# # div=[1,1,0,1]
# div=list(map.int(input("enter the divisor :")))
# # for i in div:
# #     div1.append(i)
# print(div)
# i=1
# while i<(len(div)):
#     k.append(0)
#     i+=1
# print(k)
# k1=k
# print(k1)
# c=0