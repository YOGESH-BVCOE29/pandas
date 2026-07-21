import pandas as pd 
data = {
"name" :["arun", 'arjun', 'varun', 'tarun', 'yogesh'],
"age":[28, 20, 33, 28, 19],
"salary":[10000, 20000, 30000, 55000, 90000]
}
df = pd.DataFrame(data)
grouped = df.groupby('age')["salary"].sum() # create unique values of age and add salry of that unique ages 
print(grouped)
grouped1 = df.groupby(['age', "name"])["salary"].sum()
print(grouped1)
#common aggregation functions 
'''
1= sum
2= mean
3= std
4= max
5= min
6= std
'''
# merging = combining rows of two or more dataframes basedon accommon key column
# pd.merge(df1, df2, on="column name", how="type of join" )
df_customers = pd.DataFrame({
"customer_id":[1, 2, 3],
"name":["ramesh","suresh", "kalpesh"]
})
df_orders = pd.DataFrame({
"customer_id":[1, 2, 4],
"order_amount":[250,  450, 350]
})
# merge 
df_merged = pd.merge(df_customers, df_orders, on="customer_id", how="inner")
print("inner join")
print(df_merged)

df_merged1 = pd.merge(df_customers, df_orders, on="customer_id", how="outer")
print("outer join")
print(df_merged1)
# try all joins
