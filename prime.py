n= 11
flag =1 # is prime number
for i in range(2,int((n)**(1/2))+1):
    if n%i == 0:
        flag = 0 # is not primer number
        break
if flag == 1:
    print("given number is a prime number")
else:
    print("Given number is not a prime number")