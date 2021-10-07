caps = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
lower = [chr(x) for x in range(ord('a'), ord('z') + 1)]
digits = [chr(x) for x in range(ord('0'), ord('9') + 1)]
password = input("Password\n")
capscount = 0
lowercount = 0
digitcount = 0
specialcount = 0
for ch in password:
    if ch in caps:
        capscount = 1
    elif ch in lower:
        lowercount = 1
    elif ch in digits:
        digitcount = 1
    else:
        specialcount = 1
sum = lowercount + capscount + digitcount + specialcount
strength = sum * 100 // 4
print("Strength is ", strength)
