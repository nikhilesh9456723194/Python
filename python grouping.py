# import pandas as pd
# df = pd.read_csv("F:\\New Python\\Sales_Data_2025.csv")
# print(df.head())
# # # Adding Column
# df["Total_Amount"]=df["Quantity"]*df["Price/Unit"]
# # print(df.head())
# df["Discount"] = df["Total_Amount"]*0.10
# # print(df.head())
# df["After_Discount"] = df["Total_Amount"] - df["Discount"]
# # print(df.head())
# # print(df.shape)
# # Grouping Column
# # Total Sales by Region
# # Total_sales = df.groupby("Region")["Quantity"].sum()
# # print(Total_sales)
# # Total_orders = df.groupby("Region")["Total_Amount"].sum()
# # print(Total_orders)
# # Total_avg = round(df.groupby("Gender")["Total_Amount"].mean(),2)
# # print(Total_avg)
# # Export filterted data 
# Delhi_data = df[df["City"]=="Delhi"]
# Delhi_data.to_csv("Delhi_orders.csv",index=False)

import pandas as pd
df = pd.read_csv("F:\\New Python\\Indian_Students_Data1.csv")
df['payment_date'] = pd.to_datetime(df['payment_date'], format='%d/%m/%Y')
df['payment_date'] = df['payment_date'].dt.strftime('%Y-%m-%d')
print(df.head())


