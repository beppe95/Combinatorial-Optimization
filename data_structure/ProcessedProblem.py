class ProcessedProblem:
    """

    """

    def __init__(self, name: str, description: str, dimension: int, edge_type: str, type_problem='TSP'):
        self.name = name
        self.description = description
        self.type_problem = type_problem
        self.dimension = dimension
        self.edge_type = edge_type
        self.tour = None

    def set_tour(self, tour: 'Tour'):
        """

        :param tour:
        :return:
        """
        self.tour = tour

    def __str__(self):
        return '- ProcessedProblem -\n' \
               'name=' + self.name + \
               'description=' + self.description + \
               'type_problem=' + self.type_problem + \
               '\ndimension=' + self.dimension + \
               'edge_type=' + self.edge_type + \
               'tour=' + str(self.tour) + \
               "\n-------------------"
