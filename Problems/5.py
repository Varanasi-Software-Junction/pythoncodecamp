a="sAcHin raMEsh TenDUlkar"#Sachin Ramesh Tendulkar
#a= a.title()
#a = a.upper()
b=""
for i in range(len(a)):
    if i == 0:
         b += a[i].upper()
    elif ord(a[i-1]) == 32:
        b += a[i].upper()
    else:
        b += a[i].lower()
print(b)



