with open('./input.txt') as f:
    ipt = [x.strip() for x in f.readlines()]

#### pt 1
def parseCard(line): 
    parts = line.split(":") 
    cardNo = int(parts[0].lstrip("Card "))
    numbers = parts[1].split("|") 
    winners = [x.strip() for x in numbers[0].split(" ")]
    draw = [x.strip() for x in numbers[1].split(" ")]

    drawWinners = [x for x in draw if x in winners and x != ''] 
    if not len(drawWinners):
        return 0
    return pow(2, len(drawWinners) - 1)

running = 0
for line in ipt:
    running += parseCard(line)
print(f"Pt1: {running}")



#### pt 2
def parseCard(line):
    parts = line.split(":") 
    cardNo = int(parts[0].lstrip("Card "))
    numbers = parts[1].split("|") 
    winners = [y for y in [x.strip() for x in numbers[0].split(" ")] if y != '']
    draw = [y for y in [x.strip() for x in numbers[1].split(" ")] if y != '']
    matches = [x for x in draw if x in winners]
    return cardNo, len(matches)

cards = {i:1 for i in range(1, len(ipt)+1)}
for line in ipt: 
    num, matchCount = parseCard(line)
    for i in range(num + 1, num + matchCount + 1):
        cards[i] += cards[num] 
print(f"Pt2: {sum(cards.values())}") 
