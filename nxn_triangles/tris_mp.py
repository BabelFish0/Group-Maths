import time
import matplotlib.pyplot as plt
import numpy
import math
from numba import njit, prange

triangleSides = []
#times = []

@njit(parallel = True)
def findTris(n):
    triangleSides = []
    #t1 = time.perf_counter()
    for x1 in range(n+1):
        for y1 in range(n+1):
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
    #print(n)
    t1 = time.perf_counter()
    print(len(findTris(n)), end='   ')
    t2 = time.perf_counter()
    print(str(t2-t1) + 's', end='   ')
    timeCount += t2-t1
    print(str(timeCount) + 's')