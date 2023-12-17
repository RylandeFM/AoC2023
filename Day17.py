from heapq import heappush, heappop

with open("Input/Day 17.txt", "r") as f: inputString = f.read().splitlines()

heatMap = [[int(c) for c in line] for line in inputString]
transformations = {"S": [(1, 0, "LR"), (0, 1, "UD")], "UD": [(1, 0, "LR"), (-1, 0, "LR")], "LR": [(0, 1, "UD"), (0, -1, "UD")]}

def giveStates(node, dist, minReps, maxReps):
    x, y, direction = node
    
    for t in transformations[direction]:
        newDist, newX, newY, dx, dy = dist, x, y, t[0], t[1]
        for i in range(maxReps):
            newX += dx
            newY += dy
            if newX not in range(len(inputString[0])) or newY not in range(len(inputString)): break
            newDist += heatMap[newY][newX]
            if i >= minReps - 1: yield ((newX, newY, t[2]), newDist)

def getBestPath(minReps, maxReps):
    toVisit, start, visited = [], (0, 0, "S"), {}
    visited[start] = 0
    heappush(toVisit, (0, start))
    
    while toVisit:
        dist, current = heappop(toVisit)
        
        if current in visited.keys() and dist > visited[current]: continue
        
        for newNode, nodeDist in giveStates(current, dist, minReps, maxReps):
            if (newNode in visited.keys() and nodeDist < visited[newNode]) or newNode not in visited.keys():
                visited[newNode] = nodeDist
                heappush(toVisit, (nodeDist, newNode))

    print(min([dist for (x, y, _), dist in visited.items() if x == len(inputString[0]) - 1 and y == len(inputString) - 1]))
    
getBestPath(0, 3)
getBestPath(4, 10)