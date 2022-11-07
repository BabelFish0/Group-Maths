import time
import matplotlib.pyplot as plt
import numpy
import math
from numba import njit, prange
from multiprocessing import Pool

triangleSides = []
#times = []
#@njit(parallel = False)

def findTris(polyArg):
    '''
    run by each process.
    finds all unique trianlges in grid n x n where:
    point 1 = (0, 0)
    point 2 = (x1, n)
    point 3 = every point in n x n grid
    triangleSides is list of currently known sets of side lengths for unique trianlges w/o repeats
    '''
    x1Start = polyArg[0]
    x1End = polyArg[1]
    n = polyArg[2]
    triangleSides = polyArg[3]
    newTris = []
    y1 = n
    for x2 in range(n+1):
        for y2 in range(n+1):
             if (not (x1 == 0 and x2 == 0)) and (not ((x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0))):
                if not(x1 == 0 or x2 == 0):
                     if y1/x1 != y2/x2:
                        if sorted([(x1-x2)**2 + (y1-y2)**2, x1**2 + y1**2, x2**2 + y2**2]) not in triangleSides:
                            newTris.append(sorted([(x1-x2)**2 + (y1-y2)**2, x1**2 + y1**2, x2**2 + y2**2]))
                else:
                    if sorted([(x1-x2)**2 + (y1-y2)**2, x1**2 + y1**2, x2**2 + y2**2]) not in triangleSides:
                        newTris.append(sorted([(x1-x2)**2 + (y1-y2)**2, x1**2 + y1**2, x2**2 + y2**2]))
    return numpy.unique(newTris, axis=0)

def encodeArgs(n, triangleSides, processCount):
    if n/processCount < 1:
        x1Start = 0
        x1End = n
        return [x1Start, x1End, n, triangleSides]
    else:
        if n % processCount == 0:
            args = []
            for chunk in range(n/processCount):
                x1Start = n/processCount * chunk
                x1End = x1Start + n/processCount * chunk - 1
                args.append([x1Start, x1End, n, triangleSides])
            return args
        remainder = n % (processCount-1)
        args = []
        processCount -= 1
        for chunk in range(n//(processCount)):
            x1Start = n/processCount * chunk
            x1End = x1Start + n/processCount * chunk - 1
            args.append([x1Start, x1End, n, triangleSides])
        args.append([n-remainder, n-1, n, triangleSides])
        return args


if __name__ == '__main__':
    with Pool(processes=4) as pool:
        pool.imap_unordered(findTris, args)

        #[2, 4, 10, [[2, 4, 5], [6, 8, 7]]]