import numpy as np
arr = np.array([10,20,30,40,50,60,70,80])
print("First element is ",arr[4])
print("The last element is",arr[-1])

# # slicing : Extract the part of array
# print("First three element ",arr[0:4])
# print("Last three elemetn ",arr[2::])
# print("The first element is ",arr[:-6])
# print("Every second element is ",arr[::2])

# # indexing 2D array 
# matrix = np.array([[10,20,30],[40,50,60],[70,80,90]])
# print("The matrix is",matrix)

# import numpy as np
# list_1 = [1,2,3]
# list_2 = [4,5,6]
# list_3 = [7,8,9]
# list_4 = [10,11,12]
# list_5 = np.array([[[[list_1, list_2, list_3, list_4]]]])
# print("The 4 dimensional is \n",list_5)
# print(list_5.ndim)

import numpy as np

# arr_1 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print("The attributes of numpy array are:\n", arr_1)
# print("Shape:", arr_1.shape)   # (2, 3) → 2 rows, 3 columns
# print("Size:", arr_1.size)     # 6 → total number of elements
# print("dtype:", arr_1.dtype)   # int64 (depends on your system)
# print("ndim:", arr_1.ndim)     # 2 → two-dimensional array

# Zeros array
zeros_arry = np.zeros((2,3))
print("The zeros : \n",zeros_arry)

ones_arry = np.ones((3,5))
print("The ones array is :\n",ones_arry)