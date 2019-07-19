class Node:

    def __init__(self, node_id: int, x: int, y: int):
        self.node_id = node_id
        self.x = x
        self.y = y
        self.neighbor = None
        self.cost = None

    def get_info(self) -> str:
        return '{ID: ' + self.node_id + '\t' + 'x_coordinate: ' \
               + self.x + 'y_coordinate: ' + self.y

    def set_neighbor(self, n: 'Node', c: int):
        self.neighbor = n
        self.cost = c

