import irises
import knn_regression 
import matplotlib.pyplot as plt

data_len = len(irises.iris_data)
x = [i for i in range(1,50)]
y = [knn_regression.error_for(i,irises.iris_data) for i in range(1,50)]

  
plt.plot(x, y)
# naming the x-axis
plt.xlabel('kth-NN')
# naming the y-axis
plt.ylabel('Root-mean-squared Error (RMSE)')
# plot title
plt.title('Leave-one-out Cross Validation')
# function to store
plt.savefig('knn_pic/Regression/Leave-one-out Cross Validation_Line.png')