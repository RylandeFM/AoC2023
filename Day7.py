from collections import Counter

with open("Input/Day 7.txt", "r") as f: inputString = f.read().splitlines()

cards = []

for line in inputString: cards.append([line.split(" ")[0], int(line.split(" ")[1])])
    
def partOne():
    translatedCards, translationTable = [], {'2':'0','3':'1','4':'2','5':'3','6':'4','7':'5','8':'6','9':'7','T':'8','J':'9','Q':'A','K':'B','A':'C'}
    for card in cards:
        newCard = card[0].translate(str.maketrans(translationTable))
        cardProfile = "".join(map(str,sorted(Counter(newCard).values(), reverse=True)))
        match cardProfile:
            case "5": newCard = "7" + newCard #five of a kind
            case "41": newCard = "6" + newCard #four of a kind
            case "32": newCard = "5" + newCard #full house
            case "311": newCard = "4" + newCard #three of a kind
            case "221": newCard = "3" + newCard #two pair
            case "2111": newCard = "2" + newCard #one pair
            case "11111": newCard = "1" + newCard #high card
        translatedCards.append([newCard, card[1], int(newCard, 13)])    

    print(sum([(i+1) * x[1] for i, x in enumerate(sorted(translatedCards, key=lambda x: x[2]))]))

def partTwo():
    translatedCards, translationTable = [], {'2':'1','3':'2','4':'3','5':'4','6':'5','7':'6','8':'7','9':'8','T':'9','J':'0','Q':'A','K':'B','A':'C'}
    for card in cards:
        newCard = card[0].translate(str.maketrans(translationTable))
        occurrences = Counter(newCard)
        if '0' in occurrences.keys(): # there is a Joker so we need to change the profile
            noJokers, toAdd = [], occurrences['0']
            for key in occurrences.keys():
                if key != '0': noJokers.append(occurrences[key])
            noJokers = sorted(noJokers, reverse=True)
            if len(noJokers) == 0: #hand with all Jokers 
                cardProfile = "5"
            else:
                noJokers[0] += toAdd
                cardProfile = "".join(map(str, noJokers))
        else:
            cardProfile = "".join(map(str,sorted(occurrences.values(), reverse=True)))
        match cardProfile:
            case "5": newCard = "7" + newCard #five of a kind
            case "41": newCard = "6" + newCard #four of a kind
            case "32": newCard = "5" + newCard #full house
            case "311": newCard = "4" + newCard #three of a kind
            case "221": newCard = "3" + newCard #two pair
            case "2111": newCard = "2" + newCard #one pair
            case "11111": newCard = "1" + newCard #high card
        translatedCards.append([newCard, card[1], int(newCard, 13)])    

    print(sum([(i+1) * x[1] for i, x in enumerate(sorted(translatedCards, key=lambda x: x[2]))]))

partOne()
partTwo()