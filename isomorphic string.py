def areIsomorphic(str1,str2):
        if len(str1)!= len(str2):
            return False
        else:
            charCount = dict()
            c = "a"
            for i in range(len(str1)):
                if str1[i] in charCount:
                    c = charCount[str1[i]]
                    if c != str2[i]:
                        return False
                elif str2[i] not in charCount.values():
                    charCount[str1[i]] = str2[i]
                else:
                    return False
            return True      
str1="bgib"     
str2="ggik"
k=areIsomorphic(str1,str2)
if k==True:
    print("isomorphic")
else:
    print("not isomorphic")









# dic={'b': 5, 'g': 10, 'i': 3,'a': 7, 'o': 12, 'l': 1}
# dic1=dict(sorted(dic.items(), key=lambda kv:(kv[0], kv[1])))    ## sort dictionary by key
# dict2=dict(sorted(dic.items(), key=lambda kv:(kv[1], kv[0])))    ## sort dictionary by value
# print(dic)
# print(dic1)
# print(dict2)
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       