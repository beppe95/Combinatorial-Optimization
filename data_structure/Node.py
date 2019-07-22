class Node:
    """

    """
    def __init__(self, node_id: int, x: int = None, y: int = None):
        self.node_id = node_id
        self.x = x
        self.y = y

    def __str__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

