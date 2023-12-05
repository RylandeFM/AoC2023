import time

with open("Input/Day 5.txt", "r") as f: inputString = f.read()

#parse input
maps, mapIndex, diffMap = {0: []}, 0, {0: []}
inputLines = [n for n in inputString.split("\n") if n]
seeds = [int(x) for x in inputLines[0].split(": ")[1].split(" ")]
inputLines = inputLines[2:]
for line in inputLines:
    if not line[0].isnumeric(): 
        maps[mapIndex] = sorted(maps[mapIndex], key=lambda x: x[1]) #sort maps by source number
        for m in maps[mapIndex]: diffMap[mapIndex].append([m[1],m[1]+m[2]-1,m[0]-m[1]]) #diffmap = start, end, modification
        mapIndex += 1
        maps[mapIndex], diffMap[mapIndex] = [], []
    else:
        maps[mapIndex].append([int(x) for x in line.split(" ")])
maps[mapIndex] = sorted(maps[mapIndex], key=lambda x: x[1])
for m in maps[mapIndex]: diffMap[mapIndex].append([m[1],m[1]+m[2]-1,m[0]-m[1]]) #filling the last diffmap

'''        
def partOne():
    lowestLoc, currentSearch = -1, 0
    for seed in seeds:
        currentSearch = seed
        for m in maps.values():
            for r in m:
                if r[1] <= currentSearch < r[1] + r[2]:
                    currentSearch = currentSearch + (r[0]-r[1])
                    break
        lowestLoc = currentSearch if lowestLoc == -1 else min(lowestLoc, currentSearch)
    print(lowestLoc)
'''

def findLowestLocation(seeds):
    currentRanges = seeds
    for m in diffMap.values():
        newRanges, diffIndex = [], 0
        #determine new ranges
        for r in currentRanges:
            #range to right of map, so we can ignore this map since we're going through a sorted list and the start is past the end of the map
            while diffIndex < len(m)-1 and r[0] > m[diffIndex][1]: diffIndex += 1
            if diffIndex == len(m):
                newRanges.append([r[0], r[1]])
                break
            if r[0] < m[diffIndex][0]: #there is a part to the left of the range that is not captured by a map
                if r[1] < m[diffIndex][0]:
                    newRanges.append([r[0], r[1]]) #range is fully to the left of the map so we add it unchanged an move to the next range
                    break
                else:
                    newRanges.append([r[0], m[diffIndex][0]-1]) #add new range, stays as is because it's not captured by a map
                    r[0] = m[diffIndex][0]
            while diffIndex < len(m) and r[1] > m[diffIndex][1] and r[0] <= m[diffIndex][1]: #range in window as the end of the range is higher than the end of the map but left is higher or equal to start of map
                if r[0] < m[diffIndex][0]: #range is larger than multiple maps, but the maps are not adjacent so we add the part between the maps unchanged
                    newRanges.append([r[0], m[diffIndex][0]-1])
                    r[0] = m[diffIndex][0]
                newRanges.append([r[0]+m[diffIndex][2], m[diffIndex][1]+m[diffIndex][2]])
                r[0] = m[diffIndex][1] + 1
                diffIndex += 1
            if diffIndex == len(m) or r[1] < m[diffIndex][0]: #we've reached the end of the diffmaps or the remaining range is wholly before the next map
                newRanges.append([r[0], r[1]])
            else:
                if r[0] > m[diffIndex][1]:
                    newRanges.append([r[0], r[1]])
                else:
                    if r[1] <= m[diffIndex][1]:
                        newRanges.append([r[0]+m[diffIndex][2], r[1]+m[diffIndex][2]])
                    else:
                        newRanges.append([r[0]+m[diffIndex][2], m[diffIndex][1]+m[diffIndex][2]])
                        newRanges.append([m[diffIndex][1]+1, r[1]])
            
        #sort new ranges
        newRanges = sorted(newRanges, key=lambda x: x[0])
        #set new ranges as current
        currentRanges = newRanges
    print(currentRanges[0][0])

findLowestLocation(sorted([[seeds[i], seeds[i]] for i in range(0, len(seeds))], key=lambda x: x[0]))
findLowestLocation(sorted([[seeds[i], seeds[i]+seeds[i+1]-1] for i in range(0, len(seeds), 2)], key=lambda x: x[0]))