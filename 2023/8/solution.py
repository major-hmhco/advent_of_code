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


