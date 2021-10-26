duplicates = [1,2,2,3,3,3,1]  # The list whose duplicates are to be removed
n = len(duplicates)  # Get length of the list
print("List with duplicates ",duplicates)
duplicates = duplicates + [duplicates[n - 1] + 1]  # Add an extra element to the end with value 1 more than the last element so that the seequence breaks

n = n + 1
noduplicates = []

p1 = 0  # Start of the sequence
for i in range(1, n):
    if duplicates[i] == duplicates[i - 1]:  # Move forward if elements are equal
        continue
    p2 = i  # Sequence ends here
    if p2 - p1 == 1:  # If sequence has one element add it to no duplicates
        noduplicates = noduplicates + [duplicates[p1]]
    p1 = p2

print("List without duplicates ",noduplicates)  # Print no duplicates
