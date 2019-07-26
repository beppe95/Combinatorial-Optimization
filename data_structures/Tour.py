from numpy import ndarray


class Tour:
    """
    A TSP tour.
    """

    def __init__(self):
        self.path = list()

    def calculate_total_cost(self, distances_matrix: ndarray) -> int:
        return sum([distances_matrix[self.path[i - 1], self.path[i]]
                    for i in range(1, len(self.path))])

    def set_path(self, new_path: list):
        self.path = new_path

    def __str__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

