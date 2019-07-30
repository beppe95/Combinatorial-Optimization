from matplotlib.pyplot import plot, show


def draw_plot(tsp_nodes: list, path: list):
    """
    Draws plot for tbe given path.
    """

    data = list()
    for i in range(len(path)):
        curr_coord = _get_node_coordinate(tsp_nodes, path[i])
        data.append(curr_coord)

    for i in range(1, len(data)):
        plot([data[i - 1][0], data[i][0]], [data[i - 1][1], data[i][1]], color='black', linestyle='dashed',
             marker='o', markerfacecolor='red', markersize=8)

    plot([data[0][0], data[len(data)-1][0]], [data[0][1], data[len(data)-1][1]], color='black', linestyle='dashed',
         marker='o', markerfacecolor='red', markersize=8)

    show()


def _get_node_coordinate(tsp_nodes: list, n_id: int):
    elem = [x for x in tsp_nodes if x.node_id == n_id][0]
    return [elem.x, elem.y]
