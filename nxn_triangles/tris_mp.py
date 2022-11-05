from numba import njit
 
@njit
def project4(n):
   lst = []
   for item in range(1, n + 1):
       coordinates = [(x, y) for x in range(item) for y in range(item)]
       coordinates.remove((0,0))
       combo = []
       for i in range(len(coordinates) - 1):
           for j in range(i + 1, len(coordinates)):
               if item - 1 in coordinates[i] or item - 1 in coordinates[j]:
                   combo.append([coordinates[i], coordinates[j]])
 
       tri = []
       for i in combo:
           if i[0][0] * i[1][1] - i[1][0] * i[0][1] != 0:
               tri.append(i)
              
       distance = []
       for i in tri:
           temp = [i[0][0] ** 2 + i[0][-1] ** 2, (i[0][0] - i[1][0]) ** 2 + (i[0][-1] - i[1][-1]) ** 2, i[1][0] ** 2 + i[1][-1] ** 2]
           temp.sort()
           distance.append(temp)
          
       add_lst = []
       for i in distance:
           if i not in add_lst:
               add_lst.append(i)
       for i in lst:
           if i in add_lst:
               add_lst.remove(i)
      
       for i in add_lst:
           lst.append(i)
       print(len(lst))
