class Tour:
    """

    """

    def __init__(self):
        self.root_tour = None
        self.total_cost = None

    def set_root(self, root_tour: 'Node'):
        """

        :param root_tour:
        :return:
        """
        self.root_tour = root_tour

    def set_total_cost(self, total_cost: int):
        """

        :param total_cost:
        :return:
        """
        self.total_cost = total_cost

    def get_tour_length(self):
        length = 0
        curr_node = self.root_tour
        while curr_node.neighbor is not None:
            length += 1
            curr_node = curr_node.neighbor

        return length

    def __str__(self):
        tour = '['
        curr_node = self.root_tour
        while curr_node.neighbor is not None:
            tour += str(curr_node.node_id) + '-'
            curr_node = curr_node.neighbor

        return tour[:-1] + ']'
