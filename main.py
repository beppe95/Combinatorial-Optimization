from utils.read_tsp_file import read_file, list_to_distances_matrix
from TSP.tour_construction_heuristics import random_tour_heuristic, nearest_neighbor_heuristic
from TSP.local_search import two_opt, three_opt


def main(verbose=False):
    if verbose:
        import logging
        logging.basicConfig(filename='execution.log', filemode='w', level=logging.INFO)
        logging.info(' Started main module\n')

    tsp_nodes, optimal_tour = read_file('st70', verbose)
    distances_matrix = list_to_distances_matrix(tsp_nodes, verbose)
    #rnd_tour = random_tour_heuristic(distances_matrix, verbose)
    #nn_tour = nearest_neighbor_heuristic(distances_matrix, verbose)

    '''two_opt_tour = two_opt(nn_tour, distances_matrix, verbose)
    three_opt_tour = three_opt(nn_tour, distances_matrix, verbose)

    print(nn_tour.calculate_total_cost(distances_matrix))
    print(two_opt_tour.calculate_total_cost(distances_matrix))
    print(three_opt_tour.calculate_total_cost(distances_matrix))'''


if __name__ == '__main__':
    main()
