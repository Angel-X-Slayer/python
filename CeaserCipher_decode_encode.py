class CeaserCipher:
    def __init__(self,shift):
        decode=[None]*26
        encode=[None]*26
        for i in range(26):
            encode[i]=chr((i+shift)%26+ord('A'))
            decode[i]=chr((i-shift)%26+ord('A'))
        self.forw=''.join(encode)
        self.backw=''.join(decode)
        # print(''.join(encode))
        # print(''.join(decode))
    def encoding(self,msg):
        return self.transform(msg,self.forw)
    def decoding(self,msg):
        return self.transform(msg,self.backw)
    def transform(self,msg,code):
        msg=list(msg)
        for i in range(len(msg)):
            if msg[i].isupper():
                j=ord(msg[i])-ord('A')
                msg[i]=code[j]
        return(''.join(msg))
if __name__=="__main__":
    s=int(input("enter the shift value :"))
    cpr=CeaserCipher(s)
    message=input("enter the message :")
    coded=cpr.encoding(message)
    print("code is :",coded)
    ans=cpr.decoding(coded)
    print("the message is :",ans)

