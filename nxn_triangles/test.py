lt = [[1, 3, 5], [3, 3, 2], [3, 3, 2], [2, 5, 7]]
remList = []

for triIndex, tri in enumerate(lt):
    if lt.index(tri, triIndex+1) != triIndex:
        remList.append(tri)
    print(lt)

for item in remList:
    lt.remove(item)
    print()