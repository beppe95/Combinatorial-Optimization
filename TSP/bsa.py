from sys import maxsize
from TSP.local_search import two_opt, three_opt
from utils.read_tsp_file import read_file, list_to_distances_matrix
from TSP.tour_construction_heuristics import random_tour_heuristic, nearest_neighbor_heuristic


def local_search(verbose):
    """
    Do a single iteration of local search starting from random solutions.

    :param verbose: True for printing on log file, False otherwise.
                    Default value is False.
    """

    if verbose:
        import logging
        logging.basicConfig(filename='execution.log', filemode='w', level=logging.INFO)
        logging.info(' Started main module\n')

    tsp_nodes, optimal_tour = read_file('berlin52', verbose)
    distances_matrix = list_to_distances_matrix(tsp_nodes, verbose)
    # h_tour = random_tour_heuristic(distances_matrix, verbose)
    h_tour = nearest_neighbor_heuristic(distances_matrix, verbose)

    two_opt_tour = two_opt(h_tour, distances_matrix, verbose)
    three_opt_tour = three_opt(h_tour, distances_matrix, verbose)

    print('Cost of heuristic tour is:', h_tour.calculate_total_cost(distances_matrix))
    print('Cost of 2-OPT tour is:', two_opt_tour.calculate_total_cost(distances_matrix))
    print('Cost of 3-OPT tour is:', three_opt_tour.calculate_total_cost(distances_matrix))


def multi_start_local_search(k, verbose):
    """
    Do 'k' iterations of local search starting from random solutions.

    :param k: number of iterations
    :param verbose: True for printing on log file, False otherwise.
                    Default value is False.
    """

    if verbose:
        import logging
        logging.basicConfig(filename='execution.log', filemode='w', level=logging.INFO)
        logging.info(' Started main module\n')

    tsp_nodes, optimal_tour = read_file('berlin52', verbose)
    distances_matrix = list_to_distances_matrix(tsp_nodes, verbose)

    best_tour = None
    best_cost = maxsize
    for i in range(k):
        h_tour = random_tour_heuristic(distances_matrix, verbose)
        two_opt_tour = two_opt(h_tour, distances_matrix, verbose)
        two_opt_tour_cost = two_opt_tour.calculate_total_cost(distances_matrix)
        
        if two_opt_tour_cost < best_cost:
            best_tour, best_cost = two_opt_tour, two_opt_tour_cost

    print('Best Tour is:',  best_tour, '\nBest cost is:', best_cost)
