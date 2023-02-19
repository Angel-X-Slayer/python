def find_prime(j):
    for i in range(2,j):
        if j%i==0:
            return(False)
    return(True)


def find_finite_prime(a,b,k):
    count=0
    check=0
    for i in range(a+1,b):
        if find_prime(i)==True:
            count+=1
            if count==k:
                check=1
                break
        else:
            pass
    if check==1:
        print(i+1)
    else:
        print(-1)
        


a=int(input())
b=int(input())
k=int(input())
find_finite_prime(a,b,k)