import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('F:\\New Python\\Indian_Students_Data1.csv',encoding='unicode_escape')
# print(df.head(21))
df['payment_date'] =pd.to_datetime(df['payment_date'],errors='coerce',dayfirst=True,format='mixed')
df['payment_date']=df['payment_date'].dt.strftime('%Y-%m-%d')
df['payment_id']=df['payment_id'].str.replace('tra_','',regex=False)
df['payment_status'] = df['payment_status'].str.upper()
df['student_name'] = df['student_name'].str.title()
print(df.head(21))