import random
import sys
from operator import itemgetter

from data_structure.Node import Node
from data_structure.MutableTuple import MutableTuple
from data_structure.Tour import Tour
from utils.metrics import l2_norm


def nearest_neighbor_heuristic(tour_nodes: list) -> Tour:
    nn_tour = Tour()

    current_node = random.choice(tour_nodes)
    nn_tour.add_entry(current_node.node_id)
    tour_nodes.remove(current_node)

    while len(tour_nodes) > 1:
        best_node = None
        best_distance = sys.maxsize

        for node in tour_nodes:
            euclidean_distance = l2_norm(current_node, node)
            if euclidean_distance < best_distance:
                best_node, best_distance = node, euclidean_distance

        nn_tour.add_entry(best_node.node_id)
        nn_tour.modify_entry(current_node.node_id, MutableTuple(best_node, best_distance))

        current_node = best_node
        tour_nodes.remove(best_node)

    # qui sta messo a mano il nodo
    nn_tour.add_entry(tour_nodes.pop(0).node_id, MutableTuple(Node(nn_tour.path_tour.keys()[0], 0, 0), ))

    return nn_tour


def greedy_heuristic(tour_nodes: set) -> 'Tour':
    greedy_tour = Tour()

    ordered_edges_list = list()
    for node1 in tour_nodes:
        for node2 in tour_nodes:
            if node1 != node2:
                #ordered_edges_list.append([node1.node_id, node2.node_id, l2_norm(node1, node2)])
                ordered_edges_list.append((node1.node_id, node2.node_id, l2_norm(node1, node2)))

    ordered_edges_list.sort(key=itemgetter(2))
    print(ordered_edges_list)



    '''current_node = random.choice(tour_nodes)
    nn_tour.add_entry(current_node.node_id)
    tour_nodes.remove(current_node)

    print(current_node)
    while len(tour_nodes) > 1:
        best_node = None
        best_distance = sys.maxsize

        for node in tour_nodes:
            euclidean_distance = l2_norm(current_node, node)
            if euclidean_distance < best_distance:
                best_node, best_distance = node, euclidean_distance

        nn_tour.add_entry(best_node.node_id)
        nn_tour.modify_entry(current_node.node_id, MutableTuple(best_node, best_distance))

        current_node = best_node
        tour_nodes.remove(best_node)

    # qui sta messo a mano il nodo
    # nn_tour.add_entry(tour_nodes.pop(0).node_id, MutableTuple(Node(nn_tour.path_tour.keys()[0], 0, 0), ))'''


    return greedy_tour


def clarke_wright_heuristic(tour_nodes: set) -> 'Tour':
    cw_tour = Tour()
    return cw_tour


def christofides_heuristic(tour_nodes: set) -> 'Tour':
    c_tour = Tour()
    return c_tour
