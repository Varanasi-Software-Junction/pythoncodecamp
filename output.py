def f(x):
    vowels = ["a", "e", 'i', "o", 'u']
    x = x.lower()
    count = 0
    for ch in x:
        if ch in vowels:
            count += 1
    return count


a = ["Python", "Java", "C", "Fortran", "Pascal"]
for x in a:
    count = f(x)
    print(x, count)
a.sort(key=f)
print(a)
