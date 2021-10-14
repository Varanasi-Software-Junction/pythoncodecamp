import pandas as pd

data = {
  "rollno": [1, 2, 3],
  "maths": [80, 70, 45],
"chemistry": [55, 42, 75],
"physics": [50, 67, 45]
}
df = pd.DataFrame(data,index=[0])

print(df)