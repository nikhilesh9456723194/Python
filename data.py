scores = [55 , 89, 76 , 65 , 93 , 50 , 72 , 88 , 56 , 99, 23]

high_score = []

# for x in scores:
#     if x >80:
#         high_score.append(x)
# print(high_score)

# data = [1 , 2 , 3 , 4 , 5, 6 , 7 , 8 , 9 , 10]

# sum_of_first_five = sum(data[:5])
# print("The sumof first number ", sum_of_first_five)

# revers = data[::-1]
# print(revers)

# numbers = [1 , 2 , 3 , 4 , 5, 6 , 7 , 8 , 9 , 10]
# fist_half = numbers[:5]
# second_half = numbers[5:]
# # Inter chmage the values
# interchanged = second_half+fist_half
# print(interchanged)
# sum_of_last_3 = sum(numbers[-3:])
# print(sum_of_last_3)

import numpy as np
# arr1 = np.array([[1,2,3] , [4,5,7]])
# arr2 = np.array([[7,8,9], [3,2,1]])
# arr = np.concatenate((arr1,arr2),axis=0)
# print(arr)

arr = np.array([1,2,3,4,5,6,7,8,9])
new_arr = np.array_split(arr,4)
print(new_arr)