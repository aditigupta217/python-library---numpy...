import pandas as pd
# sorting 
data = {
    "name" : ["ram","sham","adiil",None,"buddy","niikita"],
    "number":[1,23,53,23,21,3],
    "city": ["nagpur","None","lakhano","agra","narayba","pokimon"],
    "age" : [3,2,74,32,32,2]
}
df = pd.DataFrame(data) 
"""
#df.sort_values(by='age',ascending=False,inplace=True)
#print(df)
#df.sort_values(by=['age','number'],ascending=False,inplace=True)
#print(df)

# # summary statics , aggregation
print(df['age'].sum())
print(df['age'].mean()) # min,max,std,count

# groupiing of single column
grouped = df.groupby("age")['number'].sum()
print(grouped)

#grouping of multiple columns
grouped = df.groupby(['age','name'])['number'].sum()
print(grouped)
"""
#merging and joining
coustmer_df = pd.DataFrame({
    'name' : [ 'surash', 'rajesh', 'kamlash'],
    'age' : [33,32,29]
})

order_df = pd.DataFrame({
    'order':['biscuit','apple','bag'],
    'age' : [33,32,45]
})
# inner joint
#df_merged = pd.merge(coustmer_df,order_df, on='age',how='inner')
#print(df_merged)
# outer joint
#df_merged = pd.merge(coustmer_df,order_df, on='age',how='outer')
#print(df_merged)     # like this ,there is left , right, cross = m*n rows type

# concatenate
#df_concat = pd.concat([order_df,coustmer_df],ignore_index=True) # vertically
#print(df_concat)
df_concat = pd.concat([order_df,coustmer_df],axis=1,ignore_index=True) # horizontally
print(df_concat)
