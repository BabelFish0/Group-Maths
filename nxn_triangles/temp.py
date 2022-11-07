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

print(encodeArgs(15, [[3, 3, 3], [2, 2, 2]], 4))