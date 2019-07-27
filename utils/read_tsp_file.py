from logging import info
from pathlib import Path
from numpy import zeros
from data_structures.Node import Node
from data_structures.Tour import Tour
from utils.metrics import l1_norm, l2_norm


def read_file(problem_name: str, verbose: bool) -> tuple:
    """
    Read both .tsp and .opt.tour files from a TSPLIB problem.

    :param problem_name: TSP name from TSPLIB repository
    :param verbose: True for printing on log file, False otherwise.
                    Default value is False.

    :return: a list, named 'tsp_nodes', containing all nodes specified inside .tsp file
             and a tour, named 'optimal_tour', which contains the sequence given as
             optimal path for the current TSP.
    """

    tsp_file_path = Path.cwd() / 'TSPLIB_instances' / problem_name

    if verbose:
        info(' Reading %s.tsp file', problem_name)

    with open(tsp_file_path / (problem_name + '.tsp'), encoding='utf-8') as tsp_file:
        tsp_lines = tsp_file.readlines()

        tsp_nodes = list()
        for node in tsp_lines[6:-1]:
            node_info = node.split(' ')
            tsp_nodes.append(Node(int(node_info[0]), int(float(node_info[1])), int(float(node_info[2]))))

    if verbose:
        info(' %s.tsp EOF reached\n', problem_name)
        info(' Reading %s.opt.tour file', problem_name)

    with open(tsp_file_path / (problem_name + '.opt.tour'), encoding='utf-8') as opt_file:
        opt_lines = opt_file.readlines()

        optimal_tour = Tour()
        for opt_node in opt_lines[6:-2]:
            optimal_tour.path.append(int(opt_node))

    if verbose:
        info(' %s.opt.tour EOF reached\n', problem_name)

    optimal_tour.path.append(optimal_tour.path[0])

    return tsp_nodes, optimal_tour


def list_to_distances_matrix(tsp_nodes: list, verbose, metric='euclidean',) -> zeros:
    """
    Builds up a distance matrix which represent the complete graph
    build from the given list,

    :param tsp_nodes: list of TSP's nodes
    :param verbose: True for printing on log file, False otherwise.
                    Default value is False.
    :param metric: metric used to calculate distances between TSP's nodes.
           If metric='manhattan' then method will use Manhattan Distance.
           Otherwise, if metric='euclidean' then method will use Euclidean Distance.

    :return: a len(tsp_nodes) x len(tsp_nodes) matrix, named 'distances_matrix', which contains
             for each pair of nodes their distance.
    """

    dimension = len(tsp_nodes) + 1
    distances_matrix = zeros(shape=(dimension, dimension), dtype=int)

    if verbose:
        info(' Computing distances matrix for %d nodes', dimension)

    for i in range(1, dimension):
        for j in range(1, dimension):
            if i == j:
                continue
            node_1, node_2 = tsp_nodes[i-1], tsp_nodes[j-1]
            if metric == 'manhattan':
                distances_matrix[i, j] = l1_norm(node_1, node_2)
            if metric == 'euclidean':
                distances_matrix[i, j] = l2_norm(node_1, node_2)

    if verbose:
        info(' Distances matrix is ready for use now.\n')
    return distances_matrix

