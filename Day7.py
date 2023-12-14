from collections import Counter

with open("Input/Day 7.txt", "r") as f: inputString = f.read().splitlines()

cards = []

for line in inputString: cards.append([line.split(" ")[0], int(line.split(" ")[1])])

def camelCards(jokersApply, translationTable):
    translatedCards = []
    for card in cards:
        newCard = card[0].translate(str.maketrans(translationTable))
        occurrences = Counter(newCard)
        if '0' in occurrences.keys() and jokersApply: # there is a Joker so we need to change the profile and Joker rules apply
            noJokers, toAdd = [], occurrences['0']
            if occurrences['0'] == 5: 
                cardProfile = "5"
            else:
                for key in occurrences.keys():
                    if key != '0': noJokers.append(occurrences[key])
                noJokers = sorted(noJokers, reverse = True)
                noJokers[0] += toAdd
                cardProfile = "".join(map(str, noJokers))
        else:
            cardProfile = "".join(map(str, sorted(occurrences.values(), reverse = True)))
        match cardProfile:
            case "5": newCard = "7" + newCard # five of a kind
            case "41": newCard = "6" + newCard # four of a kind
            case "32": newCard = "5" + newCard # full house
            case "311": newCard = "4" + newCard # three of a kind
            case "221": newCard = "3" + newCard # two pair
            case "2111": newCard = "2" + newCard # one pair
            case "11111": newCard = "1" + newCard # high card
        translatedCards.append([int(newCard, 13), card[1]])    

    print(sum([(i + 1) * x[1] for i, x in enumerate(sorted(translatedCards, key = lambda x: x[0]))]))

camelCards(False, {'2': '0', '3': '1', '4': '2', '5': '3', '6': '4', '7': '5', '8': '6', '9': '7', 'T': '8', 'J': '9', 'Q': 'A', 'K': 'B', 'A': 'C'})
camelCards(True, {'2': '1', '3': '2', '4': '3', '5': '4', '6': '5', '7': '6', '8': '7', '9': '8', 'T': '9', 'J': '0', 'Q': 'A', 'K': 'B', 'A': 'C'})