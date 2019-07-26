from numpy import zeros
from copy import deepcopy
from logging import info
from data_structures.Tour import Tour


def two_opt(current_tour: Tour, distances_matrix: zeros) -> Tour:
    """
    Implements 2-OPT heuristic for TSP.

    :param current_tour: the initial tour which is provided by the Nearest Neighbor heuristic.
    :param distances_matrix: distances matrix for a TSP.
    :return: the optimal tour according to 2-OPT heuristic.
    """

    iteration = 0
    info(' Started 2-OPT heuristic')
    info(' Initial cost: %d', current_tour.calculate_total_cost(distances_matrix))

    best_tour = deepcopy(current_tour)
    improved = True

    while improved:
        info(' Started iteration %d', iteration)
        improved = False
        for i in range(1, len(current_tour.path) - 2):
            for j in range(i + 2, len(current_tour.path)):
                if j - i == 1 or j - i == len(current_tour.path) - 2:
                    continue

                old_edges_cost = get_edges_cost(distances_matrix, current_tour.path, i, j)
                new_edges_cost = get_edges_cost(distances_matrix, current_tour.path, i, j, case='new')
                info(' Iteration %d: \t Old cost: %d \t New cost: %d', iteration, old_edges_cost, new_edges_cost)

                iteration += 1
                if new_edges_cost < old_edges_cost:
                    best_tour.path[i:j] = current_tour.path[j-1:i-1:-1]
                    current_tour = best_tour
                    info(' Swapping... got this path\n %s\n', current_tour.path)
                    improved = True
                    break

            if improved:
                break
    info(' Optimal solution found is\n %s', current_tour.path)
    info(' Optimal solution cost is %d\n', current_tour.calculate_total_cost(distances_matrix))
    return current_tour


def get_edges_cost(distances_matrix: zeros, current_path: list, index1: int, index2: int, case: str = 'old') -> int:
    """
    Calculate the cost of the edges to be swapped inside the tour.

    :param distances_matrix: distances matrix for a TSP.
    :param current_path: list which contains the current path.
    :param index1: first index to be swapped.
    :param index2: second index to be swapped.
    :param case: string representing the current swap to be made.
    :return: cost of the swapped edges
    """

    return (distances_matrix[current_path[index1 - 1], current_path[index1]] +
            distances_matrix[current_path[index2 - 1], current_path[index2]]) if case == 'old' \
        else (distances_matrix[current_path[index1 - 1], current_path[index2 - 1]] +
              distances_matrix[current_path[index1], current_path[index2]])


def three_opt(current_tour: Tour, distances_matrix: zeros) -> Tour:
    """
    Implements 3-OPT heuristic for TSP.

    :param current_tour: the initial tour which is provided by the Nearest Neighbor heuristic.
    :param distances_matrix: distances matrix for a TSP.
    :return: the optimal tour according to 3-OPT heuristic.
    """

    iteration = 0
    info(' Started 3-OPT heuristic')
    info(' Initial cost: %d', current_tour.calculate_total_cost(distances_matrix))

    best_tour = deepcopy(current_tour)
    improved = True
    dict_cost = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

    while improved:
        info(' Started iteration %d', iteration)
        improved = False
        for (i, j, k) in possible_segments(len(current_tour.path)):
            for case in dict_cost:
                dict_cost[case] = get_moves_cost(distances_matrix, best_tour.path, case, i, j, k)

            best_case = max(dict_cost, key=dict_cost.get)
            iteration += 1
            if dict_cost[best_case] > 0:
                best_tour.set_path(reverse_segments(best_tour.path, best_case, i, j, k))
                current_tour = best_tour
                info(' Swapping... got this path\n %s\n', current_tour.path)
                improved = True
                break

    info(' Optimal solution found is\n %s', current_tour.path)
    info(' Optimal solution cost is %d\n', current_tour.calculate_total_cost(distances_matrix))
    return current_tour


def possible_segments(n: int):
    """
    Generate all possible i-j-k feasible combinations for the given input number.

    :param n: input number
    :return: a generator which contains ll possible i-j-k feasible combinations for the given input number.
    """
    segments = ((i+1, j+1, k+1) for i in range(n) for j in range(i + 2, n-1) for k in range(j + 2, n - 2 + (i > 0)))
    return segments


def get_moves_cost(distances_matrix: zeros, best_path: list, case: int, i: int, j: int, k: int):
    """

    :param distances_matrix:
    :param best_path:
    :param case:
    :param i:
    :param j:
    :param k:
    :return:
    """

    A, B, C, D, E, F = best_path[i - 1], best_path[i], \
                       best_path[j - 1], best_path[j], \
                       best_path[k - 1], best_path[k % len(best_path)]

    if case == 0:
        # first case is the current solution ABC
        return 0
    elif case == 1:
        # second case is the case A'BC
        return distances_matrix[A, B] + distances_matrix[E, F] - (distances_matrix[B, F] + distances_matrix[A, E])
    elif case == 2:
        # ABC'
        return distances_matrix[C, D] + distances_matrix[E, F] - (distances_matrix[D, F] + distances_matrix[C, E])
    elif case == 3:
        # A'BC'
        return distances_matrix[A, B] + distances_matrix[C, D] + distances_matrix[E, F] - \
               (distances_matrix[A, D] + distances_matrix[B, F] + distances_matrix[E, C])
    elif case == 4:
        # A'B'C
        return distances_matrix[A, B] + distances_matrix[C, D] + distances_matrix[E, F] - \
               (distances_matrix[C, F] + distances_matrix[B, D] + distances_matrix[E, A])
    elif case == 5:
        # AB'C
        return distances_matrix[B, A] + distances_matrix[D, C] - (distances_matrix[C, A] + distances_matrix[B, D])
    elif case == 6:
        # AB'C'
        return distances_matrix[A, B] + distances_matrix[C, D] + distances_matrix[E, F] - \
               (distances_matrix[B, E] + distances_matrix[D, F] + distances_matrix[C, A])
    elif case == 7:
        # A'B'C
        return distances_matrix[A, B] + distances_matrix[C, D] + distances_matrix[E, F] - \
               (distances_matrix[A, D] + distances_matrix[C, F] + distances_matrix[B, E])
    
    
def reverse_segments(best_path, case, i, j, k):
    """

    :param best_path:
    :param case:
    :param i:
    :param j:
    :param k:
    :return:
    """

    if (i - 1) < (k % len(best_path)):
        first_segment = best_path[k % len(best_path):] + best_path[:i]
    else:
        first_segment = best_path[k % len(best_path):i]
    second_segment = best_path[i:j]
    third_segment = best_path[j:k]

    if case == 0:
        pass
    elif case == 1:
        solution = list(reversed(first_segment)) + second_segment + third_segment
    elif case == 2:
        solution = first_segment + second_segment + list(reversed(third_segment))
    elif case == 3:
        solution = list(reversed(first_segment)) + second_segment + list(reversed(third_segment))
    elif case == 4:
        solution = list(reversed(first_segment)) + list(reversed(second_segment)) + third_segment
    elif case == 5:
        solution = first_segment + list(reversed(second_segment)) + third_segment
    elif case == 6:
        solution = first_segment + list(reversed(second_segment)) + list(reversed(third_segment))
    elif case == 7:
        solution = list(reversed(first_segment)) + list(reversed(second_segment)) + list(reversed(third_segment))
    return solution