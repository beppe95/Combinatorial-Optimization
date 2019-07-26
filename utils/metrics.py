from math import sqrt
from data_structures.Node import Node


def l1_norm(n1: Node, n2: Node) -> int:
    """
    Compute Manhattan distance between n1 and n2 nodes using their respective coordinates.

    :param n1: first node
    :param n2: second node
    :return: Manhattan distance between n1 and n2
    """
    return int((abs(n2.x - n1.x) + abs(n2.y - n1.y)) + .5)


def l2_norm(n1: Node, n2: Node):
    """
    Compute Euclidean distance between n1 and n2 nodes using their respective coordinates.

    :param n1: first node
    :param n2: second node
    :return: Euclidean distance between n1 and n2
    """
    return int((sqrt((n1.x - n2.x)**2 + (n1.y - n2.y)**2)) + .5)





