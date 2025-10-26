import numpy as np

def transform_array(array):
    out = np.square(array)
    out1 = [0] * len(out)
    for i in range(len(out)):
        out1[i] = int(out[i])
    return out1
