#!python3 

with open("./input.txt") as f:
    ipt = [x.strip() for x in f.readlines()] 

## to avoid edge boundaries, add "." wrappers around all input
ipt = ["." + row + "." for row in ipt]
ipt = ["." * len(ipt[0])] + ipt + ["." * len(ipt[0])]


#### pt1 

directions = {
    "-": [(0, 1), (0, -1)],
    "|": [(1, 0), (-1, 0)],
    "L": [(0, 1), (-1, 0)],
    "F": [(0, 1), (1, 0)],
    "7": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
}

## find our starting index 
for row, chars in enumerate(ipt): 
    start = [col for col, char in enumerate(chars) if char == "S"]
    if len(start):
        col = start[0]
        break
start = (row, col)
steps = [start]

## get my first step 
if ipt[row][col+1] in "J-7":
    current = (row, col+1)
elif ipt[row][col-1] in "L-F":
    current = (row, col-1)
elif ipt[row+1][col] in "|F7":
    current = (row+1, col)
elif ipt[row-1][col] in "|LJ":
    current = (row-1, col)

prev = start 
while current != start: 
    steps.append(current)
    (row, col) = current
    pipe = ipt[row][col]
    for (step_row, step_col) in directions[pipe]:
        nxt = (row + step_row, col + step_col) 
        if nxt != prev:
            prev = current 
            current = nxt 
            break 
print(f"Pt1: {len(steps) // 2}")



