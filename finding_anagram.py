def anagram(s1,s2):
    m=3
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()
    his=dict()
    if len(s1)!=len(s2):
        m=-1
    else:
        for i in s1:
            if i in his:
                his[i]+=1
            else:
                his[i]=1

        for i in s2:
            if i in his:
                his[i]-=1
            else:
                his[i]=1
        

    for i in his.values():
        if i!=0:
            m=-1
            break
    if m==3:
        print("the strings are anagram")
    else:
        print("the strings are not palindrome")


s1=input("enter the string: ")
s2=input("enter the string: ")
anagram(s1,s2)
