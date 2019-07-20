import random
import sys

from utils.Tour import Tour
from utils.metrics import l2_norm


def nearest_neighbor_heuristic(tour_nodes: list) -> 'Tour':
    '''nn_tour = Tour()

    current_node = random.choice(tour_nodes)
    nn_tour.set_root(current_node)
    tour_nodes.remove(current_node)

    # something wrong HERE!
    while len(tour_nodes) > 1:
        best_node = None
        best_distance = sys.maxsize
        for node in tour_nodes:
            euclidean_distance = l2_norm(current_node, node)

            if euclidean_distance < best_distance:
                best_node, best_distance = node, euclidean_distance

        print(best_node)
        current_node.set_neighbor(best_node)
        current_node = best_node
        tour_nodes.remove(current_node)

    current_node.set_neighbor(tour_nodes.pop(0))
    return nn_tour'''
    return None


def greedy_heuristic(tour_nodes: set) -> 'Tour':
    greedy_tour = Tour()
    return greedy_tour


def clarke_wright_heuristic(tour_nodes: set) -> 'Tour':
    cw_tour = Tour()
    return cw_tour


def christofides_heuristic(tour_nodes: set) -> 'Tour':
    c_tour = Tour()
    return c_tour
