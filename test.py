# count=1
# str(count)
# a=count+1
# print(a)
# b="ll"
# needle="ll"
# if b==needle:
#     print("fucking yes")
# else:
#     print("fucking no")
# ress=b[0]+need
# c="the number is ="
# b=''
# b=b.join(('2',b))
# print(b)
# for i in range(-1,-7,-1):
#     print(i)


# def solve(A):
#     L = len(A)
#     if L<2: return 0
        
#     A_r = A[::-1]
        
#     for i in range(L):
#         if A_r[i:] == A[:L-i]:
#             return i
#     return L

# A="AABB"
# print(solve(A))

# s="panorama"
# print(s[2:6])
# s="ababbbababbbaba"
# s="PRAMIT"
# # s="aaaabaaa"
# i=0
# j=len(s)-1
# # print(i,j)
# print(s[i:j+1])
# print(s[j::-1])
# a=[1,2,3,4,5,6,7,8,9,0,11]
# for i in range(len(a)-1, -1,-1):
#     print(a[i])
# s="i am a boy"
# for i in range(len(s)-1,-1,-1):
#     print(s[i],end="")

# b=[]
# for i in range(len(a)):
#     # b[i]=a[i]
#     pass
#     # print(a[i],end="")
# print(type(b))
    # @param A : string
    # @return a strings
# def solve(A):
#     return ' '.join(A.strip().split()[::-1])
# a="i am a boy"
# print(solve(a))

# def solve1(A):
#     rev = A.split()
#     print(rev)
#     rev.reverse()
#     print(rev)
#     s = ' '
#     s = s.join(rev)
#     print(s)
# ##..................*************************..................##
# def solve2(A):
#     s=''
#     temp=''
#     i=len(A)-1
#     while i>-1:
#         if A[i]!=' ':
#             temp+=A[i]
#                 #print(temp)
#             i-=1 
#         if A[i]==' ':
#             s=s+temp[::-1]+A[i]
#             temp=''
#             i-=1
#     s=s+temp[::-1]
#     print(s)
# a="i am a boy"
# # solve1(a)
# solve2(a)


# for i in range(15):
#     bnr = bin(i).replace('0b','')
#     print(bnr)
# a=12345
# b=a[::-1]
# print(b)
# print(int(0b1101))
# bnr = bin(13).replace('0b','')
# print(bnr)
# if bnr==1101:
#     print(bnr)
# else:
#     print("exit")


# def change_forbidden(n):
#   a=[]
#   while(n!=0):
#     r=int(n%10)
#     n=int(n/10)
#     a.append(r)
#   print(a)
def change_forbidden(n):
  sum=0
  a=[]
  while(n!=0):
    r=int(n%10)
    n=int(n/10)
    a.append(r)
#   print(a)
  for i in range(len(a)):
    k=pow(2,i)*(a[i])
    sum+=k
  print(sum)
n=1000
change_forbidden(n)



# anm=12^0
# print(anm)




# txt = 0b0010
# txt=str(txt)

# x = bin(txt.zfill(8))

# print(x)




# i=56
# bnr = bin(i).replace('0b','')
# x = bnr[::-1]
# print(type(x))
# print(x)




# from dataclasses import replace


# bnr=bin(56).replace('0b','')
# k=bin(34).replace('0b','')
# # m=int(bnr, 2)
# # print(m)
# y = int(bnr, 2)^int(k,2)
# print(y)



y=8
bnr=[1,2,3,4,5]
m=(bin(y).replace('0b','').zfill(len(bnr)))
print(type(m))























