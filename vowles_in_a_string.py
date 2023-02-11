string=input("enter the string: ")
count=0
lc=string.lower()
for i in lc:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count+=1
print(f"there are {count} vowels in the given string")

