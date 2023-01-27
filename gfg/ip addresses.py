ip = "123456789123"
n = len(ip)
# print(ip)
for i in range(1, 4):
    part1 = ip[:i]
    p2 = ip[i:]
    for j in range(i, i + 3):
        part2 = p2[:j ]
        newip = part1 + "." + part2


    # print(newip)
