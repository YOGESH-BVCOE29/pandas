import pandas as pd
data = {
'name' : ['ram' , 'shyam', 'ghanshyam'],
'age' : [10, 20, 30],
'city' : ['rohtak', 'delhi', 'gurgram']
}
df = pd.DataFrame(data)
print(df)
# how to save this csv file 
df.to_csv("output.csv", index = False) # here index will not use indexes which makes it more cleaner
# how to save this in excel file 
df.to_excel("output.xlsx", index = False)
# how to save this in json file 
df.to_json("output.json", index = False)
# exploring dataset 
# why do we need to eplore the data ?
'''
1 = understand the dataset
2= identify the problems 
3= plan next steps 
'''




