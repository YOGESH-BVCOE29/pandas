# adding columns 
import pandas as pd
data = {
'name' : ['ram', 'shyam', 'dhanshyam', 'aditi', 'jagdish', 'raj', 'jagi', 'yogesh'],
'age' : [10, 15, 16, 28, 24, 14, 36, 30],
'salary': [50000, 48000, 45000, 66000, 25000, 26000, 33000, 88000], 
'perf_score' : [85, 95, 88, 99, 96, 66, 77, 78]
}
df = pd.DataFrame(data)
print(df)
#m1 = square brackets df['columnm_name'] = some_data
df["bonus"] = df['salary'] * 0.1
print(df)
# m2 = using insert method at specific location
# syntax = df.insert(location, "column name", data )
df.insert(0, "employee_id", [10, 20, 30, 40, 50, 60, 70, 80])
print(df)
# updating values in dataframe 
# m1
#.loc[] method
# syntax = df.loc[row_index, "column name"] = new_value
df.loc[0, "salary"] = 88000
print(df)
# m2
# increasing salaries by 5 percent
df['salary'] = df['salary'] *0.05
print(df)

# removing columns by using drop method 
# syntax = df.drop(columns = ["column_name"], inplace = true )
df.drop(columns=["perf_score"], inplace=True)
print(df)
# removing multiple columns
# df.drop(columns=["column1", "column2"], inplace=True)