def tempunitchange(n):
    if(n=="1"):
        c=float(input("enter the celcious temp :"))
        f=((9*c)/5)+32
        print(f"the {c} equivalent in farenhite is {f}")
    else:
        f=float(input("enter the farenhite temp :"))
        c=((f-32)*5)/9
        print(f"the {f} equivalent in celcious is {c}")

print("              Welcome to the temparature change calculator")
print()
n=input("Enter 1 to change from cel to fer or press any to chnage from fer to cel :")
tempunitchange(n)


