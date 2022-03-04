a = [5, 10, 7, 19, 21, 3, 20]
mx1, mx2 = a[0], a[1]
if mx2 > mx1:
    mx1, mx2 = mx2, mx1
# Set the bigger value from pos 0 and 1 to mx1, and the second to mx2
n = len(a)  # Get length of a
for i in range(2, n):
    value = a[i]
    if value <= mx2:
        continue  # Do nothing
    if value >= mx1:  # New value larger than mx1. Set mx2 to old mx1, mx1= value
        mx2 = mx1
        mx1 = value
        continue
    mx2 = value  # Value >mx2 and less than mx1. Set mx2 to value
print("Largest is ", mx1, ", second largest ", mx2)
