def revFib(x,y):
    while(y>0):
        t=x-y
        x=y
        y=t
        print(y, end=" ")
revFib(21,13)