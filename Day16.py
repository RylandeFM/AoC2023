with open("Input/Day 16.txt", "r") as f: inputString = f.read().splitlines()

floorMap, directions = [[c for c in line]for line in inputString], {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}, 
opposite = {"R": "L", "L": "R", "U":"D", "D": "U"}
        
def energizeFloor(start):
    energized, toVisit, visited, exits = set(), [], set(), set()
    toVisit.append(start)
    while toVisit:
        current = toVisit.pop()
        if current in visited: continue #if we already seen this, we're in a loop and we can stop following it
        #if we're going out bounds, we can remove the exit point from the points to check as it will lead to the same entry point with the same energy
        if current[0] not in range(0, len(floorMap[0])) or current[1] not in range(0, len(floorMap)): 
            toApply = directions[opposite[current[2]]]
            exits.add((current[0] + toApply[0], current[1] + toApply[1], opposite[current[2]]))
            continue
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
    return len(energized), exits

def findMaxEnergy():
    toCheck, energizes = [], []
    for y in range(len(inputString)): 
        toCheck.append((0, y, "R"))
        toCheck.append((len(inputString[0]) - 1, y, "L"))
    for x in range(len(inputString[0])):
        toCheck.append((x, 0, "D"))
        toCheck.append((x, len(inputString) - 1, "U"))
    
    while toCheck:
        energy, toRemove = energizeFloor(toCheck.pop())
        energizes.append(energy)
        for r in toRemove:
            if r in toCheck: toCheck.remove(r)
    print(max(energizes))

print(energizeFloor((0, 0, "R"))[0])
findMaxEnergy()