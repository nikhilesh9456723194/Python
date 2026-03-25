import matplotlib.pyplot as plt 

# DATA
x = [1,2,3,4,5,6,7,8,9]
y1 = [30,50,24,67,89,34,65,87,99]
y2 = [99,43,12,45,67,89,34,11,32]

plt.plot(x , y1, label = "Sales 2024")
plt.plot(x , y2, label = "Sales 2025")
plt.title("YOY Sales")
plt.xlabel ('Month')
plt.ylabel ("Sales")

plt.legend()
plt.show()