import irises
import knn_classification 
import matplotlib.pyplot as plt

data_len = len(irises.iris_data)
x = [i for i in range(1,51)]
y = [knn_classification.error_for(i,irises.iris_data) for i in range(1,51)]

  
plt.plot(x, y)
# naming the x-axis
plt.xlabel('kth-NN')
# naming the y-axis
plt.ylabel('Error Rate')
# plot title
plt.title('Leave-one-out-cross Validation')

# function to show the plot
plt.savefig('knn_pic/Classification/Leave-one-out-cross_Validation_Line_Graph.png')