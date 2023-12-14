from time import perf_counter_ns

with open("Input/Day 14.txt", "r") as f: inputString = f.read().splitlines()

rocks, blockers = [], []

for y, line in enumerate(inputString):
    for x, c in enumerate(line):
        if c == "O": rocks.append((x, y))
        if c == "#": blockers.append((x, y))
        
def tumble(rocks, direction):
    newRocks, newBlockers = [], blockers[:]
    if direction[0] != 0:
        rocks = sorted(rocks, key=lambda x: (x[0] if direction[0] == -1 else -x[0], x[1]))
    else:
        rocks = sorted(rocks, key=lambda x: (x[0], x[1] if direction[1] == -1 else -x[1]))
    for rock in rocks:
        while (rock[0] > 0 if direction[0] == -1 else rock[0] < len(inputString[0])-1 if direction[0] != 0 else rock[1] > 0 if direction[1] == -1 else rock[1] < len(inputString)-1) and (rock[0] + direction[0], rock[1] + direction[1]) not in newBlockers:
            rock = (rock[0] + direction[0], rock[1] + direction[1])
        newRocks.append(rock)
        newBlockers.append(rock)
    '''
    for y in range(len(inputString)):
        line = ""
        for x in range(len(inputString[0])):
            if (x, y) in newRocks: line+="O"
            elif (x, y) in blockers: line+="#"
            else: line += "."
        print(line)
    print("\n")
    '''
    return newRocks
    
def partOne():
    print(sum([len(inputString) - r[1] for r in tumble(rocks, (0, -1))]))
    
def partTwo(r):
    rockLayouts, rocks = [], r[:]
    while rocks not in rockLayouts:
        rockLayouts.append(rocks)
        rocks = tumble(tumble(tumble(tumble(rocks,(0,-1)),(-1,0)),(0,1)),(1,0))

    startOfCycle = rockLayouts.index(rocks)
    targetIndex = ((1000000000 - startOfCycle) % (len(rockLayouts) - startOfCycle)) + startOfCycle
    print(sum([len(inputString) - r[1] for r in rockLayouts[targetIndex]]))
    
start = perf_counter_ns()
partOne()
print((perf_counter_ns()-start)/1000000)
start = perf_counter_ns()
partTwo(rocks)
print((perf_counter_ns()-start)/1000000)