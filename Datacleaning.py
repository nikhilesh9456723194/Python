import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv(r'F:\\New Python\\Diwali Sales Data.csv',encoding='unicode_escape')
# print(df.info())

df.drop(['Status','unnamed1'],axis=1,inplace=True)

df['Amount']=df['Amount'].fillna(df['Amount'].mode()[0])
df= df.fillna(df.mode().iloc[0])
Missing_value = df.isnull().sum()

# print(Missing_value)
df['Age'] = df['Age'].str.replace(r'\s*(years?|yrs?|y/o|years old)', '', regex=True)
df['Age'] = df['Age'].str.strip()  # remove leading/trailing spaces
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

df['Gender']= df['Gender'].replace({
    'M' : 'M',
    'F' : 'F',
    'Femae' : 'F',
    'Fif' : 'F',
    'FIG' : 'F',
    'Ma;le' : 'M'
})

df.drop(['Status','unnamed1'], axis=1, inplace=True,errors='ignore')
print(df.head(26))

# df.to_csv('Cleaned_diwali.csv',index=False)
# print("File saved successfully!")
