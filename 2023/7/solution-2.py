#!python3

with open('./input.txt') as f: 
    ipt = [x.strip() for x in f.readlines() if x.strip() != '']



#### pt2
import collections 
from functools import cmp_to_key

labels = {k: i for i, k in enumerate(reversed(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]))}
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
    jokers = counter['J']
    if num == 1:
        return 'five'
    elif num == 2:
        if jokers: 
            return 'five'
        if 4 in counter.values():
            return 'four'
        else:
            return 'house'
    elif num == 3:
        if 2 in counter.values():
            if jokers == 2: 
                return 'four'
            if jokers == 1: 
                return 'house'
            return 'twopair'
        else: 
            if jokers: 
                return 'four'
            return 'three'
    elif num == 4:
        if jokers:
            return 'three'
        return 'pair' 
    else: 
        if jokers: 
            return 'pair'
        return 'high' 

hands = parseHands(ipt)
ranked = sorted(hands, key=lambda x: (x['handType'], x['handLabels']))
returns = sum([x['bid'] * (i+1) for i, x in enumerate(ranked)])
print(f"Pt2: {returns}")

