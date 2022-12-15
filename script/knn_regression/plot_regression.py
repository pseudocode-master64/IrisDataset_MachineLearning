import irises
import knn_regression 
import matplotlib.pyplot as plt

data_len = len(irises.iris_data)

# x-coordinates of left sides of bars
x = [i for i in range(1,50)]
# heights of bars
y = [knn_regression.error_for(i,irises.iris_data) for i in range(1,50)]

plt.figure(figsize=(40, 5), dpi=200)

# labels for bars
tick_label = x

# plotting a bar chart
plt.bar(x, y, tick_label = tick_label,
		width = 0.8, color = ['black'])

# naming the x-axis
plt.xlabel('kth-NN')
# naming the y-axis
plt.ylabel('Root-mean-squared Error (RMSE)')
# plot title
plt.title('Leave-one-out Cross Validation')
# function to store
plt.savefig('knn_pic/Regression/Leave-one-out Cross Validation_Bar_Plot.png')




