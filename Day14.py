with open("Input/Day 14.txt", "r") as f: inputString = f.read().splitlines()

rocks, blockMap = [], [["."] * len(inputString) for _ in range(len(inputString[0]))]

for y, line in enumerate(inputString):
    for x, c in enumerate(line):
        if c == "O": rocks.append((x, y))
        if c == "#": blockMap[y][x] = "#"

def tumbleMapped(rocks, direction):
    newRocks, newBlockMap = [], [row[:] for row in blockMap]
    if direction[0] != 0:
        rocks = sorted(rocks, key=lambda x: (x[0] if direction[0] == -1 else -x[0]))
    else:
        rocks = sorted(rocks, key=lambda x: (x[1] if direction[1] == -1 else -x[1]))
        
    for rock in rocks:
        while (rock[0] > 0 if direction[0] == -1 else rock[0] < len(inputString[0]) - 1 if direction[0] != 0 else rock[1] > 0 if direction[1] == -1 else rock[1] < len(inputString) - 1) and newBlockMap[rock[1] + direction[1]][rock[0] + direction[0]] != "#":
            rock = (rock[0] + direction[0], rock[1] + direction[1])
        newRocks.append(rock)
        newBlockMap[rock[1]][rock[0]] = "#"
    
    return newRocks
    
def tumbleRocks(r):
    print(sum([len(inputString) - rock[1] for rock in tumbleMapped(r, (0, -1))]))
    
    rockLayouts, rocks = [], r[:]
    while rocks not in rockLayouts:
        rockLayouts.append(rocks)
        rocks = tumbleMapped(tumbleMapped(tumbleMapped(tumbleMapped(rocks, (0, -1)), (-1, 0)), (0, 1)), (1, 0))

    startOfCycle = rockLayouts.index(rocks)
    targetIndex = ((1000000000 - startOfCycle) % (len(rockLayouts) - startOfCycle)) + startOfCycle
    print(sum([len(inputString) - r[1] for r in rockLayouts[targetIndex]]))
    
tumbleRocks(rocks)