import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv(r'F:\\New Python\\mymoviedb.csv',encoding ='unicode_escape')

# Drop the null value 
df.isnull().sum()
df.dropna(inplace=True)

#Rename the column 
df.rename(columns={'Vote_Count' : 'Vote__Count','Vote_Average' : 'Vote__Average'},inplace=True)

# Show the column name 
df[['Vote__Count','Vote__Average']].describe()

# Check the duplicate 
df.duplicated().sum()

# Describe 
# df.describe()

# Check the type of data 
# df.info()

#Change the data type 
df['Vote__Count'] = df['Vote__Count'].astype('Int64')
df['Vote__Average'] = df['Vote__Average'].astype(float)

# Change in date format
# df['Release_Date'] = pd.to_datetime(df['Release_Date']).dt.date
df['Release_Date'] = pd.to_datetime(df['Release_Date'], errors='coerce')


#Extract the Year from date 
df['Release_Date'] = df['Release_Date'].dt.year
df['Release_Date'].dtypes

# Dropping the column 
cols = ['Overview','Original_Language','Poster_Url']
df.drop(cols, axis=1,inplace=True)

# Column change into bucketing ( Like 8.3 = 'Popular')
def categorize_col(df, col, labels):
    # Define edges using quartiles
    edges = [
        df[col].describe()['min'],
        df[col].describe()['25%'],
        df[col].describe()['50%'],
        df[col].describe()['75%'],
        df[col].describe()['max']
    ] 
    # Apply pd.cut
    df[col] = pd.cut(df[col], edges, labels=labels, duplicates='drop')
    
    return df
labels = ['not_popular' , 'below_avg' , 'average',  'popular']
categorize_col(df, 'Vote__Average', labels)
df['Vote__Average'].unique()
df['Vote__Average'].value_counts()

# Drop the Na from column 
df.dropna(inplace=True)
(df.isna().sum())

# Split genre into the list  and then explode our dataframe to have only one genre per row for each movie
df['Genre'] = df['Genre'].str.split(', ')
df = df.explode('Genre').reset_index(drop=True)

# Data type change into category 
df['Genre'] = df['Genre'].astype('category')
df['Genre'].dtypes

# Unique Value check 
df.nunique()

# Saved Data in csv file 
# df.to_csv("Cleaned_data.csv", index=False, encoding="utf-8")
# print("File saved successfully")

# Unique Value check 
# print(df.nunique())

# # Data Viusalization
sns.set_style('whitegrid')

sns.catplot(y= 'Genre',data= df,kind='count',
            order= df['Genre'].value_counts().index,
            color= 'Yellow')
plt.title('Genre column distribution')
plt.show()

sns.catplot (y= 'Vote__Average', data=df, kind= 'count',
            order= df['Vote__Average'].value_counts().index,
            color= 'Green')
plt.title('Vote_Average column distribution')
plt.show()

print(df[df['Popularity']==df['Popularity'].max()])

print(df[df['Popularity']== df['Popularity'].min()])

sns.catplot(x= 'Release_Date', data=df , kind='count',
            order= df['Release_Date'].value_counts().index,
            color= '#4287f5')
plt.title('Release_Date column distribution')
plt.show()

df['Release_Date'].hist()
plt.title("Release_Date column distribution")
plt.show()