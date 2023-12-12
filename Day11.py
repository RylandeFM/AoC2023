from itertools import combinations

with open("Input/Day 11.txt", "r") as f: inputString = f.read().splitlines()

galaxies = []
for y, line in enumerate(inputString):
    for x, c in enumerate(line):
        if c == "#": galaxies.append((x, y))
        
def galaxyLength(expansion):
    newGalaxies = galaxies    

    emptyColumns = [z for z in range(len(inputString[0])) if z not in set([g[0] for g in newGalaxies])]
    emptyRows = [z for z in range(len(inputString[0])) if z not in set([g[1] for g in newGalaxies])]

    for c in sorted(emptyColumns, reverse=True): newGalaxies = [(g[0] + expansion, g[1]) if g[0] > c else g for g in newGalaxies]
    for r in sorted(emptyRows, reverse=True): newGalaxies = [(g[0], g[1] + expansion) if g[1] > r else g for g in newGalaxies]

    print(sum([abs(newGalaxies[c[0]][0] - newGalaxies[c[1]][0]) + abs(newGalaxies[c[0]][1] - newGalaxies[c[1]][1]) for c in list(combinations(range(len(newGalaxies)), 2))]))
    
galaxyLength(1)
galaxyLength(999999)