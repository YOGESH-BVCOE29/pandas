import pandas as pd 
# concatination = vertically and horizontally
# syntax pd.concate([df1, df2], axis =0, ignore_index = true)

# vertically
region1 = pd.DataFrame({
"customer_id":[1, 2],
"customer_name":["gopal", "raju"]
})
region2 = pd.DataFrame({
"customer_id":[3, 4],
"name":["shyam", "baburao"]
})
df_conc = pd.concat([region1, region2], ignore_index=True)

print(df_conc)
# horizontally
df_conc1 = pd.concat([region1, region2], axis=1, ignore_index=True)
print(df_conc1)