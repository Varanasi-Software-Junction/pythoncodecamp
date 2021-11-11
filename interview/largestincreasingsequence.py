l = [10, 33, 3, 0]  # Input Array
n = len(l)
if n <= 0:
    print("No Array")
    exit(0)
print("Input Array ", l)
l = l + [l[n - 1] - 1]  # Add an extra element to the array to break the last sequence

n = n + 1
maxlength = 0  # initialize maxlnght so that it gets replaced the first time
maxsequence = []  # Max sequence is blank initially
currentseq = [l[0]]  # Start current seq with first element

for i in range(1, n):  # Loop from 1
    prev = l[i - 1]  # Element just before current one
    current = l[i]  # The current element
    if current >= prev:  # Current > Prev add new element to seq
        currentseq = currentseq + [current]
    else:  # Increasing sequence broken
        if (len(currentseq)) > maxlength:  # Length of current sequence greater than largest found thus far
            maxlength = len(currentseq)
            maxsequence = currentseq.copy()
        currentseq = [current]
print("Max Sequence", maxsequence)
