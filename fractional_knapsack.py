profit=[10,5,15,7,6,18,3]
weight=[2,3,5,7,1,4,1]
ratio=[]
solution=0
bag_w=0
capacity=15
for i in range(len(profit)):
    ratio.append(profit[i]/weight[i])
# ratio.sort()
zipped=zip(ratio,profit)
zipped1=zip(ratio,weight)

# print(ratio)
# zipped1=zip(ratio,zipped)
p=[x1 for _, x1 in sorted(zipped)]
w=[x1 for _, x1 in sorted(zipped1)]
p.reverse()
w.reverse()
ratio=sorted(ratio,reverse=True)
for i in range(len(p)):
    if bag_w<=15:
        if 15-bag_w> w[i] :
            solution+=p[i]
            bag_w+=w[i]
        else:
            solution+=(p[i]*((15-bag_w)/w[i]))
            bag_w+=(w[i]*((15-bag_w)/w[i]))



# print(p)
# print(w)
# print(ratio)
print(solution)