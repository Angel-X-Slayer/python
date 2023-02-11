points={'A+':4.0,'A':4.0,'A-':3.67,'B+':3.33,'B':3.0,'B-':2.67,'C+':2.22,'C':2.0,'C-':1.67,'D+':1.33,'D':1.0,'F':0.0}
num_cources=0
total_points=0
done=False
while not done:
    grade=input()
    if grade=='':
        done=True
    elif grade not in points:
        print("unknown grade '{0}' being ignored".format(grade))
    else:
        num_cources+=1
        total_points+=points[grade]
if num_cources>0:
    print('ypur gpa is {0:.3}'.format(total_points/num_cources))