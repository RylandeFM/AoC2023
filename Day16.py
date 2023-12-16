with open("Input/Day 16.txt", "r") as f: inputString = f.read().splitlines()

floorMap, directions = [[c for c in line]for line in inputString], {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
        
def energizeFloor(start):
    energized, toVisit, visited = set(), [], set()
    toVisit.append(start)
    while toVisit:
        current = toVisit.pop()
        if current[0] not in range(0, len(floorMap[0])) or current[1] not in range(0, len(floorMap)) or current in visited: continue
        energized.add((current[0], current[1]))
        visited.add(current)
        newX, newY = current[0] + directions[current[2]][0], current[1] + directions[current[2]][1]

        match floorMap[current[1]][current[0]]:
            case ".":
                toVisit.append((newX, newY, current[2]))
            case "\\":
                match current[2]:
                    case "L":
                        toVisit.append((current[0], current[1] - 1, "U"))
                    case "R":
                        toVisit.append((current[0], current[1] + 1, "D"))
                    case "U":
                        toVisit.append((current[0] - 1, current[1], "L"))
                    case "D":
                        toVisit.append((current[0] + 1, current[1], "R"))
            case "/":
                match current[2]:
                    case "L":
                        toVisit.append((current[0], current[1] + 1, "D"))
                    case "R":
                        toVisit.append((current[0], current[1] - 1, "U"))
                    case "U":
                        toVisit.append((current[0] + 1, current[1], "R"))
                    case "D":
                        toVisit.append((current[0] - 1, current[1], "L"))
            case "|":
                if current[2] in "LR":
                    toVisit.append((current[0], current[1] + 1, "D"))
                    toVisit.append((current[0], current[1] - 1, "U"))
                else:
                    toVisit.append((newX, newY, current[2]))
            case "-":
                if current[2] in "UD":
                    toVisit.append((current[0] - 1, current[1], "L"))
                    toVisit.append((current[0] + 1, current[1], "R"))
                else:
                    toVisit.append((newX, newY, current[2]))
    
    return len(energized)

def findMaxEnergy():
    rights = max([energizeFloor((0, y, "R")) for y in range(len(inputString))])
    lefts = max([energizeFloor((len(inputString[0]) - 1, y, "L")) for y in range(len(inputString))])
    downs = max([energizeFloor((x, 0, "D")) for x in range(len(inputString[0]))])
    ups = max([energizeFloor((x, len(inputString) - 1, "U")) for x in range(len(inputString[0]))])
    return max(rights, lefts, downs, ups)

print(energizeFloor((0, 0, "R")))
print(findMaxEnergy())