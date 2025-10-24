import numpy as np

def multadd_func(a, b):
    temp = np.add(a, b)
    y1 = np.multiply(2, temp)
    y2 = np.multiply(3, temp)
    return int(y1), int(y2)
