import numpy as np

#np.isnan = missing values detect
array = np.array([1,2,np.nan,3,4,5,6,np.nan])
print(np.isnan(array))

# replace missing value , defalut 0
print(np.nan_to_num(array))
print(np.nan_to_num(array,nan=100))

#infinte numberss
arr = np.array([1,2,np.inf])
print(np.isinf(arr))
print(np.nan_to_num(arr,posinf=100,neginf=1222))