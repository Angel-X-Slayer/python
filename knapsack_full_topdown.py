def knapsack_topdown(w1,v1,w,n):
    t=[[(-1) for i in range(w+1)]for j in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if i==0 or j==0:
                t[i][j]=0
    for i in range(1,n+1):
        for j in range(1,w+1):
            if (w1[i-1]<=j):
                t[i][j]=max(v1[i-1]+t[i-1][j-w1[i-1]],t[i-1][j])
            else:
                t[i][j]=t[i-1][j]

## NOT COMPUPSORY,JST FOR FUN

    # for i in range(n+1):
    #     for j in range(w+1):
    #         print(t[i][j],end=" ")
    #     print()

## NOT COMPULSORY,JST FOR FUN

    return(t[n][w])


            




w1=[1,3,4,5]
v1=[1,4,5,7]
w=7
n=len(w1)

print(knapsack_topdown(w1,v1,w,n))