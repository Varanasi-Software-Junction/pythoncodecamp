notes = [2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
amt = 3501
n = len(notes)
for i in range(n):
    x = amt // notes[i]
    amt = amt - x * notes[i]
    if x > 0:
        print(x, " X ", notes[i])
