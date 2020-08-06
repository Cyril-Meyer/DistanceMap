import math
from numba import jit


@jit(nopython=True)
def manhattan_distance(p1, p2):
    """
    Precondition: p1 and p2 are same length
    :param p1: point 1 tuple coordinate
    :param p2: point 2 tuple coordinate
    :return: manhattan distance between two points p1 and p2
    """
    distance = 0
    for dim in range(len(p1)):
        distance += abs(p1[dim] - p2[dim])
    return distance


@jit(nopython=True)
def euclidean_distance(p1, p2):
    """
    Precondition: p1 and p2 are same length
    :param p1: point 1 tuple coordinate
    :param p2: point 2 tuple coordinate
    :return: euclidean distance between two points p1 and p2
    """
    distance = 0
    for dim in range(len(p1)):
        distance += (p1[dim] - p2[dim])**2
    return math.sqrt(distance)