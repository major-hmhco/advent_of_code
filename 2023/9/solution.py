#!python3

with open("./input.txt") as f:
    ipt = [x.strip() for x in f.readlines()] 

running = 0
for line in ipt:
    nums = [int(x) for x in line.split()] 
    delta = [nums[n] - nums[n-1] for n in range(1, len(nums))]
    deltas = [delta]
    while not all([delta[n] == 0 for n in range(0, len(delta))]):
        delta = [delta[n] - delta[n-1] for n in range(1, len(delta))]
        deltas.append(delta)
    for n in range(len(deltas) -1, 0, -1):
        deltas[n-1].append(deltas[n-1][-1] + deltas[n][-1])
    running += nums[-1] + deltas[0][-1]
    


print(f"Pt1: {running}")



running = 0
for line in ipt:
    nums = list(reversed([int(x) for x in line.split()]))
    delta = [nums[n] - nums[n-1] for n in range(1, len(nums))]
    deltas = [delta]
    while not all([delta[n] == 0 for n in range(0, len(delta))]):
        delta = [delta[n] - delta[n-1] for n in range(1, len(delta))]
        deltas.append(delta)
    for n in range(len(deltas) -1, 0, -1):
        deltas[n-1].append(deltas[n-1][-1] + deltas[n][-1])
    running += nums[-1] + deltas[0][-1]

print(f"Pt2: {running}")
