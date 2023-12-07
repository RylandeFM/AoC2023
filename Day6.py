import re

with open("Input/Day 6.txt", "r") as f: inputString = f.read().splitlines()

seconds, goals = [int(x) for x in re.findall("([0-9]+)",inputString[0])], [int(x) for x in re.findall("([0-9]+)",inputString[1])]

def findWays(seconds, goals):
    numberOfWays = 1
    for index, entry in enumerate(seconds):
        for i in range(goals[index]//entry, entry):
            if i * (entry-i) > goals[index]: break
        numberOfWays *= len(range(i, entry-i+1))
    print(numberOfWays)

findWays(seconds, goals)
findWays([int("".join(re.findall("([0-9]+)",inputString[0])))], [int("".join(re.findall("([0-9]+)",inputString[1])))])