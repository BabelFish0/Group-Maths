import time
import matplotlib.pyplot as plt
import numpy
import math
from numba import njit, prange

triangleSides = [[1, 1, 1]]
#times = []

def remDuplicates(list):
    for tri in list:
        break

#@njit(parallel = False)
def findTris(x1Start, x1End, n, triangleSides):
    '''
    run by each process.
    finds all unique trianlges in grid n x  n where:
    point 1 = (0, 0)
    point 2 = all in range (x1Start - x1End, n)
    point 3 = every point in n x n grid
    triangleSides is list of currently known sets of side lengths for unique trianlges w/o repeats
    '''
    y1 = n
    for x1 in range(x1Start, x1End+1):
        for x2 in range(n+1):
            for y2 in range(n+1):
                if (not (x1 == 0 and x2 == 0)) and (not ((x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0))):
                    if not(x1 == 0 or x2 == 0):
                        if y1/x1 != y2/x2:
                            if sorted([(x1-x2)**2 + (y1-y2)**2, x1**2 + y1**2, x2**2 + y2**2]) not in triangleSides:
                                triangleSides.append(sorted([(x1-x2)**2 + (y1-y2)**2, x1**2 + y1**2, x2**2 + y2**2]))
                    else:
                        if sorted([(x1-x2)**2 + (y1-y2)**2, x1**2 + y1**2, x2**2 + y2**2]) not in triangleSides:
                            triangleSides.append(sorted([(x1-x2)**2 + (y1-y2)**2, x1**2 + y1**2, x2**2 + y2**2]))
    #t2 = time.perf_counter()
    #print("Unique triangles: " + str(len(triangleSides)) + " in " + str(t2-t1) + "s")
    #times.append(t2-t1)
    return triangleSides

timeCount = 0
for n in range(25):
    print(n, end='   ')
    t1 = time.perf_counter()
    print(len(findTris(n, triangleSides)), end='   ')
    t2 = time.perf_counter()
    print(str(t2-t1) + 's', end='   ')
    timeCount += t2-t1
    print(str(timeCount) + 's')