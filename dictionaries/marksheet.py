results = {}
while True:
    print("0-Exit,1-Add, 2-Search,  3-Delete")
    n = int(input("Option\n"))
    if n == 0:
        break
    elif n == 1:
        print("Add")
        rollno = int(input("Roll no\n"))
        getter = results.get(rollno)
        if getter is not None:
            print('Already exits')
        else:
            name = input("name\n")
            phy = int(input("phy\n"))
            chem = int(input("chem\n"))
            math = int(input("math\n"))
            value = 'Pass'
            if phy < 33 or chem < 33 or math < 33:
                value = "Fail"
            total = phy + chem + math
            percentage = total / 3
            results[rollno] = {"name": name, "total": total, "Result": value, "Percentage": percentage,
                               "physics": phy, "Chemistry": chem, "Math": math}
    elif n == 2:
        print("Search")
        rollno = int(input("Roll no\n"))
        result = results.get(rollno, "Not found")
        print(result)
    elif n== 3:
        print("Delete")
        rollno = int(input("Roll no\n"))
        result = results.get(rollno,'not found')
        result.pop("rollno",'no key found')
        print("Deleted")
    else:
        print('Invalid option')
