product = 1
n = 9
x = 2
# Raise x to the power n
xseq = x
while n > 0:
    if n % 2 != 0:
        product = product * xseq
    print("N % 2", n % 2, "Product", product, ", xseq", xseq)
    n = n // 2

    xseq = xseq * xseq
print("Answer=", product)
