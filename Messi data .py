import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv(r'F:\New Python\\Diwali Sales Data.csv',encoding='unicode_escape')
# print(df.head())
# Drop unrlated / Blank column 
df.drop(['Status','unnamed1'],axis=1,inplace=True,errors='ignore')

# Chnage the data type 
df['Age']= pd.to_numeric(df['Age'],errors='coerce')
df['Age']=df['Age'].fillna(df['Age'].median())
df['Age']=df['Age'].astype('Int64')

#Step 1: Clean column names (remove trailing spaces)
df.columns = df.columns.str.strip()
# Step 2: Convert to datetime properly
date_columns = ['Login date ', 'Disbursed', 'Order Date']
for col in date_columns:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col],dayfirst=True,format='mixed',errors='coerce')
# Step 3: If you want formatted strings (YYYY-MM-DD)
for col in date_columns:
    if col in df.columns:
        df[col] = df[col].dt.strftime('%Y-%m-%d')
# print(df.info())
df['Gender'] = df['Gender'].replace({
    'M' : 'M',
    'F' : 'F',
    'Female' : 'F',
    'Male' : 'M'
})
# print(df.head(25))
duplicate_all = df[df.duplicated(keep=False)]
df = df.drop_duplicates()
# print(duplicate_all)

# Replace blanks/NaN in a specific column, e.g. 'City'
df['State'] = df['State'].fillna('Delhi')
# print(df.head(21))
# df.to_csv('Cleaned_data.csv',index=False)
# print('File saved successfully')
# print(df[['Login date','Disbursed']])

# Amount fill with Meadin
df['Amount']=df['Amount'].fillna(df['Amount'].mean())
# print(df['Amount'].head(51))
# df.to_csv('Cleaned_databas.csv',index=False)
# print('File saved successfully')

# Replace blanks/NaN in a specific column, e.g. 'Age Group'
df['Age Group'] = df['Age Group'].fillna('18-25')
df['Zone'] = df['Zone'].fillna('southern')
df['Product_Category'] = df['Product_Category'].fillna('Beauty')
df['Gender'] = df['Gender'].fillna('M')
df.to_csv('Cleand Rawdata.csv',index=False)
print('File saved successfully')


