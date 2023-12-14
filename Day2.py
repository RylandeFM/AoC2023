with open("Input/Day 2.txt", "r") as f: inputString = f.read().splitlines()

games = {}

for line in inputString:
    games[int(line[5:].split(":")[0])] = line[5:].split(":")[1].split(";")
    
def playGame():
    gameSum, powerSum = 0, 0
    for i in range(1, len(inputString) + 1):
        colours = {"red": 0, "blue": 0, "green": 0}
        for subGame in games[i]:
            for colour in subGame.strip().split(","):
                entry = colour.strip().split(" ")
                if colours[entry[1]] < int(entry[0]): colours[entry[1]] = int(entry[0])
        if colours["red"] <= 12 and colours["green"] <= 13 and colours["blue"] <= 14: gameSum += i
        powerSum += colours["red"] * colours["green"] * colours["blue"]
    print(gameSum)
    print(powerSum)
                
playGame()