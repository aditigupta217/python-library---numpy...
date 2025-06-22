import pandas as pd
"""
# read data ->
df = pd.read_csv("/Users/aditi/Desktop/Numpy/pandas/sales_data_sample.csv", encoding= "latin1")
print(df) 
#df = pd.read_json("/Users/aditi/Desktop/Numpy/pandas/sample_Data.json") 
#df = pd.read_excel("/Users/aditi/Desktop/Numpy/pandas/SampleSuperstore.xlsx") 

# save data ->
data = {
    "name" : ["ram","sham","adiil","krishn"],
    "number":[2,32,32,424],
    "city": ["nagpur","surate","lakhano","agra"]
}
df = pd.DataFrame(data)
print(df)

#df.to_csv("outputin.csv", index=False)
#df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)

# rows ->
df = pd.read_json("/Users/aditi/Desktop/Numpy/pandas/sample_Data.json") 

print("first 10 rows of dataset")
print(df.head(10))
print("last 10 rows of dataset")
print(df.tail(10)) """

# adding a columns
data = {
    "name" : ["ram","sham","adiil","krishn","buddy","niikita"],
    "number":[2,32,32,424,3,22],
    "city": ["nagpur","surate","lakhano","agra","narayba","pokimon"],
    "age" : [3,56,74,32,32,12,]
}
df = pd.DataFrame(data)
print(df)
df["bonus"] = df['number'] * 0.1
print(df)