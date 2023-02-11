def knapsack(w1,v1,W,N): ## w1=weight array, v1=value array, W=max weight of knapsack,N=len of weight array
    if N==0 or W==0:
        return (0) 
    elif w1[N-1]<=W:
        return(max((v1[N-1]+knapsack(w1,v1,W-w1[N-1],N-1)),knapsack(w1,v1,W,N-1)))
    else:
        return(knapsack(w1,v1,W,N-1))

w1=[1,3,4,5]
v1=[1,4,5,7]
W=7
N=len(w1)
print(knapsack(w1,v1,W,N))

