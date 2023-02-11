s=input("enter the string:")
l=len(s)
i=0
j=l-1
m=3
while i<j:
    while not s[i].isalnum() and i<j:
        i+=1
    while not s[j].isalnum() and i<j:
        j-=1
    if s[i].lower()!=s[j].lower():
        m=-1
        break
    i+=1
    j-=1
if m==3:
    print("the string is palindrome")
else:
    print("the string is not palindrome")