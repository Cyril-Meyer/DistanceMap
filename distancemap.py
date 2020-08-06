import numpy as np

from numba import jit

from distances import manhattan_distance, euclidean_distance
from functions import identity, square, linear


@jit(nopython=True)
def distance_map_2d(map_shape, input_points, distance, omega, alpha):
    dm = np.full(map_shape, omega)

    """
    for p in input_points:
        for x in range(map_shape[0]):
            for y in range(map_shape[1]):
                dm[x,y] = min(dm[x, y], alpha(distance(((x,y)), (p[0], p[1]))))
    """

    for p in input_points:
        x_min = 0
        x_max = map_shape[0]
        y_min = 0
        y_max = map_shape[1]

        for x in range(p[0], 0, -1):
            if alpha(distance((x, p[1]), (p[0], p[1]))) > omega:
                x_min = x
                break
        for x in range(p[0], map_shape[0]):
            if alpha(distance((x, p[1]), (p[0], p[1]))) > omega:
                x_max = x
                break

        for y in range(p[1], 0, -1):
            if alpha(distance((p[0], y), (p[0], p[1]))) > omega:
                y_min = y
                break
        for y in range(p[1], map_shape[1]):
            if alpha(distance((p[0], y), (p[0], p[1]))) > omega:
                y_max = y
                break

        for x in range(x_min, x_max):
            for y in range(y_min, y_max):
                dm[x, y] = min(dm[x, y], alpha(distance((x, y), (p[0], p[1]))))

    return dm


@jit(nopython=True)
def distance_map_3d(map_shape, input_points, distance, omega, alpha):
    dm = np.full(map_shape, omega)

    for p in input_points:
        x_min = 0
        x_max = map_shape[0]
        y_min = 0
        y_max = map_shape[1]
        z_min = 0
        z_max = map_shape[2]

        for x in range(p[0], 0, -1):
            if alpha(distance((x, p[1], p[2]), (p[0], p[1], p[2]))) > omega:
                x_min = x
                break
        for x in range(p[0], map_shape[0]):
            if alpha(distance((x, p[1], p[2]), (p[0], p[1], p[2]))) > omega:
                x_max = x
                break

        for y in range(p[1], 0, -1):
            if alpha(distance((p[0], y, p[2]), (p[0], p[1], p[2]))) > omega:
                y_min = y
                break
        for y in range(p[1], map_shape[1]):
            if alpha(distance((p[0], y, p[2]), (p[0], p[1], p[2]))) > omega:
                y_max = y
                break

        for z in range(p[2], 0, -1):
            if alpha(distance((p[0], p[1], z), (p[0], p[1], p[2]))) > omega:
                z_min = z
                break
        for z in range(p[2], map_shape[2]):
            if alpha(distance((p[0], p[1], z), (p[0], p[1], p[2]))) > omega:
                z_max = z
                break

        for x in range(x_min, x_max):
            for y in range(y_min, y_max):
                for z in range(z_min, z_max):
                    dm[x, y, z] = min(dm[x, y, z], alpha(distance((x, y, z), (p[0], p[1], p[2]))))

    return dm


def distance_map(map_shape, input_points, distance="euclidean", omega=255, alpha="identity"):
    """
    precondition :  1 <= len(map_shape) <= 3
                    input_points not empty
    """

    distance_function = euclidean_distance
    if distance == "manhattan":
        distance_function = manhattan_distance
    elif not (distance == "euclidean"):
        print("WARN: invalid distance name, set default distance (euclidean)")

    alpha_function = identity
    if alpha == "square":
        alpha_function = square
    elif alpha == "linear":
        alpha_function = linear
    elif not (alpha == "identity"):
        print("WARN: invalid alpha function name, set default alpha function (identity)")

    if len(map_shape) == 2:
        return distance_map_2d(map_shape, input_points, distance_function, omega, alpha_function)
    if len(map_shape) == 3:
        return distance_map_3d(map_shape, input_points, distance_function, omega, alpha_function)
    else:
        return np.zeros(map_shape)


# replace np.argwhere (not used because not efficient after tests)
@jit(nopython=True)
def jit_np_argwhere(input):
    return np.argwhere(input)


def distance_map_from_binary_matrix(input_matrix, distance="euclidean", omega=255, alpha="identity"):
    """
    :param input_matrix:
    :param distance:
    :param omega:
    :param alpha:
    :return:
    """
    points = np.argwhere(input_matrix)
    return distance_map(input_matrix.shape, points, distance, omega, alpha)
