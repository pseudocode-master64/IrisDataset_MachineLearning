from irises import Iris, iris_data

# TODO: add other imports you may use.

def classify(iris: Iris, data: list[Iris], k: int) -> str:
    """
    Returns a prediction of the species of `iris` based on
    the `k` nearest neighbors in `data`.
    """
    count = 0
    distances = []
    k_neighbors = []
    species = []

    # Sort the Euclidean distance of each flower to the new flower
    for flower in data:
        distances.append([Iris.distance1(iris, flower), count])
        count += 1
    distances.sort(key = lambda x: x[0])

    # Find the index of k nearest neighbors
    for i in range(k):
        k_neighbors.append(distances[i][1])
    
    # Find the species of k nearest neighbors
    for neighbor in k_neighbors:
        species.append(data[neighbor].species)
    
    # Return the most common species of the neighbors 
    return str(max(set(species), key = species.count))


def error_for(k: int, data: list[Iris]) -> float:
    """
    Uses "leave-one-out" cross validation to estimate the
    error associated with k nearest neighbors.
    """

    incorrect = 0
    prediction_species = []

    for i in range(len(data)):
        # Leave one out, find remaining
        remaining_flower = []
        for j in range(len(data)):
            if j != i:
                remaining_flower.append(data[j])

        # Prediction and error counting
        prediction_species.append(classify(data[i], remaining_flower, k))
        if prediction_species[i-1] != remaining_flower[i-1].species:
            incorrect += 1

    return incorrect/len(data)
        
# TODO: test classify and error_for.

Iris1 = Iris(99,5.1,2.5,3.0,1.1,"versicolor")
print(classify(Iris1, iris_data, 3))

k = 3
print(error_for(k,iris_data))