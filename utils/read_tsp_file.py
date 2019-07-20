from pathlib import Path

from utils.Node import Node
from utils.ProcessedProblem import ProcessedProblem
from utils.Tour import Tour


def read_file(problem_name: str) -> tuple:
    with open(Path(problem_name + '.tsp').resolve(), encoding='utf-8') as tsp_file:
        tsp_lines = tsp_file.readlines()

        problem = ProcessedProblem(tsp_lines[0].split(':')[1][1:],
                                   tsp_lines[1].split(':')[1][1:],
                                   tsp_lines[3].split(':')[1][1:],
                                   tsp_lines[4].split(':')[1][1:])

        tsp_nodes = list()
        for node in tsp_lines[6:-1]:
            node_info = node.split(' ')
            tsp_nodes.append(Node(int(node_info[0]), int(node_info[1]), int(node_info[2])))

    with open(Path(problem_name + '.opt.tour').resolve(), encoding='utf-8') as opt_file:
        opt_lines = opt_file.readlines()

        tsp_tour = Tour()
        tsp_tour.set_root(Node(int(opt_lines[5])))
        curr_node = tsp_tour.root_tour

        for opt_node in opt_lines[6:-1]:
            node_to_be_add = Node(int(opt_node))
            curr_node.set_neighbor(node_to_be_add)
            curr_node = node_to_be_add

    problem.set_tour(tsp_tour)

    return problem, tsp_nodes
