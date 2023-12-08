#!python3 

with open('./input.txt') as f: 
    ipt = [x.strip() for x in f.readlines()]

#### pt1 
instrs = ipt[0] 
nodes = {} 
for line in ipt[2:]: 
    parts = line.split(" = ")
    nexts = parts[1].split(", ") 
    nexts[0] = nexts[0][1:]
    nexts[1] = nexts[1][:-1]
    nodes[parts[0]] = (nexts[0], nexts[1])

steps = 0
node = 'AAA'
while not node == 'ZZZ': 
    direction = instrs[steps % len(instrs)]
    node = nodes[node][0 if direction == 'L' else 1]
    steps += 1 
print(f"Pt1: {steps}")


#### pt2 
def solver(start):
    steps = 0
    node = start
    while not node.endswith('Z'):
        direction = instrs[steps % len(instrs)]
        node = nodes[node][0 if direction == 'L' else 1]
        steps += 1
    return steps 

## this is a lowest common multiple problem - we have a stdlib for that!
import math
answer = 1
for start in nodes: 
    if start.endswith('A'):
        answer = math.lcm(answer, solver(start))
print(f"Pt2: {answer}") 

