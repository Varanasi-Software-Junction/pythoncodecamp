class stack:
    def __init__(self):
        self.a = []

    def isEmpty(self):
        return len(self.a) <= 0

    def push(self, x):
        self.a.append(x)

    def pop(self):
        if self.isEmpty():
            return None
        return self.a.pop()

    def __str__(self):
        return str(self.a)


def quickSort(a):
    left = 0
    right = len(a) - 1
    st = stack()
    st.push((left, right))
    while not st.isEmpty():
        left, right = st.pop()
        if left >= right:
            continue
        pivot = a[left]
        finalposition = left
        for i in range(left + 1, right + 1):
            if a[i] >= pivot:
                continue
            finalposition += 1
            a[i], a[finalposition] = a[finalposition], a[i]
        a[left], a[finalposition] = a[finalposition], a[left]
        st.push((left, finalposition - 1))
        st.push((finalposition + 1, right))


a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(a)
quickSort(a)
print(a)
