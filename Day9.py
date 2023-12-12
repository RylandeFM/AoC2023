with open("Input/Day 9.txt", "r") as f: inputList = [[int(x) for x in line.split(" ")] for line in f.read().splitlines()]

def getLastElement(r):
    if set(r) == {0}: return 0
    return r[-1] + getLastElement([b - a for a, b in zip(r, r[1:])]) 
    
print(sum([getLastElement(row) for row in inputList]))
print(sum([getLastElement(row[::-1]) for row in inputList]))