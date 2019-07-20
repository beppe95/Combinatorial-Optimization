import random

from utils.Tour import Tour


def nearest_neighbor_heuristic(tour_nodes: list) -> 'Tour':
    nn_tour = Tour()

    root = random.choice(tour_nodes)
    nn_tour.set_root(root)
    tour_nodes.remove(root)




    return nn_tour


def greedy_heuristic(tour_nodes: set) -> 'Tour':
    greedy_tour = Tour()
    return greedy_tour


def clarke_wright_heuristic(tour_nodes: set) -> 'Tour':
    cw_tour = Tour()
    return cw_tour


def christofides_heuristic(tour_nodes: set) -> 'Tour':
    c_tour = Tour()
    return c_tour
