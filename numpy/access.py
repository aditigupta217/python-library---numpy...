import numpy as np

#indexing and slicng 
arr = np.array([3,63,78,99,43,343,534,999])
print(arr[0])
print(arr[-1])
print(arr[2])

# slicing ( for more then 1 element ) , indexing starts from 0 
# arr[start, end ,step]
print(arr[1:5]) # index 1 to 4  , 5 excluded
print(arr[:5]) # starts from 0
print(arr[::2]) # every 2nd element , 0 to last
print(arr[::-1])

# fancy indexing
array = np.array([10,20,30,40,50,60])
print(array[[2,3,5]])

# filtering 
print(array[25>array])

#reshaping and manipulating
reshape = array.reshape(2,3)  # dimenstions
print(reshape)

#flatten
arr_2d = np.array ([[1,2,3], [4,5,6]])
print(arr_2d. ravel())   # view , modifications in orginal array
print(arr_2d. flatten()) # copy, not in orginal array

# insert  np.inssert(array , index, value , asix = none)
new_array = np.insert(array,2,23, axis=None )
print(new_array)

# insert for 2d array
print("for row wise")
new_2d_arr = np.insert(arr_2d,1,[23,3,23],axis=0)
print(new_2d_arr)
print("for columnn wise")
#new_2d_arr_c = np.insert(arr_2d,1,[23,3,23],axis=1)
#print(new_2d_arr_c)

#Appendd - add at the end in array
a = np.array([1,2,3,4,5])
n = np.append(a,[6,9,0])
print(n)

#concatenate ((arr1,arr2),axis)
arr1 = np.array([1,2,3])
arr2 = np.array([5,6,7])
print(np.concatenate((arr1,arr2)))

#to delete the element
print(np.delete(arr2,2))

arr_2d = np.array ([[1,2,3], [4,5,6]])
print(np.delete(arr_2d, 0 , axis=0))
print(np.delete(arr_2d, 0 , axis=1))

#stacking 
print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))     

#splitting
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7])
print(np.split(arr1,2))
print(np.hsplit(arr1,2))

#broadcasting 
prices = np.array([100,200,300,400])
discount = 10 
final_price = prices - (prices * discount/100)
print(final_price)

# 1d to 2d 
matrix = np.array([[2,3,4],[5,6,7]])
vector = np.array([10,20,30])
print( matrix + vector )



