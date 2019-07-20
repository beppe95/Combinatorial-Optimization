from TSP.tour_construction_heuristic import nearest_neighbor_heuristic
from utils.read_tsp_file import read_file

if __name__ == '__main__':
    problem, tsp_nodes = read_file('att48')

    #print(problem.tour.get_tour_length())

    nn_tour = nearest_neighbor_heuristic(tsp_nodes)
    print(nn_tour.get_tour_length())
