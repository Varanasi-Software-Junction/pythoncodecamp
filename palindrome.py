a=input("Enter the number")

flag =1# is palindrome
l= len(a)
i =0
j= len(a)-1
while i<len(a) and j>-1:
    if a[i]!=a[j]:
        flag = 0
        break

    i+=1
    j-=1

if flag == 1:
    print("Given number is Palindrome")
else:
    print("Not a palindrome")
