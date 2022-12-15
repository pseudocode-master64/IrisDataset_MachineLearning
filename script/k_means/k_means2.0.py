from dataclasses import dataclass
from math import sqrt
from irises import iris_data
from random import randint
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import imageio.v2 as iio


# TODO: add other imports you may use.


@dataclass
class Point:
    """A simplified iris flower."""
    sepal_width: float
    petal_width: float
    species: str
    center_index = -1


@dataclass
class Cluster:
    sepal_width: float
    petal_width: float
    previous_sepal = -1.0
    previous_petal = -1.0

    def distance(self, p: Point) -> float:
        return sqrt((self.sepal_width - p.sepal_width) ** 2 + (self.petal_width - p.petal_width) ** 2)

    def has_moved(self, e=1e-4) -> bool:
        d = sqrt(
            (self.previous_petal - self.petal_width)**2 
            + (self.previous_sepal - self.sepal_width)**2
        )
        self.previous_petal, self.previous_sepal = self.petal_width,self.sepal_width
        return d > e


points = [
    Point(
        iris.sepal_width,
        iris.petal_width,
        iris.species,
    )
    for iris in iris_data
]

def random_centroids(k, data) -> list[Cluster]:
    """Initate the centroids by using random coordinates within the dataset"""

    centroids = []
    for _ in range (k):
        centroids.append(Cluster(data[randint(0,len(data))].sepal_width, data[randint(0,len(data))].petal_width))
    
    return centroids

def assign_cluster(centroids, data) -> list[list[Cluster],int]:
    """Find the nearest cluster of a single point, assign point to the cluster, repeat for all"""

    points_with_cluster = []
    for point in data:
        distance = []
        count = 0 #index for centroids
        for center in centroids:
            distance.append([Cluster.distance(center, point), count])
            count += 1
        distance.sort(key = lambda x: x[0]) 
        points_with_cluster.append([point,distance[0][1]])

    return points_with_cluster

def move_centroids(k, centroids, points_with_cluster) -> None:
    """Find the average x&y of the points, make that position the new centroid"""

    for i in range(k):
        total_x = 0
        total_y = 0
        count = 0
        for point in points_with_cluster:
            if point[1] == i:
                total_x += point[0].sepal_width
                total_y += point[0].petal_width
                count += 1
        centroids[i].sepal_width = total_x/count # Cluster() is used to create a new cluster point. Not covering the initial centroid point
        centroids[i].petal_width = total_y/count

def plotting(centroids, points_with_cluster, k) -> None:
    """Plot the sepal width and petal width """

    fig, ax = plt.subplots(1,1)
    x = [centroid.sepal_width for centroid in centroids]
    y = [centroid.petal_width for centroid in centroids]
    ax.scatter(x, y, marker='x', color='black')

    colors = ['red','green','blue','brown','purple']
    species = ['setosa','versicolor','virginica']
    shapes = ['o','s','D']
    shape = ''
    for point in points_with_cluster:

        x1 = [point[0].sepal_width]
        y1 = [point[0].petal_width]

        for i in range(k):
            if i == point[1]:
                chosen_color = colors[i]

        for i in range(3):
            if point[0].species == species[i]:
                shape = shapes[i]

        ax.scatter(x1, y1, marker = shape, color = chosen_color, alpha=0.4)

        clusters = []
        for i in range (k):
            clusters.append(mpatches.Patch(color = colors[i], label = f'Cluster {i+1}'))
        plt.legend(handles=clusters)


def k_means(k: int, data: list[Point]):
    """Performs k-means on the data, plots the points and clusters after each iteration"""
    
    counter = 0
    centroids = random_centroids(k, data)
    paths = []

    # continously move the centroids until the distance they are being moved by is negligible
    while any([c.has_moved() == True for c in centroids]): # Any => if one element in a list is true, the function returns true

        points_with_cluster = assign_cluster(centroids, data)

        # Plotting initial graph and each iteration
        plotting(centroids, points_with_cluster, k)

        path = f'knn_pic/K-means/G{counter+1}.png'
        plt.savefig(path)
        paths.append(path)
        counter += 1
        print(f"Graph {counter} saved")


        move_centroids(k, centroids, points_with_cluster)
    
    print(f"Total iterations: {counter}")

    return paths

def save_gif(img_paths: list[str], path: str) -> None:
    """Create a gif animation of the pictures generated"""

    imgs = [iio.imread(img_path) for img_path in img_paths]
    iio.mimsave(path, imgs, duration = 0.2)
    print("GIF file saved")

# k_input = int(input("How many clusters would you like to form? "))

save_gif(k_means(3,points), 'knn_pic/K-means/animate.gif')

print(f"View at knn_pic/K-means")
        
    
# TODO: test k_means.