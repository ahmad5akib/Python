import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers")
    else:
        matrix = np.array(list).reshape(3, 3)

    calculated_val = {}

    mean = [
        (matrix.mean(axis=0).tolist()),
        (matrix.mean(axis=1).tolist()),
        (matrix.flatten().mean().tolist()),
    ]

    variance = [
        (matrix.var(axis=0).tolist()),
        (matrix.var(axis=1).tolist()),
        (matrix.flatten().var().tolist()),
    ]

    std_dev = [
        (matrix.std(axis=0).tolist()),
        (matrix.std(axis=1).tolist()),
        (matrix.flatten().std().tolist()),
    ]

    max = [
        (matrix.max(axis=0).tolist()),
        (matrix.max(axis=1).tolist()),
        (matrix.flatten().max().tolist()),
    ]

    min = [
        (matrix.min(axis=0).tolist()),
        (matrix.min(axis=1).tolist()),
        (matrix.flatten().min().tolist()),
    ]

    sum = [
        (matrix.sum(axis=0).tolist()),
        (matrix.sum(axis=1).tolist()),
        (matrix.flatten().sum().tolist()),
    ]

    calculated_val["mean"] = mean
    calculated_val["variance"] = variance
    calculated_val["standard deviation"] = std_dev
    calculated_val["max"] = max
    calculated_val["min"] = min
    calculated_val["sum"] = sum

    return calculated_val


# print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
