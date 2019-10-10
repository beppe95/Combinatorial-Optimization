from sys import maxsize
from TSP.local_search import two_opt, three_opt
from TSP.tour_construction_heuristics import random_tour_heuristic, nearest_neighbor_heuristic
from utils.make_plot import draw_plot
from utils.read_tsp_file import read_file, list_to_distances_matrix


def local_search(tsp_problem, draw, verbose, initial_h):
    """
    Do a single iteration of local search starting from random solutions.

    :param tsp_problem: name of TSP file.
    :param draw:    True for drawing plot, False otherwise.
                    Default value is False.
    :param verbose: True for printing on log file, False otherwise.
                    Default value is False.
    :param initial_h: nn to use Nearest Neighbor heuristic,
                    random to use Random heuristic.
    """

    if verbose:
        import logging
        logging.basicConfig(filename='execution.log', filemode='w', level=logging.INFO)
        logging.info(' Started main module\n')

    tsp_nodes, optimal_tour = read_file(tsp_problem, verbose)
    distances_matrix = list_to_distances_matrix(tsp_nodes, verbose)
    if initial_h == 'random':
        h_tour = random_tour_heuristic(distances_matrix, verbose)
    if initial_h == 'nn':
        h_tour = nearest_neighbor_heuristic(distances_matrix, verbose)

    two_opt_tour = two_opt(h_tour, distances_matrix, verbose)
    three_opt_tour = three_opt(h_tour, distances_matrix, verbose)

    print('Cost of heuristic tour is:', h_tour.calculate_total_cost(distances_matrix))
    print('Cost of 2-OPT tour is:', two_opt_tour.calculate_total_cost(distances_matrix))
    print('Cost of 3-OPT tour is:', three_opt_tour.calculate_total_cost(distances_matrix))

    if draw:
        draw_plot(tsp_nodes, h_tour.path)
        draw_plot(tsp_nodes, two_opt_tour.path)
        draw_plot(tsp_nodes, three_opt_tour.path)
        draw_plot(tsp_nodes, optimal_tour.path)


def multi_start_local_search(tsp_problem, k, draw, verbose, local_search_h):
    """
    Do 'k' iterations of local search starting from random solutions.

    :param tsp_problem: name of TSP file.
    :param k: number of iterations
    :param draw:    True for drawing plot, False otherwise.
                    Default value is False.
    :param verbose: True for printing on log file, False otherwise.
                    Default value is False.
    :param local_search_h: two-opt to use 2-OPT heuristic local search,
                           three-opt to use 3-OPT heuristic local search.
    """

    if verbose:
        import logging
        logging.basicConfig(filename='execution.log', filemode='w', level=logging.INFO)
        logging.info(' Started main module\n')

    tsp_nodes, optimal_tour = read_file(tsp_problem, verbose)
    distances_matrix = list_to_distances_matrix(tsp_nodes, verbose)

    best_h_tour = None
    best_tour = None
    best_cost = maxsize
    for i in range(k):
        h_tour = random_tour_heuristic(distances_matrix, verbose)
        if local_search_h == 'two_opt':
            two_opt_tour = two_opt(h_tour, distances_matrix, verbose)
            two_opt_tour_cost = two_opt_tour.calculate_total_cost(distances_matrix)
            if two_opt_tour_cost < best_cost:
                best_h_tour, best_tour, best_cost = h_tour, two_opt_tour, two_opt_tour_cost

        if local_search_h == 'three_opt':
            three_opt_tour = three_opt(h_tour, distances_matrix, verbose)
            three_opt_tour_cost = three_opt_tour.calculate_total_cost(distances_matrix)
            if three_opt_tour_cost < best_cost:
                best_h_tour, best_tour, best_cost = h_tour, three_opt_tour, three_opt_tour_cost

    print('Best Tour is:',  best_tour, '\nBest cost is:', best_cost)

    if draw:
        draw_plot(tsp_nodes, best_h_tour.path)
        if local_search_h == 'two_opt':
            draw_plot(tsp_nodes, two_opt_tour.path)
        if local_search_h == 'three_opt':
            draw_plot(tsp_nodes, three_opt_tour.path)
