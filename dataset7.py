import pandas as pd 

data = {
"time" :[1, 2, 3, 4, 5],
"value":[10, None, 30, None, 50]
}
df = pd.DataFrame(data)
print("value befroe interpolation")
print(df)
# linear interpolation
df['value'] = df['value'].interpolate(method="linear")
print("after interpolation")
print(df)
'''
when it is used?
time series interpolation used
numeric data with trends
avoid dropping rows
'''



