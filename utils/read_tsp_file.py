from pathlib import Path

from data_structure.Node import Node
from data_structure.ProcessedProblem import ProcessedProblem
from data_structure.Tour import Tour


def read_file(problem_name: str):
    """
    Read both .tsp and .opt.tour files from a TSPLIB problem.

    :param problem_name: TSP name from TSPLIB repository
    :return:
    """

    tsp_file_path = Path.cwd() / 'TSPLIB_instances' / problem_name

    with open(tsp_file_path / (problem_name + '.tsp'), encoding='utf-8') as tsp_file:
        tsp_lines = tsp_file.readlines()

        problem = ProcessedProblem(tsp_lines[0].split(':')[1][1:],
                                   tsp_lines[1].split(':')[1][1:],
                                   tsp_lines[3].split(':')[1][1:],
                                   tsp_lines[4].split(':')[1][1:])

        tsp_nodes = list()
        for node in tsp_lines[6:-1]:
            node_info = node.split(' ')
            tsp_nodes.append(Node(int(node_info[0]), int(node_info[1]), int(node_info[2])))

    with open(tsp_file_path / (problem_name + '.opt.tour'), encoding='utf-8') as opt_file:
        opt_lines = opt_file.readlines()

        tsp_tour = Tour()

        for opt_node in opt_lines[6:-2]:
            tsp_tour.add_entry(int(opt_node))

    tsp_tour.total_cost = int(opt_lines[4].split(':')[1])

    problem.set_tour(tsp_tour)

    return problem, tsp_nodes
