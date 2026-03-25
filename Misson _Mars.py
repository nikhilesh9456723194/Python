import numpy as Np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv(r"F:\\New Python\\Data set Part 2 - propulsion_module.csv",encoding='unicode_escape')

data = {
    "Parameter":[
        "Lunar Polar Orbit",
        "Mission life",
        "Structure",
        "Dry Mass",
        "Propellant Mass",
        "Total PM Mass",
        "Power Generation",
        "Communiaction",
        "Attitude Sensors",
        "Propulsion System"
    ],
    "Specifications":[
        "From 170 x 36500 km to lunar polar orbit",
        "Carrying Lander Module & Rover upto ~100 x 100 km launch injection",
        "Modified version of I-3 K",
        "448.62 kg (including pressurant)",
        "1696.39 kg",
        "2145.01 kg",
        "738 W, Summer solistices and with bias",
        "S-Band Transponder (TTC) â€“ with IDSN",
        "CASS, IRAP, Micro star sensor",
        "Bi-Propellant Propulsion System (MMH + MON3)"
    ]
}
prop_df = pd.DataFrame(data)
# print(prop_df)

data ={
    "Parameter":[
        "Mission life",
        "Mass",
        "Power",
        "Payloads",
        "Dimensions (mm3)",
        "Communication",
        "Landing site"
    ],
    "Specifications":[
        "1 Lunar day (14 Earth days)",
        "1749.86 kg including Rover",
        "738 W (Winter solstice)",
        "3",
        "2000 x 2000 x 1166",
        "ISDN, Ch-2 Orbiter, Rover",
        "69.367621 S, 32.348126 E"
    ]
}
lander_df = pd.DataFrame(data)
# print(lander_df)

data = {
    "Parameter":[
        "Mission Life",
        "Mass",
        "Power",
        "Payloads",
        "Dimensions (mm3)",
        "Communication"
    ],
    "Specifications":[
        "1 Lunar day",
        "26 kg",
        "50 W",
        "2",
        "917 x 750 x 397",
        "Lander"
    ]
}
rover_df = pd.DataFrame(data)
# print(rover_df)

import re
def extract_numerical_value(spec):
    numeric_pattern = r'(\d+(\.\d+)?)'
    custom_numeric_pattern = r"[-+]?[.]?[\d]+(?:,\d\d\d)*(?:[eE][-+]?\d+)?"
    combined_pattern = f"({numeric_pattern}|{custom_numeric_pattern})"
    matches = re.findall(combined_pattern,spec)
    if matches:
        return float(matches[0][0])
    else:
        return None

prop_df["numerical_value"] = prop_df["Specifications"].apply(extract_numerical_value)
lander_df['numerical_value'] = lander_df['Specifications'].apply(extract_numerical_value)
rover_df['numerical_value'] = rover_df['Specifications'].apply(extract_numerical_value)
# print(rover_df)

import math
rover_mass = 26
lander_dry_mass = 1749.86
total_mass = rover_mass+lander_dry_mass
delta_v_required = 1500
isp_lander_engine = 300
Propellant_mass_required = total_mass*math.exp(delta_v_required/isp_lander_engine)
Propellant_mass_required = round(Propellant_mass_required,2)

rover_power_requirement = 50
lander_battery_capacity = 2000
rover_operting_time_hours = lander_battery_capacity/rover_power_requirement

# print('Mass Budget:')
# print(f"Lander mass:{lander_dry_mass} kg")
# print(f"Rover mass : {rover_mass} kg")
# print(f"propellant mass required: {Propellant_mass_required} kg(matches value)")

# print("\nPower Budget:")
# print(f"Rover power requirement:{rover_power_requirement} W")
# print(f"Lander Battery capacity :{lander_battery_capacity} Wh")
# print(f"Rover can OPerate:{rover_operting_time_hours:.2f}hours on stored")

# print("\nMobility Assessment:")
# print("Low mass of the rover allows for mobility on uneven lunar surface")
# print("Number pf payloads for science measurement is 2")

# Visulaization

import matplotlib.pyplot as plt

labels = ['Lander Dry Mass', 'Rover Mass', 'Propellant Mass']
Mass_value = [lander_dry_mass, rover_mass, Propellant_mass_required]

plt.figure(figsize=(8,5))
plt.bar(labels, Mass_value, color=['blue','pink','red'])
plt.xlabel("Components")
plt.ylabel("Mass (kg)")
plt.title("Mass Budget")
plt.ylim(0, max(Mass_value) * 1.2)

for i, v in enumerate(Mass_value):
    plt.text(i, v, f"{v:.2f}", ha='center', va="bottom")
# plt.show()

lables = ['Rover Power Requirement','lander Battery capacity']
Power_values = [rover_power_requirement,lander_battery_capacity]
plt.figure(figsize=(8,6))
plt.bar(lables,Power_values,color=['blue','green'])
plt.xlabel("Components")
plt.ylabel("Power(Watt-hours)")
plt.title("Power Budget")
plt.ylim(0,max(Power_values)*1.2)
for i , v in enumerate(Power_values):
    plt.text(i, v, str(v),ha="center",va="bottom")
# plt.show()

import plotly.express as px
mass_labels = ['Lander Dry Mass','Rover Mass','Propellant Mass']
Mass_value = [lander_dry_mass , rover_mass , Propellant_mass_required]
Mass_fig = px.bar(x=mass_labels,y=Mass_value,color=mass_labels,
                    labels={"x":"Components","y":"Mass(kg)"},
                    title="Mass Budget")
Mass_fig.update_traces(texttemplate='%{y:.2f}kg',textposition='outside')
# Mass_fig.show()

import plotly.express as px
power_labels = ['Rover Power Requirement', 'Lander Battery Capacity']
power_values = [rover_power_requirement, lander_battery_capacity]

power_fig = px.bar(
    x=power_labels,
    y=power_values,
    color=power_labels,
    labels={"x": "Components", "y": "Power (Watt-hours)"},
    title="Power Budget"
)
power_fig.update_traces(texttemplate='%{y:.2f} Wh', textposition="outside")
# power_fig.show()

import plotly.express as px

mass_fig = px.pie(
    names=mass_labels,
    values= Mass_value,
    title='Mass Budget'
)
mass_fig.show()
