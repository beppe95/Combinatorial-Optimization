from utils.read_tsp_file import read_file, list_to_distances_matrix
from TSP.tour_construction_heuristics import nearest_neighbor_heuristic
from TSP.local_search import two_opt, three_opt


def main(verbose=False):
    if verbose:
        import logging
        logging.basicConfig(filename='execution.log', filemode='w', level=logging.INFO)
        logging.info(' Started main module\n')

    tsp_nodes, optimal_tour = read_file('berlin52', verbose)
    distances_matrix = list_to_distances_matrix(tsp_nodes, verbose)
    nn_tour = nearest_neighbor_heuristic(distances_matrix, verbose)

    two_opt(nn_tour, distances_matrix, verbose)
    three_opt(nn_tour, distances_matrix, verbose)


if __name__ == '__main__':
    main()
