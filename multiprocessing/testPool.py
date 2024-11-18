from multiprocessing import Pool
import numpy as np
import random
import os

def f(x):
    return x*x

if __name__ == '__main__':
    random_floats = [random.random() for _ in range(100000)]
    # print(random_floats)

    with Pool(5) as p:
        results = p.map(f, random_floats)
        print(os.name, len(results))
