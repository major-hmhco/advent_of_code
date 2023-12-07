## load input
with open('./input.txt') as f: 
    ipt = f.readlines() 

## pt1
def parseLine(line):
    parts = line.split(":")
    gameNo = int(parts[0].lstrip("Game "))
    draws = [parseDraw(draw) for draw in parts[1].split(";")]
    return gameNo, draws

def parseDraw(draw):
    colours = draw.split(",")
    colourCounts = {}
    for colour in colours: 
        bits = colour.strip().split(" ")
        colourCounts[bits[1]] = int(bits[0])
    return colourCounts

def checkDrawInvalid(load, draw): 
    for colour, maxNum in load.items():
        if draw.get(colour, 0) > maxNum:
            return True
    return False

pt1load = {
    "red": 12, 
    "green": 13,
    "blue": 14
}

running = 0
for line in ipt:
    gameNo, lineDraws = parseLine(line)
    if not any([checkDrawInvalid(pt1load, draw) for draw in lineDraws]):
        running += gameNo
print(f"Pt1: {running}") 


## pt2
def getMinimalSetPower(lineDraws):
    reds = max([draw.get("red", 0) for draw in lineDraws])
    blues = max([draw.get("blue", 0) for draw in lineDraws])
    greens = max([draw.get("green", 0) for draw in lineDraws])
    return reds * blues * greens 

running = 0
for line in ipt:
    _, lineDraws = parseLine(line)
    running += getMinimalSetPower(lineDraws)
print(f"Pt2: {running}")
