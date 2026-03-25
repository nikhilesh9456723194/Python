import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv(r'F:\\New Python\\Airbnb_data.csv',encoding='unicode_escape')
# print(df.head(21))
# print(df.shape)
# print(df.info())
# print(df.columns)

# Checking the Missing value 
# print(df.isnull().sum())
# print(df.info())

# Convert 'last review' to datetime
df['last review'] = pd.to_datetime(df['last review'], errors='coerce', dayfirst=True)

# print(df.info())

# Fill missing values
df.fillna({'reviews per month':0, 'last review':df['last review'].min()} , inplace= True)
df.dropna(subset=['NAME' , 'host name'], inplace=True)

# Drop the column 
df = df.drop(columns=['license', 'house_rules'], errors='ignore')

# Remove dollor sign and conver the data type in float
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
df['service fee'] = df['service fee'].replace('[\$,]', '', regex=True).astype(float)
# print(df[['price' , 'service fee']])

# Remove Duplicates
df.drop_duplicates(inplace=True)
# print(df.info())

# Descriptive Statistics
# print(df.describe())

# Visulaization 
# 1. What is the distribution of listing price?
# plt.figure(figsize=(10,6))
# sns.histplot(df['price'], bins=50 , kde=True , color= 'Orange')
# plt.title('Distibution of listing price')
# plt.xlabel("Price $")
# plt.ylabel("Frequency")
# # plt.show()

# 2.  How are different room type distributed?
# print(df['room type'])
# plt.figure(figsize=(8,9))
# sns.countplot(x= 'room type' , data=df , color='#FF9999')
# plt.title("Distribution of Room Types")
# plt.ylabel("Count")
# plt.show()

# 3. How are listing distribution across different neighborhood ?

# plt.figure(figsize=(20,16))
# sns.countplot(y= 'neighbourhood group', data=df,color='lightgreen', order=df['neighbourhood group'].value_counts().index)
# plt.title("Number of listing by Neighbourhood Group")
# plt.xlabel('count')
# plt.ylabel('Neighbourhood Group')
# plt.show()

# Alternative 
# plt.figure(figsize=(6,3))
# sns.countplot(x= 'neighbourhood group' , data=df , color='#FF9999', order=df['neighbourhood group'].value_counts().index)
# plt.title("Distribution of Room Types")
# plt.ylabel("Count")
# plt.xlabel("Neighboured Group")
# plt.show()

# 4. What is the relationship between price and room type?
# plt.figure(figsize=(10,6))
# sns.boxenplot(x='room type', y='price', hue='room type',data=df,palette='Set1')
# plt.title('Price vs Room Type')
# plt.xlabel("Room Type")
# plt.ylabel("Price $")
# plt.legend(title="Room Type")
# plt.show()

# 5. How has the number of Reviews changes over with time
df['last review'] = pd.to_datetime(df['last review'])
review_order = df.groupby(df['last review'].dt.to_period('M')).size()
plt.figure(figsize=(12,6))
review_order.plot(kind='line',color='red')
plt.title('Number of Reviews over time')
plt.xlabel('Date')
plt.ylabel('Number of Reviews')
plt.show()