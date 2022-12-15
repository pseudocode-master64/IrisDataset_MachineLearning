from dataclasses import dataclass
from csv import DictReader
from math import sqrt


@dataclass
class Iris_Base:
    iris_id: int
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    species: str


class Iris(Iris_Base):
    "A representation of an iris flower."

    def distance1(self, other: Iris_Base) -> float:
        """
        Pythagorean distance using width and length
        of petals and sepals.
        """
        return sqrt(
            (self.sepal_length - other.sepal_length) ** 2
            + (self.sepal_width - other.sepal_width) ** 2
            + (self.petal_length - other.petal_length) ** 2
            + (self.petal_width - other.petal_width) ** 2
        )

    def distance2(self, other: Iris_Base) -> float:
        """
        Pythagorean distance using width and length
        of sepals, and whether the two flowers are
        of the same species (0 if yes, 1 if no).
        """
        return sqrt(
            (self.sepal_length - other.sepal_length) ** 2
            + (self.sepal_width - other.sepal_width) ** 2
            + (self.species != other.species)
        )


transform = {
    "id": int,
    "sepal_length": float,
    "sepal_width": float,
    "petal_length": float,
    "petal_width": float,
    "species": str,
}

iris_data: list[Iris]
with open("data/iris.csv") as f:
    iris_data = [
        Iris(*(t(row[column]) for column, t in transform.items()))
        for row in DictReader(f)
    ]