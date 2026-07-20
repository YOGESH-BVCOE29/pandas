#HANDLING MISSING DATA 
#1 NAN = not a number 
#2 none = for object data type 
# how to  identify which value is missing 
# isnull9 method gives True(value missing), false(value is present)
import pandas as pd 
data = {
'name' : ['ram', None, 'dhanshyam', 'aditi', 'jagdish', 'raj', 'jagi', 'yogesh'],
'age' : [10, None, 16, 28, 24, 14, 36, 30],
'salary': [50000, None, 45000, 66000, 25000, 26000, 33000, 88000], 
'perf_score' : [85, None, 88, 99, 96, 66, 77, 78]
}
df = pd.DataFrame(data)
print(df)
print(df.isnull())
# how to find that how many value are missing in column = isnull().sum()
print(df.isnull().sum())
