class Node:
    """
    Node inside a TSP file.

    Any of them has:
        - an identifier, named 'id'
        - a longitude coordinate, named 'x'
        - a latitude coordinate, named 'y'
    """
    def __init__(self, node_id: int, x: int = None, y: int = None):
        self.node_id = node_id
        self.x = x
        self.y = y

    def __str__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

