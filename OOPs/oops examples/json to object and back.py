import json


class Book:
    def __init__(self, bookname, subject, price):
        self.bookname = bookname
        self.subject = subject
        self.price = price

    def __str__(self):
        return 'Book Name={0},Subject={1}, Price={2}'.format(self.bookname, self.subject, self.price)


b = Book("The Recursion Sutras", "Recursion", 299)
print(b)
jsonbookdata = json.dumps(b.__dict__)
print(jsonbookdata)

data = '{"bookname": "The Recursion Sutras", "subject": "Recursion","price":299}'

jsonbook = json.loads(data, object_hook=lambda d: Book(**d))
print(jsonbook)
jsonbook = json.loads(jsonbookdata, object_hook=lambda d: Book(**d))
print(jsonbook)
