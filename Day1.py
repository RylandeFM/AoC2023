import re

with open("Input/Day 1.txt", "r") as f: inputString = f.read().splitlines()

def partOne():
    numbers = [[y for y in x if y.isnumeric()] for x in inputString]
    print(sum([int(x[0] + x[-1]) for x in numbers]))

''' Initial attempt
def partTwo():
    sum, replaces = 0, {"one":'1',"two":'2',"three":'3',"four":'4',"five":'5',"six":'6',"seven":'7',"eight":'8',"nine":'9'}
    for line in inputString:
        number = ["0", "0"]
        for i in range(len(line)):
            if line[i].isnumeric():
                number[0] = line[i]
                break
            elif any(num in line[:i+1] for num in replaces.keys()):
                number[0] = [replaces[num] for num in replaces.keys() if num in line[:i+1]][0]
                break
        for i in range(len(line))[::-1]:
            if line[i].isnumeric():
                number[1] = line[i]
                break
            elif any(num in line[i:] for num in replaces.keys()):
                number[1] = [replaces[num] for num in replaces.keys() if num in line[i:]][0]
                break
        sum += int(number[0]+number[1])
    print(sum)
'''

def partTwo():
    sum, replaces = 0, {"one":'1',"two":'2',"three":'3',"four":'4',"five":'5',"six":'6',"seven":'7',"eight":'8',"nine":'9'}
    for line in inputString:
        numbers = re.findall('(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))',line)
        sum += int((numbers[0] if numbers[0].isnumeric() else replaces[numbers[0]]) + (numbers[-1] if numbers[-1].isnumeric() else replaces[numbers[-1]]))
    print(sum)
        
partOne()
partTwo()