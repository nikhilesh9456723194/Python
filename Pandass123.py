import pandas as pd
df = pd.read_csv("F:\\New Python\\Sales_Data_2025.csv")
# print(df.head())
# print(df[["Customer Name","City","Price/Unit"]].head(10))
# print(df.iloc[0])
# print(df.iloc[9:10])
# delhi_orders = df[df["City"]=="Delhi"]
# print(delhi_orders)
# big_orders = df[df["Quantity"]>=4]
# print("\n Filtered Record :")
# print(big_orders.head())
# soarted_data = df.sort_values(by="Price/Unit",ascending=False)
# print(soarted_data.head(11))
# multi_sort = df.sort_values(by=["Region","City"],ascending=False)
# print(multi_sort.head(20))
# print("Shape",df.shape)
df["Total_amount"]=df["Quantity"]*df["Price/Unit"]
# print(df.head(10))
# print("Shape",df.shape)
df["Discount"] = df["Total_amount"]*.10
# print(df.head(11))
df["after_discount"] = df["Total_amount"] - df["Discount"]
print(df.head(11))
