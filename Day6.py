import re

with open("Input/Day 6.txt", "r") as f: inputString = f.read().splitlines()

seconds, goals = re.findall("([0-9]+)", inputString[0]), re.findall("([0-9]+)", inputString[1])

def findWays(seconds, goals):
    numberOfWays = 1
    for index, entry in enumerate(seconds):
        for i in range(goals[index] // entry, entry):
            if i * (entry - i) > goals[index]: break
        numberOfWays *= entry - (i * 2) + 1
    print(numberOfWays)

findWays([int(x) for x in seconds], [int(x) for x in goals])
findWays([int("".join(seconds))], [int("".join(goals))])