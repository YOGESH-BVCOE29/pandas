import pandas as pd
'''
what we do in it
1= select specific columns by using square brackets
2= filter rows by using boolean conditions
3= combine multiple conditions
'''
# what selecting columns will return?
#  asingle and mutiple columns of data 
# column = df['column name]
# subset =df["column1", "column2" ...]
# filtering row basedon a single condition
# filtered_rows = df[df['column name] > condition]
# combining multiple conditions = just use and &
data = {
'name' : ['ram', 'shyam', 'dhanshyam', 'aditi', 'jagdish', 'raj', 'jagi', 'yogesh'],
'age' : [10, 15, 16, 28, 24, 14, 36, 30],
'salary': [50000, 48000, 45000, 66000, 25000, 26000, 33000, 88000], 
'perf_score' : [85, 95, 88, 99, 96, 66, 77, 78]
}
df = pd.DataFrame(data)
# display the dataframe
print("sample datframe")
print(df)
print("name (single column returns seriees)")
print(df['name'])
# selecting multiple columns
print("subset with name and salary")
print(df[["name","salary"]])
# rows filter 
high_salary = df[df['salary'] > 50000]
print("employees whose salary greater than 60k")
print(high_salary)
# filtering multiple rows 
filtered = df[(df["age"] > 30) & (df['salary'] > 20000)]
print(filtered)
# using or condition
filtered_or = df[(df['age'] > 35) | (df['perf_score'] > 90)]
print(filtered_or)




import pandas as pd
'''
what we do in it
1= select specific columns by using square brackets
2= filter rows by using boolean conditions
3= combine multiple conditions
'''
# what selecting columns will return?
#  asingle and mutiple columns of data 
# column = df['column name]
# subset =df["column1", "column2" ...]
# filtering row basedon a single condition
# filtered_rows = df[df['column name] > condition]
# combining multiple conditions = just use and &
data = {
'name' : ['ram', 'shyam', 'dhanshyam', 'aditi', 'jagdish', 'raj', 'jagi', 'yogesh'],
'age' : [10, 15, 16, 28, 24, 14, 36, 30],
'salary': [50000, 48000, 45000, 66000, 25000, 26000, 33000, 88000], 
'perf_score' : [85, 95, 88, 99, 96, 66, 77, 78]
}
df = pd.DataFrame(data)
# display the dataframe
print("sample datframe")
print(df)
print("name (single column returns seriees)")
print(df['name'])
# selecting multiple columns
print("subset with name and salary")
print(df[["name","salary"]])
# rows filter 
high_salary = df[df['salary'] > 50000]
print("employees whose salary greater than 60k")
print(high_salary)
# filtering multiple rows 
filtered = df[(df["age"] > 30) & (df['salary'] > 20000)]
print(filtered)
# using or condition
filtered_or = df[(df['age'] > 35) | (df['perf_score'] > 90)]
print(filtered_or)




