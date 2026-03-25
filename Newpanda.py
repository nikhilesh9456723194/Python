import pandas as pd
df = pd.read_csv("F:\\New Python\\Sales_Data_2025.csv")
print(df[["Customer Name","Gender","Product","City"]].head(11))
print(df.iloc[0])
print(df.iloc[10:16])
Delhi_orders =df[df["City"]=="Bangalore"]
print(Delhi_orders.head())
Orders where the Quantity is greater than >=3
greater = df[df["Quantity"]>=4]
print("\n Filterted Data")
print(greater.head())
sorated_data = df.sort_values(by="City",ascending=False)
print(sorated_data.head(25))
mutli_soarted = df.sort_values(by=["City","Price/Unit"],ascending=False)
print(mutli_soarted.head(50))
print("The shape of the table is ",df.shape)
Column Add 
df["Total_Amount"] = df["Quantity"]*df["Price/Unit"]
print(df.head())
# print(df.shape)
