from irises import Iris, Iris_Base, iris_data

# TODO: add other imports you may use.


def predict_petal_length(iris: Iris, data: list[Iris], k: int) -> float:
    """
    Returns a prediction of the petal_length of `iris`
    based on the `k` nearest neighbors in `data`.
    """
    count = 0
    distances = []
    k_neighbors = []
    total = 0

    # Sort the Euclidean distance of each flower to the new flower
    for flower in data:
        distances.append([Iris.distance2(iris, flower), count])
        count += 1
    distances.sort(key = lambda x: x[0])

    # Find the index of k nearest neighbors
    for i in range(k):
        k_neighbors.append(distances[i][1])
    
    # Return the average petal length among the neighbors
    for i in k_neighbors:
        total += data[i].petal_length

    return total/k
        

    


def error_for(k: int, data: list[Iris]) -> float:
    """
    Uses "leave-one-out" cross validation to estimate the
    root-,ean-squared error associated with k nearest
    neighbors.
    """

    predicted_petal_length = []
    squared_deviation = 0

    # Leave one out, find remaining
    for i in range(len(data)):
        remaining_flower = []
        for j in range(len(data)):
            if j != i:
                remaining_flower.append(data[j])

    # Predict petal length of data set
        predicted_petal_length.append(predict_petal_length(data[i], remaining_flower, k))
        squared_deviation += (predicted_petal_length[i-1] - remaining_flower[i-1].petal_length)**2

    # Return root-mean-squared error
    return squared_deviation/len(data)

# TODO: test predict_petal_length and error_for.

iris1 = Iris_Base(1,5.1,3.5,1.4,0.2,"setosa")
print(predict_petal_length(iris1,iris_data,3))

k = 3
print(error_for(k, iris_data))
