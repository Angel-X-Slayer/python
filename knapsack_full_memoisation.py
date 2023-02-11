def knapsack_memo(w1,v1,w,n): ## w1=weight array, v1=value array, W=max weight of knapsack,N=len of weight array, t=used matrix
    t=[[-1 for i in range(n+1)]for j in range(w+1)]

    if w==0 or n==0:
        return(0)    
    if t[w][n]!=-1:
        return(t[w][n])
    else:
        if w1[n-1]<=w:
            t[w][n]=max(v1[n-1]+knapsack_memo(w1,v1,w-w1[n-1],n-1),knapsack_memo(w1,v1,w,n-1))
            return(t[w][n])
        elif w1[n-1]>w:
            t[w][n]=knapsack_memo(w1,v1,w,n-1)
            return t[w][n]


w1=[1,3,4,5]
v1=[1,4,5,7]
w=7
n=len(w1)

print(knapsack_memo(w1,v1,w,n))
