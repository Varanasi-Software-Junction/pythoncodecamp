a=[65,34,72,96,35,23]
a.sort()
choice=int(input("1 for smallest\n2 for largest :"))
if(choice==1):
    sm=int(input("which smallest element you want: "))
    print(a)
    print(sm,"smallest element is : ", a[sm-1])
if(choice==2):
    lr=int(input("which largest element you want: "))
    a.sort(reverse=True)
    print(a)
    print(lr,"Largest element is : ",a[lr-1])