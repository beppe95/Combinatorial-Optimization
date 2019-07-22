from TSP.tour_construction_heuristic import nearest_neighbor_heuristic, greedy_heuristic
from utils.read_tsp_file import read_file

if __name__ == '__main__':
    problem, tsp_nodes = read_file('att48')

    '''nn_tour = nearest_neighbor_heuristic(tsp_nodes)
    for k, v in nn_tour.path_tour.items():
        print(k, v)'''


    greedy_heuristic(tsp_nodes)
