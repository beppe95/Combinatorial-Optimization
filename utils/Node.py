class Node:
    """

    """
    def __init__(
            self,
            node_id: int,
            x: int = None,
            y: int = None,
            neighbor: 'Node' = None,
            cost: int = None
    ):
        self.node_id = node_id
        self.x = x
        self.y = y
        self.neighbor = neighbor
        self.cost = cost

    def set_neighbor(self, neighbor: 'Node', c: int = None):
        """

        :param neighbor:
        :param c:
        :return:
        """
        self.neighbor = neighbor
        self.cost = c

    def __str__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

