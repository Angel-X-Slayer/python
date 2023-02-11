def check(a,p,n):
    for i in (a):
        if(i>=0):
            p+=1
        else:
            n+=1

    print(f"there are {p} positive numbers in the list")
    print(f"there are {n} negetive numbers is the list")



m=int(input("enter how many number you will give me :"))
a=[]
p=0
n=0
for i in range(m):
    k=int(input("enter the number :"))
    a.append(k)
check(a,p,n)

