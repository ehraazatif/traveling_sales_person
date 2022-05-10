import random


def _permute(original, left, right):
    """
    :param original: original arrangement of elements
    :param left: left element in original
    :param right: right element in original
    :return: new, which is original with elements left and right switched
    """
    assert left < right

    # generate copy of original
    new = []
    for num in original:
        new.append(num)
    temp = new[right]
    new[right] = new[left]
    new[left] = temp
    return new


def _cycle_weight(cycle, graph):
    """
    :param cycle: the cycle to calculate the weight of
    :param graph: an undirected weighted graph, represented as an adjacency matrix
    :return: the weight of the cycle
    """
    weight = 0
    for i in range(0, len(cycle) - 1):
        v1 = cycle[i]
        v2 = cycle[i + 1]
        weight += graph[v1][v2]
    return weight


def _is_valid_cycle(cycle, graph):
    """
    :param cycle: the cycle to check for validity
    :param graph: an undirected weighted graph, represented as an adjacency matrix
    :return: whether the cycle is valid or not (possible, given the edge set)
    """
    for i in range(0, len(cycle) - 1):
        v1 = cycle[i]
        v2 = cycle[i + 1]
        if graph[v1][v2] == 0:
            return False
    return True


def traveling_sales_person(graph):
    """
    :param graph: an undirected weighted graph, represented as an adjacency matrix
    :return: the Hamiltonian cycle in the graph with the smallest total weight
    """
    assert len(graph) > 1, "Graph must have at least 2 vertices"

    cycles = []
    # generate permutations
    for i in range(0, len(graph)):
        cycle = [i]
        # generate base permutation
        for j in range(0, len(graph)):
            if j != i:
                cycle.append(j)
        cycle.append(i)
        cycles.append(cycle)

        # add the different mutations of base permutation to list of cycles
        right = -2
        left = -3
        for k in range(0, len(cycle) - 3):
            to_add = _permute(cycles[-1], left, right)
            cycles.append(to_add)
            right -= 1
            left -= 1

    # eliminate bad permutations
    i = 0
    while i < len(cycles):
        cycle = cycles[i]
        if _is_valid_cycle(cycle, graph):
            i += 1
        else:
            cycles.pop(i)

    # find cycle with the smallest weight
    min_weight = float("inf")
    min_cycle = None
    for cycle in cycles:
        weight = _cycle_weight(cycle, graph)
        if weight < min_weight:
            min_weight = weight
            min_cycle = cycle

    return min_cycle


def gen_graph(size, lower_limit, upper_limit):
    """
    :param size: the number of vertices
    :param lower_limit: the lowest edge weight
    :param upper_limit:  the highest edge weight
    :return: an undirected weighted graph, represented as an adjacency matrix
    """
    assert lower_limit != 0 and upper_limit != 0, "Either limit cannot be 0, 0 represents no edge in the adjacency matrix"
    assert upper_limit > lower_limit, "Upper limit must be greater than lower limit"
    assert size > 0, "Size = number of vertices, must be greaer than 0"

    # generate range of weights
    weights = []
    for i in range(lower_limit, upper_limit):
        if i != 0:
            weights.append(i)

    # generate weighted, simple, undirected graph with randomly weighted edges
    graph = []
    for i in range(0, size):
        to_add = []
        for j in range(0, size):
            if j == i:
                to_add.append(0)
            else:
                to_add.append(weights[random.randint(0, len(weights) - 1)])
        graph.append(to_add)

    return graph

