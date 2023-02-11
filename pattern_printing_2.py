#je kono 1 ta loop k comment out kore dile opor vag ta paoa jabe,serm vabei kora a6e maal ta
#jdi por por chao tahle 1st er loop mane jeta cmmnt out kora a6e seta k cmmnt in korlei khela hbe 
n=int(input("Enter the number of row : "))
# #for i in range(jota por por chao tota likhe dao):
# for i in range(n):
#         print(" "*(n-1-i),end="")
#         print("*"*(i+1),end="")
#         print("*"*i)
for i in range(n):
        print(" "*(i+1),end="")
        print("*"*(n-1-i),end="")
        print("*"*(n-2-i))

