import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import the CSV file in python  
df = pd.read_csv(r'F:\\New Python\\Diwali Sales Data.csv',encoding='unicode_escape')
# print(df.head)
# print(df.info())

# Drop the blank and unrelated column 
df.drop(['Status','unnamed1'],axis=1,inplace=True,errors='ignore')
# df.info()

# Check the null Value 
# print(df.isnull().sum())

# Drop the null
df.dropna(inplace=True)
# print(df)

# Change the data type 
# df['Amount']=df['Amount'].astype('int')
# print(df)

# Rename the column name 
df.rename(columns={'Marital_Status':'Shaadi_Status'},inplace=True)
# print(df.head())

# Describe method return description of the data in the dataframe (ie. Count , Mean , Mode)
# print(df.describe())
# print(df.columns)
# print(df[['Age','Orders','Amount']].describe())
# df.to_csv('Cleaned_data.csv',index=False)
# print("File saved successfully!")

# ax = sns.countplot(x= 'Gender', data=df)
# for bar in ax.containers:
#     ax.bar_label(bar)
# # plt.show()

# Sales_gen = df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
# sns.barplot(x='Gender',y='Amount',data=Sales_gen)
# # plt.show()


# ax = sns.countplot(data=df, x='Age Group', hue='Gender', palette='Set2')
# for bars in ax.containers:
#     ax.bar_label(bars, fontsize=10, padding=3)
# plt.title("Customer Distribution by Age Group and Gender")
# plt.xlabel("Age Group")
# plt.ylabel("Count")
# plt.xticks(rotation=45)
# plt.legend(title="Gender")
# plt.show()

# Total Amount and Age group 
# Sales_age = (
# df.groupby(['Age Group'],as_index=False)['Amount']
# .sum()
# .sort_values(by='Amount',ascending=False))
# sns.barplot(x='Age Group' , y= 'Amount',data=Sales_age)
# plt.title('Total Sales Amount by Age Group', fontsize=14, weight='bold')
# plt.xlabel('Age Group', fontsize=12)
# plt.ylabel('Total Amount', fontsize=12)
# plt.show()

# Total numner of orders from top 10 cities
# Sales_state = (
# df.groupby(['State'],as_index=False)['Orders']
# .sum()
# .sort_values(by='Orders',ascending=False)
# .head(10))
# sns.set(rc={'figure.figsize':(8,5)})
# sns.barplot(
#     x='State',
#     y='Orders',
#     data=Sales_state,
# )
# plt.title('Top 10 state by Orders', fontsize=14, weight='bold')
# plt.xlabel('State', fontsize=12)
# plt.ylabel('Orders', fontsize=12)
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# Total number of state Amount from top 10 cities
sale_amount = df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False.head(10))
sns.set(rc={'figure.figsize':(8,5)})
sns.barplot(
    x='State',
    y='Amount',
    data=sale_amount
)
plt.title('Top 10 state by Orders', fontsize=14, weight='bold')
plt.xlabel('State', fontsize=12)
plt.ylabel('Orders', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()















