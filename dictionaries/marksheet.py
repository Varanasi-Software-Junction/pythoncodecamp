results = {}
while True:
    print("0-Exit,1-Add, 2-Search")
    n = int(input("Option\n"))
    if n == 0:
        break
    if n == 1:
        print("Add")
        rollno = int(input("Roll no\n"))
        name = input("name\n")
        result = input("Result\n")
        results[rollno] = (name, result)
    if n == 2:
        print("Search")
        rollno = int(input("Roll no\n"))
        result = results.get(rollno, "Not found")
        print(result)
