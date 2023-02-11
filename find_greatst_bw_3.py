def greatest(num1,num2,num3):
    if(num1!=num2 and num2!=num3 and num3!=num1):
        if(num1>num2):
            if(num2>num3):
                ptint("the greatest number is :", num1)
            else:
                print("the greatest number is :", num3)
        else:
            if(num2>num3):
                print("the greatest number is :",num2)
            else:
                print("the greatest number is :", num3)
    else:
        print("All the numbers are equal")


n1=int(input("enter the first number :"))
n2=int(input("enter the second number :"))
n3=int(input("enter the third number :"))
greatest(n1,n2,n3)