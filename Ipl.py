import numpy as np
import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv(r'F:\New Python\IPL 2022.csv',encoding="unicode_escape")

# Number of matches won by each team in ipl 2022

figures = px.bar(df, x= df['match_winner'], title = 'Number of matches won in IPL 2022')
figures.show()

data['won_by'] = df['won_by'].map({'Wickets':'Chasing',
                                    'Runs':'Defending'})
won_by = df['won_by'].value_counts()
label = won_by.index
count = won_by.values
colors = ['red','lightgreen']