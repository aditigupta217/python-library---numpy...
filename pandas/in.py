import pandas as pd
"""
df = pd.read_json("/Users/aditi/Desktop/Numpy/pandas/sample_Data.json") 
print("displaying the info of dataset")
print(df.info()) """

# decribe function
data = {
    "name" : ["ram","sham","adiil","krishn","buddy","niikita"],
    "number":[2,32,32,424,3,22],
    "city": ["nagpur","surate","lakhano","agra","narayba","pokimon"],
    "age" : [3,56,74,32,32,12,]
}
df = pd.DataFrame(data)
#print(df)
#print("descripitive staticts")
#print(df.describe())

# shapes and columns
#print(f"shapes: {df.shape}")
#print(f"columns : {df.columns}")

#filters
#print("to print single column")
#print(df['name'])
#print("to select multiple coloums")
#nameage = df[["name", "city"]]
#print(nameage)

#condition filter
#print(df[df['age'] > 32])
# 2 conditions
#print(df[(df['age'] > 22) & (df['number'] > 33)] )
print(df[(df['age'] > 22) | (df['number'] > 33)] )


