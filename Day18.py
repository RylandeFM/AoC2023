with open("Input/Day 18.txt", "r") as f: inputString = f.read().splitlines()

directions = {"R": (1, 0), "U": (0, 1), "D": (0, -1), "L": (-1, 0)}

def diggyHole(useHex):
    edges, edgePoints, current = 0, [] ,(0, 0)
    for line in inputString:
        direction, steps, hexCode = line.split(" ")
        if useHex:
            match hexCode[-2]:
                case '0': direction = "R"
                case '1': direction = "D"
                case '2': direction = "L"
                case '3': direction = "U"
            steps = int(hexCode[2:-2], 16)
        else:
            steps = int(steps)
        t = directions[direction]
        edgePoints.append((current[0] + t[0] * steps, current[1] + t[1] * steps))
        edges += steps
        current = edgePoints[-1]
        
    #Shoelace Formula
    areaInLoop = abs(sum(edgePoints[i][0] * (edgePoints[i - 1][1] - edgePoints[(i + 1) % len(edgePoints)][1]) for i in range(len(edgePoints)))) // 2
    
    #Pick's Theorem
    print(edges + (areaInLoop - edges // 2 + 1))
    
diggyHole(False)
diggyHole(True)