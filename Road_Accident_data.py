import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# LOad the data in python 
df = pd.read_excel(r"F:\New Python\Road Accident Data.xlsx")
# print(df.head(21))
# print(df.info())
# print(df.describe())

# Want to change values in a specific column, e.g. 'Accident_Type'
df['Accident_Severity'] = df['Accident_Severity'].replace('Fetal','Fatal')
df['Light_Conditions'] = df['Light_Conditions'].replace('Darkness - lighting unknown','Darkness')
df['Light_Conditions'] = df['Light_Conditions'].replace('Darkness - lights lit','Darkness')
df['Light_Conditions'] = df['Light_Conditions'].replace('Darkness - lights lit','Darkness')
df['Light_Conditions'] = df['Light_Conditions'].replace('Darkness - no lighting','Darkness')
df['Road_Surface_Conditions'] = df['Road_Surface_Conditions'].replace('Wet or damp','Wet')
df['Road_Surface_Conditions'] = df['Road_Surface_Conditions'].replace('Flood over 3cm. deep','Others')
df['Road_Surface_Conditions'] = df['Road_Surface_Conditions'].replace('Frost or ice','Snow')

# Split the Weather condition 
df['Weather_Conditions_Split'] = df['Weather_Conditions'].apply(
    lambda x: re.split(r'[+,]', x)
)

df.to_excel('Cleand_data.xlsx',index=False)
print('File saved successfully')

