import functools as ft


def mycompare(a, b):
    # <0 if a<b, =0 if a==b and >0 if a>b
    return b - a


def oddN(x):
    if x < 3:
        return True
    return False


class Book:
    def __init__(self, bookname, subject, price):
        self.bookname = bookname
        self.subject = subject
        self.price = price


print("Lambda")
f = lambda: print("Hello Lambda")
f()
f = lambda name: print("Hello " + name)
f("Champak")
f = lambda book: print("Book Name =  " + book.bookName)
f(Book("Basic C", "C", 150))
f = lambda a, b: print(a + b)
f(1, 2)
f = lambda a, b: print(a) if a > b else print(b)
f(1, 2)
l = ["Apple", "Ball", "Cat"]
l.sort(key=lambda x: x[1])
print(l)
l = [1, 2, 3, 4, 5]
l.sort(key=ft.cmp_to_key(mycompare))
print(l)
l = list(filter(oddN, l))
print(l)
print(any(l))
