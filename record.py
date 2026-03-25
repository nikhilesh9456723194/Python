import pandas as pd
df = pd.read_csv("F:\\New Python\\Sales_Data_2025.csv")
# print(df.head(6))
# Change Customer name of ID 1261
# df.loc[df["Order Number"]==1263,"Customer Name"]="A.Rawat"
# print(df.head(6))
# Update multiple column 
df.loc[df["Product"]=="Laptop",["Category","Price/Unit"]]=["Heavy Elect",95000]
# Laptop_order = df[df["Product"]=="Laptop"]
# print(Laptop_order.head())
# df= df.drop(["Region","Quantity"],axis=1)
# print(df)
df = df.drop(["Gender"],axis=1)
print(df.head())
