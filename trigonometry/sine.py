def sine(x):
    term = x
    n = 1
    error=0.00001
    total=0
    while abs(term)>error:
        total=total+term
        term=-(term*x*x)/(n+1*(n+2))
        n=n+2
    return total
print(sine(3.14))

