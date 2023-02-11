
lst1=[]
lst2=[]
lst3=[]
lst4=["sope","shampoo","conditionar","comb","brush","toothpest","toung cleaner","powder dust"]
n=input("press c to go to calculator or press anything to search : ")
flag=0
if(n=='c'):
    sum=0
    while(True):
        item=input("Enter the name of the product or to quit press e : \n")
        if(item != 'e'):
            lst1.append(item)
            quantity=int(input(f"enter how many you took {item} : \n"))
            lst3.append(quantity)
            price=int(input(f"enter the price of each {item} : \n"))
            asli_price=price*quantity
            lst2.append(asli_price)
            sum=sum+asli_price
            print(f"Price till now {sum}")
        else:
            print(": Mahaprabhu stores :")
            lenth=len(lst1)
            for i in range(lenth):
                print(f"{lst1[i]} X {lst3[i]} :: {lst2[i]}")
            print(f"Total billing amount is : Rs{sum}")
            break
else:
    search=input("enter the item to search : ")
    for i in range(len(lst4)):
        if(search==lst4[i]):
            flag=1
            break
    if(flag==0):
        print("The product is not present")
    else:
        print("product is present")
            