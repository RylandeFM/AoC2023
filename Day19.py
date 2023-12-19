from functools import reduce
from operator import mul

with open("Input/Day 19.txt", "r") as f: inputString = f.read()

instr, parts = inputString.split("\n\n")

parsedInstr = {}
for i in instr.splitlines():
    parsedInstr[i[:i.find("{")]] = i[i.find("{") + 1: -1].split(",")
    
def evaluateXmasRating(x, m, a, s, instr):
    for i in instr[:-1]:
        expr, target = i.split(":")
        if eval(expr): return target if target in "RA" else evaluateXmasRating(x, m, a, s, parsedInstr[target])
    return instr[-1] if instr[-1] in "RA" else evaluateXmasRating(x, m, a, s, parsedInstr[instr[-1]])

def partOne():
    ratingSum = 0

    for part in parts.splitlines():
        partAttr = {}
        for item in part[1: -1].split(","):
            ch, n = item.split("=")
            partAttr[ch] = int(n)
        if evaluateXmasRating(partAttr['x'], partAttr['m'], partAttr['a'], partAttr['s'], parsedInstr["in"]) == "A": 
            ratingSum += sum(partAttr.values())    
           
    print(ratingSum)
    
partOne()

def countSolutions(bounds, name = "in"):
    if name == "R":
        return 0
    if name == "A":
        #range is inclusive on both ends so + 1 to offset
        return reduce(mul, [high - low + 1 for low, high in bounds.values()])
    
    rules, fallback, total = parsedInstr[name][:-1], parsedInstr[name][-1], 0
    
    for rule in rules:
        expr, target = rule.split(":")
        prop, op, bound = expr[0], expr[1], int(expr[2:])
        
        #[Range that applies, Range that doesn't apply]
        splittedRanges = [(bounds[prop][0], bound - 1), (bound, bounds[prop][1])] if op == "<" else [(bound + 1, bounds[prop][1]), (bounds[prop][0], bound)]

        #get total for the range that applies
        copyOfBounds = dict(bounds)
        copyOfBounds[prop] = splittedRanges[0]
        total += countSolutions(copyOfBounds, target)

        #update the remainder with the range that doesn't apply to check later (or by fallback)
        bounds[prop] = splittedRanges[1]
    
    #check whatever is left for the fallback
    total += countSolutions(bounds, fallback)
            
    return total

print(countSolutions({c: (1,4000) for c in "xmas"}))
