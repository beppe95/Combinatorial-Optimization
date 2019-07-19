class Tour:

    def __init__(self):
        self.root_tour = None
        self.total_cost = None

    def set_root(self, root_tour: 'Node'):
        self.root_tour = root_tour

    def total_cost(self, total_cost: int):
        self.total_cost = total_cost

    '''def get_info(self) -> str:
        return '{ID: ' + self.node_id + '\t' + 'x_coordinate: ' \
               + self.x + 'y_coordinate: ' + self.y'''

