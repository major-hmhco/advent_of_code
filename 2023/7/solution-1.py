#!python3

with open('./input.txt') as f: 
    ipt = [x.strip() for x in f.readlines() if x.strip() != '']



#### pt1 
import collections 

labels = {k: i for i, k in enumerate(reversed(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]))}
types = {k: i for i, k in enumerate(reversed(["five", "four", "house", "three", "twopair", "pair", "high"]))}

def parseHands(ipt):
    hands = [] 
    for line in ipt: 
        hand, bid = line.split() 
        hands.append({
            'hand': hand, 
            'bid': int(bid),
            'handType': types[getHandType(hand)],
            'handLabels': [labels[c] for c in hand],
        })
    return hands 

def getHandType(hand): 
    counter = collections.Counter(hand)
    num = len(counter)
    if num == 1:
        return 'five'
    elif num == 2:
        if 4 in counter.values():
            return 'four'
        else:
            return 'house'
    elif num == 3:
        if 2 in counter.values():
            return 'twopair'
        else: 
            return 'three'
    elif num == 4:
        return 'pair' 
    else: 
        return 'high' 

def comparator(h1, h2):
    if h1['handType'] == h2['handType']:
        for char in range(0, len(h1['hand'])):
            h1c = h1['hand'][char] 
            h2c = h2['hand'][char]
            if h1c != h2c:
            ## i really hope they haven't got any equal-ranked hands
            ## as that would lead to there being _options_ for the answer
            ## depending on how you order them 
                return labels[h1c] - labels[h2c]
    else:
        return h1['handType'] - h2['handType']


hands = parseHands(ipt)
ranked = sorted(hands, key=lambda x: (x['handType'], x['handLabels']))
returns = sum([x['bid'] * (i+1) for i, x in enumerate(ranked)])
print(f"Pt1: {returns}")

