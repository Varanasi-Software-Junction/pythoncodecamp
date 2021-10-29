import csv

filename = "synonyms.csv"
d={}
with open(filename, 'r') as data:
    for line in csv.reader(data):
        d[line[0]]=line
print(d)
word = input("Enter a word to search:")
found=False
for item in d.values():
    if word in item:
        found=True
        print("Synonyms are:",end="")
        for i in item:
            if len(i)>0:
                print(i,end=',')
        break
if not found:
    print("No Synonyms found")