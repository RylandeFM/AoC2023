with open("Input/Day 4.txt", "r") as f: inputString = f.read().splitlines()

cards = {}

for i, line in enumerate(inputString):
    numbers = line.split(": ")[1]
    cards[i + 1] = {"winners":[n for n in numbers.split(" | ")[0].split(" ") if n], "numbers":[n for n in numbers.split(" | ")[1].split(" ") if n]}
    
def checkScratchers():
    amounts = {card:1 for card in cards.keys()}
    for index, card in cards.items():
        cards[index]["matches"] = len([n for n in card["winners"] if n in card["numbers"]])
        for i in range(index + 1, index + card["matches"] + 1): amounts[i] += amounts[index]
    print(sum([2 ** (p["matches"]-1) for p in cards.values() if p["matches"] > 0]))
    print(sum(amounts.values()))
    
checkScratchers()