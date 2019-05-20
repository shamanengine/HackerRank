

def removeObstacle(numRows, numColumns, lot):
    # WRITE YOUR CODE HERE
    '''
    if numRows < 1 or numColumns > 1000 or numColumns < 1:
        return -1

    for row in range(numRows):
        for col in range(numColumns):
            if lot[row][col] == 9:
                return row + col

    return -1
    '''
    from collections import deque
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

    return solve((0, 0), p)


a = removeObstacle(5,4, [[1, 1, 1, 1],
       [0, 1, 1, 1],
       [0, 1, 0, 1],
       [1, 1, 9, 1],
       [0, 0, 1, 1]])

print(a)