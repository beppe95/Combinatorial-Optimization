import numpy
from random import randrange, choice
from sys import maxsize
from logging import info
from data_structures.Tour import Tour


def random_tour_heuristic(distances_matrix: numpy.zeros, verbose: bool) -> Tour:
    """
    Implements Nearest Neighbor heuristic for TSP.

    :param distances_matrix: distances matrix for a TSP
    :param verbose: True for printing on log file, False otherwise.
                    Default value is False.

    :return: a feasible tour according to Random Tour heuristic
    """

    if verbose:
        info(' Calculating Random Tour heuristic')

    nodes = list(range(1, len(distances_matrix)))

    rnd_tour = Tour()
    while len(nodes) > 0:
        current_node = choice(nodes)
        nodes.remove(current_node)
        rnd_tour.path.append(current_node)

    rnd_tour.path.append(rnd_tour.path[0])

    if verbose:
        info(' Got tour based on Random Tour heuristic.\n')
    return rnd_tour


def nearest_neighbor_heuristic(distances_matrix: numpy.zeros, verbose: bool) -> Tour:
    """
    Implements Nearest Neighbor heuristic for TSP.

    :param distances_matrix: distances matrix for a TSP
    :param verbose: True for printing on log file, False otherwise.
                    Default value is False.

    :return: a feasible tour according to NN heuristic
    """

    if verbose:
        info(' Calculating Nearest Neighbor heuristic')

    matrix_dimension = len(distances_matrix) - 1

    nn_tour = Tour()
    visited = set()

    current_node = randrange(1, matrix_dimension)
    visited.add(current_node)
    nn_tour.path.append(current_node)

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
            nn_tour.path.append(best_node)
            current_node = best_node

    nn_tour.path.append(nn_tour.path[0])

    if verbose:
        info(' Got tour based on Nearest Neighbor heuristic.\n')
    return nn_tour


def nearest_neighbor_heuristic_optimized(distances_matrix: numpy.zeros, verbose: bool) -> Tour:
    return None