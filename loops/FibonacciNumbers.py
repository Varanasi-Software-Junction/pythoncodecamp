"""
The Fibonacci number sequence starts with the numbers
0 and 1. All other numbers come by adding the previous 2
Thus the sequence goes
0,1,
Then 1,2,3,5,8,13,21,34 and so on
34= 21 + 13, 21=13 + 8, 13=8+5, 8= 5+3,,,


"""
a = 0  # 1st Fin no
b = 1  # 2nd fib no
n = 10  # no of Fib numbers to print
print(a, b, end=" ")  # Print the 1st two
for i in range(3, n + 1):  # Start from 3 because first 2 are already printed
    c = a + b  # Calculate new number
    print(c, end=" ")  # Print the new number
    a = b  # Advance a. Previous b becomes a for the next term
    b = c  # Previous c becomes b for next term
