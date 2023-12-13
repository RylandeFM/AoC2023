with open("Input/Day 13.txt", "r") as f: inputStrings = f.read().split("\n\n")

patterns = [[line for line in inputString.split("\n")] for inputString in inputStrings]

def getMirrorRow(intList, target):
    for i in range(1, len(intList)):
        #see how far to the left and right we can go to check for similars, take the lowest bound as we can't see into the unknown
        maxWindow = min(i, len(intList) - i)
        #sum all the different elements in the windows
        if sum(sum(1 for dx, dy in zip(x, y) if dx != dy) for x, y in zip(intList[i-maxWindow:i], intList[i:i+maxWindow][::-1])) == target: return i
    return 0

def findMirrors(target):
    vertical, horizontal = 0,0
    
    for pattern in patterns: 
        horizontalInts = [line for line in pattern]
        verticalInts = ["".join([pattern[i][j] for i in range(len(pattern))]) for j in range(len(pattern[0]))]
        horizontal += getMirrorRow(horizontalInts, target)
        vertical += getMirrorRow(verticalInts, target)
        
    print((horizontal * 100) + vertical)
        
findMirrors(0)
findMirrors(1)