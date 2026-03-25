# import pandas as pd
# # data = [10,20,30,40,50,60]
# # series = pd.Series(data)
# # print("The series of the pandas liberay is:")
# # print(series)

# data1 = {
#     "Name" : ["Anita", "Sita", "Kajal","Komal","Kavita"],
#     "Age" : [ 32, 33, 31, 34, 28],
#     "City" : [ "Chandigarh" , "Bihar" , "Uttrakhand", "Delhi" , "Uttar Pradesh"]
# }
# df = pd.DataFrame(data1)
# print("He data frame is:")
# print(df)
import pandas as pd
df = pd.read_csv("F:\\New Python\\sales_data.csv")
print(df.head())
# print(df.tail())
# print(df)
# print("The shape of table is ",df.shape)
# print(df.columns)
# print(df.info())
# print(df.describe())
