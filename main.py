from TSP.bsa import local_search, multi_start_local_search


def perform(search_type):
    """
    Main TSP module.
    It performs local or multistart search for TSP.

    :param search_type: type of search to be performed
    """

    search_type()


if __name__ == '__main__':
    tsp_problem = 'berlin52'
    perform(lambda: local_search(tsp_problem, draw=True, verbose=False))
    perform(lambda: multi_start_local_search(tsp_problem, 10, draw=True, verbose=False))
