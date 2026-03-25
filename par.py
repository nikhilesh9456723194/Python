import numpy as np
# data = np.array([10,20,np.nan,50,np.nan,60,np.nan,80,np.nan,100,np.nan])
# print("orginal data is",data)

# print("Checking data is ",np.isnan(data))

# replace_value = np.nan_to_num(data,nan=0)
# print("The replace value is ",replace_value)

# mean_value = np.nanmean(data)
# replace_filled = np.where(np.isnan(data),mean_value,data)
# roun_value = np.round(replace_filled).astype(int)
# print("The correct value is ",roun_value)

sales = np.array([200,220,230,240,100000,260,290,300,310,340])
mean_value = np.mean(sales)
std_devtion = np.std(sales)
upper_limit = mean_value + 2 *std_devtion
lower_limit = mean_value -2 *std_devtion
cleaned_values = sales[(sales>=lower_limit) & (sales <=upper_limit)]
print("The cleaned data is ",cleaned_values)
print(lower_limit)
print(upper_limit)

data1 = np.array([1,2,3,2,4,2,5,2,6,2,7,2,8,2,9,2,1,2,4,2])
data1[data1==2]=20
print("The upadated data is",data1)

unique_data = np.unique(data1)
print("The unique data is",unique_data)