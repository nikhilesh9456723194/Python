import numpy as np
data = [68,79,38,68,35,70,61,45,58,66]
mean_data = np.mean(data)
print("The mean of the data is", mean_data)

# import statistics as stats
# data1 = [43,55,66,77,88,99,11,22,33]
# mean_data1 = stats.mean(data1)
# print("The statistics mean is ",mean_data1)

# import seaborn as sns
# import numpy as np
# iris = sns.load_dataset('iris')
# mean_spal_length = np.mean(iris['sepal_length'])
# print("The sepal length is ",mean_spal_length)

import numpy as np
data11 = [68,79,38,68,35,70,61,45,58,66]
medina_data = np.median(data11)
print("The median of the data is ",medina_data)

# import statistics as stats
# data22 = [12,23,45,67,800,900,34,23,54,12,43]
# sta_median = stats.median(data22)
# print("The medina of the data is",sta_median)

# import pandas as pd
# df = pd.DataFrame({
#     "values" : [23,45,65,78,67,87,18,11,12,34,500,1000]
# })
# pand_data = df["values"].median()
# print("The pamda of the median is ",pand_data)

# import seaborn as sns
# import  numpy as np
# iris = sns.load_dataset('iris')
# median_11 = np.median(iris['sepal_length'])
# print("The seaborn medina is ",median_11)

import statistics as stats
a = [68,79,38,68,35,70,61,45,58,66]
mode_a = stats.multimode(a)
print("The mode is ",mode_a)

# from scipy import stats
# b = [85,90,45,65,78,23,45,65,45,12]
# mode_b = stats.mode(b)
# print("The scipy libray is ",mode_b)

import numpy as np
ab = [68,79,38,68,35,70,61,45,58,66]
sample_var = np.var(ab,ddof=1)
print("The sample variance is ",sample_var)
popu_var = np.var(ab,ddof=0)
print("The population variance is ",popu_var)

# import pandas as pd
# abc = [2,3,4,5,6,7,8,9,12,13,14,16,17,18,19,20]
# series = pd.Series(abc)
# samplee_var = series.var(ddof=1)
# print("The panda variance is ",samplee_var)
# population_var = series.var(ddof=0)
# print("The population is ",population_var)

# from scipy import stats
# abcd = [7,8,2,3,4,5,6,7,8,9,10,12,14,15,16]
# sample_vari = stats.tvar(abcd,ddof=1)
# print("The sample variance is ",sample_vari)
# popution_scipy = stats.tvar(abcd,ddof=0)
# print("The scipy population is ",popution_scipy)

import pandas as pd
sd = [68,79,38,68,35,70,61,45,58,66]
str = pd.Series(sd) 
sampl_pd = str.std(ddof=1)
print("The sample panda ",sampl_pd)
pop_pd = str.std(ddof =0)
print("The population data is ",pop_pd)

# from scipy import stats
# import math
# sample_std = math.sqrt(stats.tvar(sd,ddof=1))
# print("The sample variance is ",sample_std)
# pip_std = math.sqrt(stats.tvar(sd,ddof=0))
# print("The population of the standard devation is ",pip_std)

# Data Representaions
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# fig, axs = plt.subplots(3, 2, figsize=(14,12))
# fig.suptitle("Histogram with KDE of Various Distributions", fontsize=16)

# # Normal distribution
# data_normal = np.random.normal(loc=0, scale=1, size=1000)
# sns.histplot(data_normal, kde=True, ax=axs[0,0], color='blue', stat='density', bins=30)
# axs[0,0].set_title("Normal Distribution")   # ✅ call the function
# axs[0,0].grid(True)

# plt.tight_layout(rect=[0, 0, 1, 0.96])  # adjust layout so title fits
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# fig, axs = plt.subplots(3, 2, figsize =(4, 12))
# fig.suptitle ("Histogram with KDE of various distributions ",fontsize = 16)

# data_normal = np.random.normal(loc=0 , scale= 1,size=1000)
# sns.histplot(data_normal, kde = True, ax=axs[0,0],color='green',stat='density',bins=30)
# axs[0,0].set_title("Normal Distribution")
# axs[0,0].grid(True)
# plt.tight_layout(rect=[0,0,1,0.96])
# plt.show()


















