## ----------METHOD 1------------##

# a = "12423564233myname1232345isishan11223322"
# alp = ""
# dig = ""
# for i in a:
#     if i.isalpha():
#         alp += i
#     else:
#         dig += i
# op = alp+" "+dig
# print(op)


## ----------METHOD 2------------##

a = "12423564233myname1232345isishan11223322"
dig = []
alp = []
dig1 = []
k = 0
l = ""
for i in range(len(a)):
    if ord(a[i]) in range(48, 58):
        # if a[i]=="1" or a[i]=="2" or a[i]=="3" or a[i]=="4" or a[i]=="5" or a[i]=="6":
        dig.append(a[i])
    else:
        alp.append(a[i])
for i in range(len(dig)):
    dig1.append(int(dig[i]))
for i in range(len(dig1)):
    k = k*10+dig1[i]
for i in range(len(alp)):
    l += alp[i]

opt = []
opt.append(l)
opt.append(k)
print(opt)
