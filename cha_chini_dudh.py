# def get_com():
#     pass



# if __name__=="__main__":
#     testcaseno=int(input("enter the number of the test case :"))
#     for i in range(testcaseno):
#         fistline=list(map,int(input("enter the first line :").split(" ")))

"""Starter Code for Milk Tea CC Problem"""

# Complete the count_complaints function
from numpy import array


def change_forbidden(n):
  sum=0
  a=[]
  while(n!=0):
    r=int(n%10)
    n=int(n/10)
    a.append(r)
  for i in range(len(a)):
    k=pow(2,i)*a[i]
    sum+=k
  return(sum)
def sum_of_digits(n):
  n=int(n)
  sum=0
  while n!=0:
    r=int(n%10)
    n=int(n/10)
    sum=sum+r
  # print(sum)
  return sum
def count_complaints(preferences, forbiddens,num_options):
  print(forbiddens)
  arr=[]
  complaints = 0
  binaryno=pow(2,num_options)-1
  arr1=[]
  #forbiddens array theke alada alada kore decimal kore onno 1 ta array te
  #store kore sei array rr element gulo k if ee i er sathe test korte hbe
  for i in forbiddens:
    k=int(forbiddens[i])
    s=change_forbidden(k)
    arr1.append(s)
  print(s)
  for i in range(binaryno+1):
      # bnr = bin(i).replace('0b','')
      sum=0
      if i not in arr1:
        # print("entering if")

        # x = bnr[::-1] #this reverses an array
        bnr = bin(i).replace('0b','')
        x = bnr[::-1]
        while len(x) < num_options:
          # arr=[]
          x += '0'
        bnr = x[::-1]
        for k in preferences:
          
          # print(bnr,k)
        
          y = int(bnr, 2)^int(k,2)
          m=(bin(y).replace('0b','').zfill(len(bnr)))
          

          m=sum_of_digits(m)
          sum+=m
          


      
        arr.append(sum)
      else:
        pass
  
  print(min(arr))


          
    #   if len(binar)<num_options:
    #       k=num_options-len(binar)




  # TODO: Add logic to count the number of complaints
  return complaints

if __name__ == '__main__':
  # Read number of test cases
  num_cases = int(input())

  for tc in range(1, num_cases + 1):
    # Read number of friends, number of forbidden teas, and number of options
    num_friends, num_forbidden, num_options = map(int, input().split())

    # Read the friends' preferences
    preferences = [input() for _ in range(num_friends)]


    # Read the forbidden teas
    forbiddens = [input() for _ in range(num_forbidden)]
    num_options=int(num_options)
    # print(type(forbiddens))
    # print(preferences)
    # forbiddens=int(forbiddens)
    # print(forbiddens)
    # print(num_forbidden)
    # binaryno=pow(2,num_options)-1
    # print(binaryno)

    # print("Case #%d: %d" % (tc, count_complaints(preferences, num_forbiddens,num_options)))
    count_complaints(preferences,forbiddens,num_options)
