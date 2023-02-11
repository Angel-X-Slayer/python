import matplotlib.pyplot as plt
def bar(number):
    oo=0
    ee=0
    aa=0
    bb=0
    cc=0
    dd=0
    ff=0
    for i in range(len(number)):
        if number[i]<=100 and number[i]>=90:
            oo+=1
        elif number[i]<=89 and number[i]>=80:
            ee+=1
        elif number[i]<=79 and number[i]>=70:
            aa+=1
        elif number[i]<=69 and number[i]>=60:
            bb+=1
        elif number[i]<=59 and number[i]>=50:
            cc+=1
        elif number[i]<=49 and number[i]>=40:
            dd+=1
        else:
            ff+=1
    x=["O","E","A","B","C","D","F"]
    h=[500,400,330,450,600,510,700]
    plt.xlabel("Grade")
    plt.ylabel("Students Enrolled")
    plt.title("Grade Card")
    plt.show()
number=[100,100,56,78,99,80,72,72,88,66,54,49,49,40,33,22,12]
bar(number)

