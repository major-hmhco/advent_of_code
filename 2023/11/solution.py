#!python3 

with open('./input.txt') as f:
    ipt = [x.strip() for x in f.readlines()]




#### pt1 
def adjustForTime(universe):
    expansionRows = []
    for idx, row in enumerate(universe):
        if "#" in row: 
            continue 
        expansionRows.append(idx)

    expansionCols = []
    ## this is gross - rotate the universe to get columnwise 
    for idx, col in enumerate([[row[idx] for row in universe] for idx in range(len(universe[0]))]):
        if "#" in col:
            continue
        expansionCols.append(idx)

    height = len(universe[0]) + len(expansionRows) 
    width = len(universe) + len(expansionCols)
    ret = []
    for idx, row in enumerate(universe):
        if idx in expansionRows:
            ret.append("."*width)
            ret.append("."*width)
            continue 
        line = ""
        for idx, char in enumerate(row):
            if idx in expansionCols:
                line += ".."
                continue
            line += char 
        ret.append(line)

    return ret

def getGalaxies(universe):
    ret = []
    for row in range(len(universe)):
        for col in range(len(universe[0])):
            if universe[row][col] == '#':
                ret.append((row, col))

    return ret 

def getPairDistances(galaxies):
    distances = [] 
    for i1 in range(len(galaxies)):
        for i2 in range(i1, len(galaxies)):
            distance = abs(galaxies[i2][0] - galaxies[i1][0]) + abs(galaxies[i2][1] - galaxies[i1][1])
            distances.append(distance)
    return distances

universe = adjustForTime(ipt)
galaxies = getGalaxies(universe)
distances = getPairDistances(galaxies)
print(f"Pt1: {sum(distances)}")

#### pt2 
## it is not a good idea to keep in memory a universe with millions of rows/columns full of empty space
## so instead, keep track of where the empty spaces are, and add the number traversed to our distances 

def getAdjustments(universe):
    expansionRows = []
    for idx, row in enumerate(universe):
        if "#" in row: 
            continue 
        expansionRows.append(idx)

    expansionCols = []
    ## this is gross - rotate the universe to get columnwise 
    for idx, col in enumerate([[row[idx] for row in universe] for idx in range(len(universe[0]))]):
        if "#" in col:
            continue
        expansionCols.append(idx)

    return expansionRows, expansionCols

def getPairDistances(galaxies, expanseRows, expanseCols, adjustmentFactor=1_000_000):
    distances = []
    for i1 in range(len(galaxies)):
        for i2 in range(i1 + 1, len(galaxies)):
            
            gal1row = galaxies[i1][0]
            gal1col = galaxies[i1][1]
            gal2row = galaxies[i2][0]
            gal2col = galaxies[i2][1]
            
            rowDist = abs(gal2row - gal1row)
            colDist = abs(gal2col - gal1col)
            baseRowIdx = min(gal1row, gal2row)
            baseColIdx = min(gal1col, gal2col)

            traversedExpanses = 0 
            for row in expanseRows: 
                if baseRowIdx <= row <= (baseRowIdx + rowDist):
                    traversedExpanses += 1
            for col in expanseCols:
                if baseColIdx <= col <= (baseColIdx + colDist):
                    traversedExpanses += 1 

            distance = rowDist + colDist - traversedExpanses + (traversedExpanses * adjustmentFactor)
            distances.append(distance)
            
    return distances

universe = ipt
galaxies = getGalaxies(universe)
expansionRows, expansionCols = getAdjustments(universe)
distances = getPairDistances(galaxies, expansionRows, expansionCols)
print(f"Pt1: {sum(getPairDistances(galaxies, expansionRows, expansionCols, 2))}")
print(f"Pt2: {sum(distances)}") 


