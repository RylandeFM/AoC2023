with open("Input/Day 13.txt", "r") as f: inputStrings = f.read().split("\n\n")

patterns = [[line for line in inputString.split("\n")] for inputString in inputStrings]

def getMirrorRow(intList, targetDifferences):
    for i in range(1, len(intList)):
        if sum(sum(1 for dx, dy in zip(x, y) if dx != dy) for x, y in zip(intList[i-min(i, len(intList) - i):i], 
                                                                          intList[i:i+min(i, len(intList) - i)][::-1])) == targetDifferences: return i
    return 0

def findMirrors(targetDifferences):  
    print((sum([getMirrorRow([line for line in pattern], targetDifferences) for pattern in patterns]) * 100) + 
          sum([getMirrorRow(["".join([pattern[i][j] for i in range(len(pattern))]) for j in range(len(pattern[0]))], targetDifferences) for pattern in patterns]))
        
findMirrors(0)
findMirrors(1)