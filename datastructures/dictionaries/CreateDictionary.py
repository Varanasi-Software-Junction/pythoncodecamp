runs = [1, 10, 23, 34, 56]
# Create a dictionary from 2 lists
names = ["Sachin", "Rahul", "Mahender", "Sourav", "Saubhagya"]
newdict1 = {name: run for (name, run) in zip(names, runs)}
print(newdict1)
newdict2 = {run: name for (run, name) in zip(runs, names)}
print(newdict2)
newdict3 = {run: name for (run, name) in zip(runs, [run * 2 for run in runs])}
print(newdict3)
newdict4 = {run: name for (run, name) in zip(runs, [(lambda run: run + 2)(run) for run in runs])}
print(newdict4)

newdict5 = dict.fromkeys(runs)
# Create dictionary from a list with values = None
print(newdict5)
