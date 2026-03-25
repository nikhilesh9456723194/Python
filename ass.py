import numpy as np
data = np.array([10,20,np.nan,40,np.nan,60,np.nan,80])
print("The orginal data is",data)
print("Checking data ",np.isnan(data))
replace_value = np.nan_to_num(data,nan=0)
print("The replace data",replace_value)
mean_value = np.nanmean(data)
Replace_filled = np.where(np.isnan(data),mean_value,data)
print("Filled with mean ",Replace_filled)