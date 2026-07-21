import pandas as pd 
data = {
"name" :["arun", 'arjun', 'varun', 'tarun', 'yogesh'],
"age":[28, 20, 33, 28, 19],
"salary":[10000, 20000, 30000, 55000, 90000]
}
df = pd.DataFrame(data)
grouped = df.groupby('age')["salary"].sum()
print(grouped)