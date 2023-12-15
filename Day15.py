with open("Input/Day 15.txt", "r") as f: inputString = f.read().split(",")

def getHashValue(str):
    value = 0
    for c in str: value = ((value + ord(c)) * 17) % 256
    return value

def findFocusingPower():
    print(sum([getHashValue(x) for x in inputString])) #part One
    boxes, powers = {}, {}
    for i in range(256): boxes[i] = []
    for op in inputString:
        lensId, power = op.split("=") if "=" in op else [op[:-1], 0]
        lensHash = getHashValue(lensId)
        if "-" in op:
            if lensId in boxes[lensHash]: boxes[lensHash].remove(lensId)
        else:
            if lensId not in boxes[lensHash]: boxes[lensHash].append(lensId)
            powers[lensId] = int(power)
    print(sum([sum([(i + 1) * ((j + 1) * powers[lensId]) for j, lensId in enumerate(box)]) for i, box in enumerate(boxes.values())]))
    
findFocusingPower()