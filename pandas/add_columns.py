import pandas as pd
# adding a columns
data = {
    "name" : ["ram","sham","adiil",None,"buddy","niikita"],
    "number":[1,2,3,None,5,6],
    "city": ["nagpur","None","lakhano","agra","narayba","pokimon"],
    "age" : [3,56,74,32,32,None]
}
df = pd.DataFrame(data)
#print(df)
"""
df["bonus"] = df['number'] * 0.1
#print(df)
# using insert method add columns
df.insert(0,"enployee_id",[1,2,3,4,5,6])
print(df)

# updating the values 
df.loc[0,'city'] = 'pune' # df.loc[ row index , ' name of column'] = new name
#print(df)
#updating more then one value
df['age'] = df['age'] * 1.05
print(df)

# removing columns 
df.drop(columns=['age','number'],inplace=True) #inplace true -> modified data 
print(df)

 # handaling the missing daata
# NaN = not a none , none = for object data type , isnull() True - NaN is missing  ,False - value is present
print(df)
#print(df.isnull())
#print(df.isnull().sum())

# handlaing  the missing vlaues
df.dropna(inplace=True)   # hole row vanishs , for columns = axis =1
print(df)

df.fillna(0,inplace=True) 
print(df)
df['age'].fillna(df['age'].mean(), inplace=True)
print(df)

# interpolate -> estimate vallues 
df.interpolate(method='linear', axis=0 , inplace=True)  # linear
print(df)"""
df ['number'] = df [ 'number']. interpolate(method="linear")
print(df)