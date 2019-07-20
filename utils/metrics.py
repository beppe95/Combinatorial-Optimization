import math

from utils import Node


def l2_norm(n1: Node, n2: Node) -> float:
    return math.sqrt((n1.x - n2.x)**2 + (n1.y - n2.y)**2)


