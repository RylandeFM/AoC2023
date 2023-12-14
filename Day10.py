with open("Input/Day 10.txt", "r") as f: inputString = f.read().splitlines()

interestingPoints, translation = {}, {"|": [(0, -1), (0, 1)], "-": [(-1, 0), (1, 0)], "L": [(0, -1), (1, 0)], "J": [(0, -1), (-1, 0)], "F": [(0, 1), (1, 0)], "7": [(0, 1), (-1, 0)]}
for y, line in enumerate(inputString):
    for x, c in enumerate(line):
        if c != ".": interestingPoints[(x, y)] = c
        if c == "S": start = (x, y) 
        
def huntAnimal():
    loopNodes = set()
    
    #find a relevant start node in the cardinal directions
    if (start[0] - 1, start[1]) in interestingPoints.keys() and interestingPoints[(start[0] - 1, start[1])] in ["-", "F", "L"]: 
        node = (start[0] - 1, start[1], start[0], start[1])
    elif (start[0] + 1,start[1]) in interestingPoints.keys() and interestingPoints[(start[0] + 1, start[1])] in ["-", "J", "7"]: 
        node = (start[0] + 1, start[1], start[0], start[1])
    elif (start[0], start[1] - 1) in interestingPoints.keys() and interestingPoints[(start[0], start[1] - 1)] in ["|", "F", "7"]: 
        node = (start[0], start[1] - 1, start[0], start[1])
    elif (start[0], start[1] + 1) in interestingPoints.keys() and interestingPoints[(start[0], start[1] + 1)] in ["|", "L", "J"]: 
        node = (start[0], start[1] + 1, start[0], start[1])
        
    #get all the nodes on the loop
    while (node[0], node[1]) in interestingPoints.keys():
        loopNodes.add((node[0], node[1]))
        if interestingPoints[(node[0], node[1])] == "S": 
            break
        for t in translation[interestingPoints[(node[0], node[1])]]:
            if (node[0] + t[0], node[1] + t[1]) != (node[2], node[3]): newNode = (node[0] + t[0], node[1] + t[1], node[0], node[1])
        node = newNode
    
    print(len(loopNodes) // 2) #part one answer, furthest point is half the length of the loop

    withinLoop = 0    

    for x in range(min([x[0] for x in loopNodes]), max([x[0] for x in loopNodes]) + 1):
        for y in range(min([x[0] for x in loopNodes]), max([x[1] for x in loopNodes]) + 1):
            if (x, y) not in loopNodes: 
                leftWalls = len([dx for dx in range(0, x) if (dx, y) in loopNodes and interestingPoints[(dx, y)] in ["|", "L", "J"]])
                if leftWalls > 0 and leftWalls % 2 == 1: withinLoop += 1
    
    print(withinLoop)

huntAnimal()