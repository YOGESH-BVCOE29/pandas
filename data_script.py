print("Hello, World!")
import pandas as pd
# read data from an Excel file
df = pd.read_excel('C:\\Users\\hp\\OneDrive\\Desktop\\pandas\\SampleSuperstore.xlsx')
print(df)
# read data from an csv file 
# df = pd.read_csv('C:\\Users\\hp\\OneDrive\\Desktop\\pandas\\SampleSuperstore.csv')
# print(df)
# read data from a json file
js = pd.read_json("C:\\Users\\hp\\OneDrive\\Desktop\\pandas\\sample_Data.json")
print(js)
