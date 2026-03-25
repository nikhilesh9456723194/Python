ta # # Python list
# list1 = [i for i in range(1, 10000)]
# start = time.time()
# list_sum = [x + 5 for x in list1]
# end = time.time()
# print("Python list time:", end - start)

# # NumPy array
# arr = np.arange(1, 10000)
# start = time.time()
# arr_sum = arr + 5
# end = time.time()
# print("NumPy array time:", end - start)# import numpy as np
# # create  1D array
# arr = np.array([1,2,3,4,5,6,7,8,9])
# print("Numpay Array :",arr


# import numpy as np
# import time

# list11 = [i for i in range (1,20000)]
# start1 = time.time()
# list1_sum = [ x+5 for x in list11]
# end11 = time. time()
# print("The Python list time:",end11 - start1)

# # Numpay Array
# arr = np.arange (1,20000)
# start = time.time()
# list_sum = arr + 5
# end = time.time()
# print("The numpay time is ",end - start)

# import numpy as np

# matrix = np.array([[1,2,3], [4,5,6],[7,8,9]])
# print("The matrxi is \n",matrix)

import numpy as np
from scipy import stats
arr = np.array([10,20,30,40,50,50,60])
print("The array with 5 number increment is ",arr+5)
print ("The mean is ",np.mean(arr))
print("The st devation is ",np.std(arr))
print("The mode is ",np.median(arr))
print("The mode is ",stats.mode(arr))
print("The sumis ",np.sum(arr))
print("The minimunm is ",np.min(arr))
print("The max is ",np.max(arr))
arr_1 = [10,20,30,40,50,60,70,80,90,100]
arr_1.reverse()
print("Reversed order is ",arr_1)



