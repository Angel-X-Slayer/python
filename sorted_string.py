# s1="i am a cat"
# s2="i am a cat but i have dog"
# s1=s1.replace(" ","")
# s2=s2.replace(" ","")
# # s1=sorted(s1)
# # s2=sorted(s2)
# print(''.join(s1))
# print(''.join(s2))

def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(a,b)
a=12
b=90
swap(a,b)

