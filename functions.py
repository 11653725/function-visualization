import numpy as np


def lin(x, a, b):
    return a * x + b


def quad(x, a, b, c):
    return a * x**2 + b * x + c


def sin(x):
    return np.sin(x)


def cos(x):
    return np.cos(x)


def exp(x):
    return np.exp(x)