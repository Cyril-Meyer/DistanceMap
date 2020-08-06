import math
from numba import jit

global A, B
A = 1
B = 0


def set_a(a):
    global A
    A = a


def set_b(b):
    global B
    B = b


@jit(nopython=True)
def identity(x):
    return x


@jit(nopython=True)
def square(x):
    return x**2


@jit(nopython=True)
def linear(x):
    return A*x + B
