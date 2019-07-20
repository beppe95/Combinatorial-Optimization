class Tour:

    def __init__(self):
        self.root_tour = None
        self.total_cost = None

    def set_root(self, root_tour: 'Node'):
        self.root_tour = root_tour

    def total_cost(self, total_cost: int):
        self.total_cost = total_cost

    def __str__(self):
        tour = '['
        curr_node = self.root_tour
        while curr_node.neighbor is not None:
            tour += str(curr_node.node_id) + '-'
            curr_node = curr_node.neighbor

        return tour[:-1] + ']'
