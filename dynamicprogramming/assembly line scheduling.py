s1 = [2, 7, 9, 3, 4, 8, 4]
s2 = [4, 8, 5, 6, 4, 5, 7]
t1 = [2, 3, 1, 3, 4, 3]
t2 = [2, 1, 2, 2, 1, 2]
path1 = []
path2 = []
n = len(s1)
f1 = [2]
f2 = [4]
f1.append(f1[0] + s1[1])
f2.append(f2[0] + s2[1])
# print(f1, f2)
v1 = f1[1] + s1[2]
v2 = f2[1] + t2[0] + s1[2]
if v1 < v2:
    path1.append(1)
    f1.append(v1)

else:
    path1.append(2)
    f1.append(v2)

v1 = f2[1] + s2[2]
v2 = f1[1] + t1[0] + s2[2]
if v1 < v2:
    path2.append(2)
    f2.append(v1)
else:
    f2.append(v2)
    path2.append(1)
# print(f1, f2)

for i in range(2, n - 1):
    v1 = f1[i] + s1[i + 1]
    v2 = f2[i] + t2[i - 1] + s1[i + 1]
    if v1 < v2:
        path1.append(1)
        f1.append(v1)
    else:
        path1.append(2)
        f1.append(v2)
    v1 = f2[i] + s2[i + 1]
    v2 = f1[i] + t1[i - 1] + s2[i + 1]
    if v1 < v2:
        path2.append(2)
        f2.append(v1)
    else:
        f2.append(v2)
        path2.append(1)
f1.append(f1[- 1] + t1[-1])
f2.append(f2[- 1] + t2[-1])
print("Score f1", f1, ", route f1", path1)
print("Score f2", f2, ", route f2", path2)

if f1[-1] < f2[-1]:
    route = path1
    fastestpath = f1
else:
    fastestpath = f2
    route = path2
print("Fastest path=", fastestpath, ", route is ", route)
