n=int(input("enter the limyt : "))
for i in range(1,n+1):
    k=0
    if(i==1):
        print(1)
    else:
        for j in range(1,i+1):
            if(i%j==0):
                k+=1
        if(k==2):
            print(i)
            
