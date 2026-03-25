import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# LOad the data in python 
df = pd.read_excel(r"D:\New Volume F\New Python\Road Accident Data.xlsx")
# print(df.head(21))
# print(df.info())
# print(df.describe())

# Want to change values in a specific column, e.g. 'Accident_Type'
df['Accident_Severity'] = df['Accident_Severity'].replace('Fetal','Fatal')
df['Light_Conditions'] = df['Light_Conditions'].replace('Darkness - lighting unknown','Darkness')
df['Light_Conditions'] = df['Light_Conditions'].replace('Darkness - lights lit','Darkness')
df['Light_Conditions'] = df['Light_Conditions'].replace('Darkness - lights lit','Darkness')
df['Light_Conditions'] = df['Light_Conditions'].replace('Darkness - no lighting','Darkness')
df['Light_Conditions'] = df['Light_Conditions'].replace('Darkness - lights unlit','Darkness')

#Road Surface Cleaning (Better Format)
df['Road_Surface_Conditions'] = df['Road_Surface_Conditions'].replace('Wet or damp','Wet')
df['Road_Surface_Conditions'] = df['Road_Surface_Conditions'].replace('Flood over 3cm. deep','Others')
df['Road_Surface_Conditions'] = df['Road_Surface_Conditions'].replace('Frost or ice','Snow')

# Extract the first word (Fine, Raining, etc.) and the rest of the phrase (high winds, no high winds, etc.)
df[["Condition", "Wind_Status"]] = df["Weather_Conditions"].str.extract(r"(\w+)\s+(.*)")

# Replace blank or NaN values in Condition with "Other"
df["Condition"] = df["Condition"].fillna("Other")

# Replace blank or NaN values in Condition with "Other"
df["Wind_Status"] = df["Wind_Status"].replace("+ high winds","high winds")
df["Wind_Status"] = df["Wind_Status"].replace("or mist","Other")
df["Wind_Status"] = df["Wind_Status"].fillna("Other")

# Define mapping dictionary
vehicle_map = {
    "Car": "Car",
    "Taxi/Private hire car": "Car",
    "Motorcycle over 500cc": "Bike",
    "Motorcycle 125cc and under": "Bike",
    "Motorcycle 50cc and under": "Bike",
    "Motorcycle over 125cc and up to 500cc": "Bike",
    "Van / Goods 3.5 tonnes mgw or under": "Good Van",
    "Goods over 3.5t. and under 7.5t": "Good Van",
    "Goods 7.5 tonnes mgw and over": "Good Van",
    "Bus or coach (17 or more pass seats)": "Bus",
    "Minibus (8 - 16 passenger seats)": "Bus",
    "Agricultural vehicle": "Agricultural",
    "Other vehicle": "Other",
    "Pedal cycle": "Other",
    "Ridden horse": "Other"
}
# Apply mapping to a new column
df["Vehicle_Category"] = df["Vehicle_Type"].replace(vehicle_map)

# Drop multiple columns
df = df.drop(columns=["Local_Authority_(District)","Carriageway_Hazards","Weather_Conditions","Vehicle_Type","Police_Force","Latitude","Longitude"])

# Convert Accident Date to datetime and format as YYYY-MM-DD
df['Accident Date'] = pd.to_datetime(df['Accident Date'], errors='coerce').dt.strftime('%Y-%m-%d')

# Save the cleaned Data
df.to_excel('Cleand_Road_Accident.xlsx',index=False)
print('File saved successfully')