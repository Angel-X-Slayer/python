class complete:
    def __init__(self,str1,str2):
        self.str1=str1
        self.str2=str2

    def if_complete(self):
        j=0
        for i in self.str2:
            if i in self.str1:
                k=self.str1.index(i)
                self.str1=self.str1[k+1:]
                j+=1
                    
            else:
                j=-1

        if j==-1:
            print("false")
        else:
            print("true")

str1=input()  ##partial=str1
str2=input()  ##full=str2
obj=complete(str1,str2)
obj.if_complete()

 