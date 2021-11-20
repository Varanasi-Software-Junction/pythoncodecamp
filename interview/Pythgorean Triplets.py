# Program to find all Pythagorean Triplets up to  limit


"""
Pythagorean triplet is a three number sequence like 3,4 and 5,
where 3 squared + 4 squared = 5 squared
9 + 16 = 25
"""
loopruns = 0
count = 0
n = 100  # Set the limit
looplimit = int(((n * n) / 2) ** .5)
for i in range(1, looplimit + 1):  # Run a loop of i from 1 to the limit
    remaining = int((n * n - i * i) ** 0.5)
    for j in range(i + 1, remaining + 1):  # Run another loop of j from i+1 to the limit
        for k in range(j + 1, n + 1):  # Run  loop of k from j+1 to the limit
            loopruns += 1  # Count the number of times the loop runs. We will optimize it using this
            if i * i + j * j == k * k:  # Check if current combination is a Pythagorean Triplet
                count += 1  # If triplet found then increment the count
                print(count, ")", i, ",", j, ",", k, ', triplet is ', i * i, " + ", j * j, " = ",
                      k * k)  # Print the triplet with full info
print("Loop runs ", loopruns, "times")
# End Program
