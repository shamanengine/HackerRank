from collections import deque

'''
# go 0
graph = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
'''

# go 0
graph1 = [[0, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 1, 0],
          [0, 0, 0, 0],
          [1, 1, 0, 0]]

# go 1
lot = [[1, 1, 1, 1],
       [0, 1, 1, 1],
       [0, 1, 0, 1],
       [1, 1, 9, 1],
       [0, 0, 1, 1]]

p = (0, 0)
for i in range(len(lot)):
    for j in range(len(lot[i])):
        if lot[i][j] == 9:
            p = (i, j)

# print(p)

graph = lot

# To move left, right, up and down
delta_x = [-1, 1, 0, 0]
delta_y = [0, 0, 1, -1]


def valid(x, y):
    if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[x]):
        return False
    return (graph[x][y] != 0)


def solve(start, end):
    Q = deque([start])
    dist = {start: 0}
    while len(Q):
        curPoint = Q.popleft()
        curDist = dist[curPoint]
        if curPoint == end:
            return curDist
        for dx, dy in zip(delta_x, delta_y):
            nextPoint = (curPoint[0] + dx, curPoint[1] + dy)
            if not valid(nextPoint[0], nextPoint[1]) or nextPoint in dist.keys():
                continue
            dist[nextPoint] = curDist + 1
            Q.append(nextPoint)


# print(solve((0, 0), (6, 7)))
print(solve((0, 0), (2, 3)))
# print(solve((0, 0), (6, 7)))
