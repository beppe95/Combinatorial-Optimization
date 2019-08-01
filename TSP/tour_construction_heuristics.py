from numpy import zeros
from random import randrange, shuffle
from sys import maxsize
from logging import info
from data_structures.Tour import Tour


def random_tour_heuristic(distances_matrix: zeros, verbose: bool) -> Tour:
    """
    Implements Random Tour heuristic for TSP.

    :param distances_matrix: distances matrix for a TSP
    :param verbose: True for printing on log file, False otherwise.
                    Default value is False.

    :return: a feasible tour according to Random Tour heuristic
    """

    if verbose:
        info(' Calculating Random Tour heuristic')

    random_path = list(range(1, len(distances_matrix)))
    shuffle(random_path)

    if verbose:
        info(' Got tour based on Random Tour heuristic.\n')
    return Tour(random_path)


def nearest_neighbor_heuristic(distances_matrix: zeros, verbose: bool) -> Tour:
    """
    Implements Nearest Neighbor heuristic for TSP.

    Uses NN heuristic to construct a solution:
    - start visiting city 'current_node'
    - while there are unvisited cities, follow to the closest one

    :param distances_matrix: distances matrix for a TSP
    :param verbose: True for printing on log file, False otherwise.
                    Default value is False.

    :return: a feasible tour according to NN heuristic
    """

    if verbose:
        info(' Calculating Nearest Neighbor heuristic')

    matrix_dimension = len(distances_matrix) - 1

    nn_path = list()
    visited = set()

    current_node = randrange(1, matrix_dimension)
    visited.add(current_node)
    nn_path.append(current_node)

    while matrix_dimension - len(visited) > 0:
        best_node = None
        best_distance = maxsize

        for j in range(1, len(distances_matrix[current_node])):
            if j in visited or current_node == j:
                continue
            if distances_matrix[current_node, j] < best_distance:
                best_node, best_distance = j, distances_matrix[current_node, j]

        if best_node is not None:
            visited.add(best_node)
            nn_path.append(best_node)
            current_node = best_node

    nn_path.append(nn_path[0])

    if verbose:
        info(' Got tour based on Nearest Neighbor heuristic.\n')
    return Tour(nn_path)


def nearest_neighbor_heuristic_optimized(distances_matrix: zeros, verbose: bool) -> Tour:
    return None
