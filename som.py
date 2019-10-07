from minisom import MiniSom
import numpy as np
from utils.make_plot import draw_plot
from utils.read_tsp_file import read_file, list_to_distances_matrix
from data_structures import Tour, Node


tsp_nodes = read_file('st70', verbose=False)[0]
dist_matrix = list_to_distances_matrix(tsp_nodes, verbose=False)

N_points = len(tsp_nodes)
N_neurons = N_points * 2

nodes = list()
x, y = np.ndarray(shape=len(tsp_nodes), dtype=int), np.ndarray(shape=len(tsp_nodes), dtype=int)
for i in range(len(tsp_nodes)):
    x[i], y[i] = tsp_nodes[i].x, tsp_nodes[i].y
    nodes.append(Node.Node(i, x[i], y[i]))

# ~ SOM
points = np.array([x, y]).T
som = MiniSom(1, N_neurons, 2, sigma=5)
som.random_weights_init(points)
som.train_random(points, 100000)
visit_order = [i+1 for i in np.argsort([som.winner(p)[1] for p in points])]
visit_order.append(visit_order[0])

# ~ PLOT
tour = Tour.Tour(visit_order)
draw_plot(tsp_nodes, tour.path)

# ~ COST
print('Il costo del tour ottenuto è:', tour.calculate_total_cost(dist_matrix))
