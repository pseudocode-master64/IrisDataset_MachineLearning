import irises
import knn_classification 
import matplotlib.pyplot as plt

# x-coordinates of left sides of bars
x = [i for i in range(1,51)]
# heights of bars
y = [knn_classification.error_for(i,irises.iris_data) for i in range(1,51)]

plt.figure(figsize=(40, 5), dpi=200)

# labels for bars
tick_label = x

# plotting a bar chart
plt.bar(x, y, tick_label = tick_label,
		width = 0.8, color = ['black'])

# naming the x-axis
plt.xlabel('kth-NN')
# naming the y-axis
plt.ylabel('Error Rate')
# plot title
plt.title('Leave-one-out-cross Validation')

# function to show the plot
plt.savefig('knn_pic/Classification/Leave-one-out-cross_Validation_Bar_Plot.png')

