from collections import defaultdict
from data_structure import MutableTuple


class Tour:
    """

    """

    def __init__(self):
        self.path_tour = defaultdict()
        self.total_cost = 0

    def add_entry(self, node_id: int, info: MutableTuple = None):
        self.path_tour[node_id] = info

    def modify_entry(self, node_id: int, info: MutableTuple, init: bool = True):
        tuple_to_be_modified = self.path_tour[node_id]

        if not init:
            self.total_cost -= tuple_to_be_modified.cost
            self.path_tour[node_id].set_info(info)
        else:
            self.path_tour[node_id] = info

        self.total_cost += info.cost

    def __str__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])