import requests

searchValue = input("Enter search value\n")
link = "https://www.googleapis.com/books/v1/volumes?q={0}".format(searchValue)
print(link)
response = requests.get(link)
print(response.json())
books = response.json()["items"]
print(len(books), books)
for book in books:
    print(book)
