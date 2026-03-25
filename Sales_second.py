import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('F:\\New Python\\Sales_Data_2025.csv',encoding='unicode_escape')
# print(df)

df['Order Date'] = pd.to_datetime(df['Order Date'],dayfirst=True,format='mixed',errors='coerce')
df['Order Date']=df['Order Date'].dt.strftime('%Y-%m-%d')
df['Gender']=df['Gender'].replace({
    'Male' : 'M',
    'Female' : 'F'
})
df['Price/Unit']= df['Price/Unit'].astype(float)
df['Quantity'] = df['Quantity'].astype(float)
# print(df.dtypes)
# print(df.head(21))
df.to_csv('Cleaned_sales_data.csv',index=False)
print('File saved successfully!')
