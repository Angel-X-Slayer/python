from collections import Counter
def find_prime(num):
  if num==1:
    return False
  elif num==2:
    return True
  else:
    for i in range(2,num):
      if num%i==0:
        return False
    return True
def find_bots(arr):
  op1=0
  
  op=[]
  for i in arr:
    k=[]
    l1=dict(Counter(i))
    for j in range(0,len(i),2):
      k.append(i[j])
    l2=dict(Counter(k))
    k1=len(l2.keys())
    op1=find_prime(k1)
    if op1==True:
        op.append(1)
    else:
        op.append(0)
  return(op)




arr=["abcdef","pqrs","xyzuvabb","aaaaaa"]
##arr=["foo", "bab"]
##arr=["zkfcowyvgneobcyay","rekorku","sbokgmealjqqhcwebs","yshkw"]
k1=find_bots(arr)
print(k1)
