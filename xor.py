a, b = 1, 1
# print(a, b, a ^ b)
data = 190
print("Original data", data)
passwd = 101
transferdata = data ^ passwd
print("transferred data encrypted  ", transferdata)

transferreddata = transferdata ^ passwd
print("decrypted ", transferreddata)
