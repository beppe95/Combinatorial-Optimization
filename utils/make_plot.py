from matplotlib import pyplot as plt


def draw_plot(tsp_nodes: list, path: list):
    """
    Draws plot for tbe given path.
    """

    fig = plt.figure()
    ids, xs, ys = list(), list(), list()

    for i in range(len(path)):
        curr_coords = _get_node_coordinates(tsp_nodes, path[i])
        ids.append(curr_coords[0])
        xs.append(curr_coords[1])
        ys.append(curr_coords[2])

    plt.plot(xs, ys, color='black', linestyle='dashed',
             marker='o', markerfacecolor='red', markersize=8)
    plt.plot([xs[0], xs[len(xs)-1]], [ys[0], ys[len(ys)-1]], color='black', linestyle='dashed',
             marker='o', markerfacecolor='red', markersize=8)
    plt.show()


def _get_node_coordinates(tsp_nodes: list, n_id: int):
    elem = [x for x in tsp_nodes if x.node_id == n_id][0]
    return [elem.node_id, elem.x, elem.y]
