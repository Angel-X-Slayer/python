def recur_sum(n):
   if n<=1:
       print(n)
    
   else:
       s=int(n + recur_sum(n-1))
       print(s)

# change this value for a different result
num=int(input("Enter the linit :"))

recur_sum(num)