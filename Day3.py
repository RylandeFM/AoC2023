with open("Input/Day 3.txt", "r") as f: inputString = f.read().splitlines()

symbols, numbers, gears = set(), {}, {}

for y, line in enumerate(inputString):
    for x, c in enumerate(line):
        if c.isnumeric() and not line[x - 1].isnumeric():
            z = x
            while z + 1 < len(line) and line[z + 1].isnumeric() : z += 1
            numbers[(x, y)] = {"end": z, "touchingPart": False, "value": int(line[x:z + 1])}
        elif c != "." and not c.isnumeric():
            symbols.add((x, y))
            if c == "*": gears[(x, y)] = {"hits": []}

def checkParts():
    for k, v in numbers.items():
        for x in range(k[0] - 1, v["end"] + 2):
            for y in range(k[1] - 1, k[1] + 2):
                if (x, y) in symbols: 
                    numbers[k]["touchingPart"] = True
                    if (x, y) in gears: gears[(x, y)]["hits"].append(v["value"])
                    break
            if numbers[k]["touchingPart"]: break
    print(sum(x["value"] for x in numbers.values() if x["touchingPart"]))
    print(sum([g["hits"][0] * g["hits"][1] for g in gears.values() if len(g["hits"]) == 2]))
            
checkParts()