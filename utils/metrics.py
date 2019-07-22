import math


def l1_norm(n1: 'Node', n2: 'Node') -> int:
    return int(abs(n2.x - n1.x) + abs(n2.y - n1.y))


def l2_norm(n1: 'Node', n2: 'Node'):
    return int(math.sqrt((n1.x - n2.x)**2 + (n1.y - n2.y)**2))





