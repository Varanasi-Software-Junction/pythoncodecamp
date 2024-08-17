upper=0
lower=0
line="HellO"

for ch in line:
	if ch.islower():
		# print("Lower", ch)
		lower+=1
	if ch.isupper():
		# print("Upper", ch)
		upper+=1
print("lower=",lower,"upper=",upper)

