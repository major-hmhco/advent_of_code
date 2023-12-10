#!python3 

with open("./input.txt") as f:
    ipt = [x.strip() for x in f.readlines()] 


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

#### pt2 
steps = set(steps)

def onPath(row, col):
    return (row, col) in steps 

## make visualisation easier
def printGrid(grid):
    for line in grid:
        print(*line, sep="")

grid = [["." if onPath(row, col) else "G" for col, _ in enumerate(ipt[row])] for row, _ in enumerate(ipt)]

#### let's try counting how many times we transition from outside to inside 
count = 0
for row in range(len(ipt)):
    inside = False 
    for col in range(len(ipt[row])):
        ## if the point is on the loop
        if onPath(row, col): 
            ## and the point forms a vertical 
            if ipt[row][col] in "|JLS":
                ## flip from inside to outside or vice-versa
                inside = not inside 
        ## if the point is not on the grid, add 1 if inside, or 0 if outside
        else: 
            count += inside 
            grid[row][col] = "I" if inside else "O"
        
printGrid(grid)
print(f"Pt2: {count}")

