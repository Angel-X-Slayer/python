##    FOR FINDING A SPECIFIC CATALAN NUMBER    ##



def catalan(n):
    remp=[0]*100
    remp[0]=1
    remp[1]=1
    # print(remp)
    for i in range(2,n+1):
        for j in range(0,i+1):
            remp[i]+=remp[j]*remp[i-j-1]
    print(remp[n])
n=3
catalan(n)



################################################

##********************************************##**********************************************##************************************

###############################################



##    FOR CREATING A CATALAN SERISE    ##



# def catalan(n):
#     remp=[0]*(n+1)
#     remp[0]=1
#     remp[1]=1
#     # print(remp)
#     for i in range(2,n+1):
#         for j in range(0,i+1):
#             remp[i]+=remp[j]*remp[i-j-1]
#     print(remp)
# n=10
# catalan(n)



##############################################