from math import lcm

with open("Input/Day 8.txt", "r") as f: inputString = f.read().splitlines()

instructions, roadMap = inputString[0], {}
for line in inputString[2:]:
    roadMap[line.split(" = ")[0]] = {"L": line.split("(")[1].split(", ")[0], "R": line.split("(")[1].split(", ")[1].split(")")[0]}

def getCycles(startEnding, endEnding):
    startNodes, stepsToEnd = [x for x in roadMap.keys() if x.endswith(startEnding)], []
    for startNode in startNodes:
        currentNode, step = startNode, 0
        while not currentNode.endswith(endEnding):
            currentNode = roadMap[currentNode][instructions[step % len(instructions)]]
            step += 1
        stepsToEnd.append(step)
    print(lcm(*stepsToEnd))
    
getCycles("AAA", "ZZZ")
getCycles("A", "Z")