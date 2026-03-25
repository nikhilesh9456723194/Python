# import pandas as pd
# Custom indexing 
# data = [76,87,98,78,99,86]
# student = ["Rita", "Gita", "Kiran", "Nisha", "Jyoti", "Kavita"]
# marks = pd.Series(data , index=student)
# # # print(marks)
# # print("\n The marks of Kiran is ", marks["Kiran"])
# # print("\n The marks of Nisha is :", marks.iloc[3])
# # BY Slicing
# # print("The first 3 students is \n",marks.iloc[0:8])
# # print("The student name is \n",marks.iloc[1:8:2])
# print("The maximium marks of the student is \n",marks.max())
# print("The ,mean of the studhent is",marks.mean())
# print("The std devation of the student is  ",marks.std())
# print ("The filtering is \n",marks [marks>=88])

# data1 = {"Rita" : 85 , "Kavita" : None, "Rekha" : 99 , "Neha" : 78 }
# seris1 = pd.Series(data1)
# print("\n",seris1.isnull())
# print(seris1.notnull())
# print(seris1.fillna(0))
