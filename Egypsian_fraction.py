########################  RECURSION METHOD  ###########################



import math

def egypsian_fraction(nr,dr):
    if dr>nr and nr!=0:
        c=math.ceil(dr / nr)
        # print("1/{0} +",format(c),end="")
        print(f"1/{c} +",end=" ")
        nr=(c*nr)-dr
        dr=c*dr
        egypsian_fraction(nr,dr)
        
nr=47
dr=56
# egypsian_fraction(nr,dr)




######################  GREEDY METHOD  ########################




def egypsian_fraction_greedy(nr,dr):
    a=[]
    while dr>nr and nr!=0:
        c=math.ceil(dr/nr)
        a.append(c)
        nr=(c*nr)-dr
        dr=c*dr
    l=len(a)        
    for i in range(l):
        if i!=(l-1):
            print(f"1/{a[i]} +",end=" ")
        else:
            print(f"1/{a[i]}",end=" ")


nr=6
dr=14
egypsian_fraction_greedy(nr,dr)