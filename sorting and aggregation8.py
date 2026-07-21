import pandas as pd
# sorting data = arranging dataon based on your conditions in one or more columns
# sorting data 1 column sort_values()
# df.sort_values(by="column name", true/false, inplace=true)
data = {
"name" :["arun", 'arjun', 'varun'],
"age":[28, 20, 33],
"salary":[10000, 20000, 30000]
}
df = pd.DataFrame(data)
df.sort_values(by="age", ascending = False, inplace=True)
print("sorted age by desc")
print(df)
# sorting operation on multiple values 
# syntax = df.sort_values(by=["age", "salary"], ascending = [true,false] inplace = true)
data1 = {
"name" :["arun", 'arjun', 'varun'],
"age":[28, 34, 22],
"salary":[10000, 20000, 30000]
}
bf = pd.DataFrame(data1)
bf.sort_values(by=["age", "salary"], ascending = [True,False], inplace=True)
print(bf)
# aggregating data = calculating summary statistics 
# summary statistics = numerical summaries of columns like mean , sum etc
'''
syntax
df["column name].mean()
df["column name].sum()
df["column name].min()
df["column name].max()
'''
avg_salary = bf['salary'].mean()
print(avg_salary)
