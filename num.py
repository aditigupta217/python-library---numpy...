# create the sequences
import numpy as np;
arr = np.arange(1,10,2) # start , end , steps 
print(arr)

# identity matrix creation
identity = np.eye(3)
print(identity)

#shape
arr_2d = np.array([[1,2,4],[5,7,7]])
print(arr_2d.shape)

#size
print(arr_2d.size)

# NO. of dimsions
print(arr_2d.ndim)

# type
print(arr_2d.dtype)

#for change the type
arr = np.array([[1.3,3.32,5.5]])  # float to int
print(arr.astype(int))

# operators

print(arr + 5)
print(arr * 7)

# aggregation functions

array = np.array([2,6,42,6,4])
print(np.sum(array))
print(np.min(array))
print(np.max(array))
print(np.average(array))
print(np.std(array))
print(np.var(array))

