# how to see rows in dataset
# head(n) = it will give you the n number of rows , tail(n) method = it will give you last n rows  , # default value for both is 5
import pandas as pd
df = pd.read_json('C:\\Users\\hp\\OneDrive\\Desktop\\pandas\\sample_Data.json')
print("display 10 rows first")
print(df.head(10))
print("display 10 rows from last")
print(df.tail(10))
# analyzing the dataset 
'''
01 = no of rows and columns 
02 = what type of data 
03 = missing data 
To get them we have 
info() , method it will gives 
1= no of rows and columns 
2= column name 
3= int , float, object
4= non null counts
5= memory usage if dataframe 
'''

bf = pd.read_json('C:\\Users\\hp\\OneDrive\\Desktop\\pandas\\sample_Data.json')
print("displaying the info of the dataset ")
print(bf.info())
# describe method in pandas = provide a summary of descriptive statistics for numerical columns in your dataframe , df.describe()
data1 = {
'name' : ['ram', 'shyam', 'dhanshyam', 'aditi', 'jagdish', 'raj', 'jagi', 'yogesh'],
'age' : [10, 15, 16, 28, 24, 14, 36, 30],
'salary': [50000, 48000, 45000, 66000, 25000, 26000, 33000, 88000], 
'perf_score' : [85, 95, 88, 99, 96, 66, 77, 78]
}
cd = pd.DataFrame(data1)
print("sample dataframe")
print(cd)
# using describe method
print("desriptive statistics")
print(cd.describe())
# before analyzing the dataset 
'''
how big is your dataset
what are the name of dataset
to get we have two methods 
shape() = return tuple of two values no of rows and no of columns, get size of datframe.
columns()= name of column as an index
'''
data2 = {
'name' : ['ram', 'shyam', 'dhanshyam', 'aditi', 'jagdish', 'raj', 'jagi', 'yogesh'],
'age' : [10, 15, 16, 28, 24, 14, 36, 30],
'salary': [50000, 48000, 45000, 66000, 25000, 26000, 33000, 88000], 
'perf_score' : [85, 95, 88, 99, 96, 66, 77, 78]
}
dd = pd.DataFrame(data2)
print(dd)
print(f'shape: {dd.shape}')
print(f'column names = {dd.columns}')

