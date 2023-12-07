with open('./input.txt') as f: 
    ipt = [x.strip() for x in f.readlines()] 

#### pt1

## loop over lines, for each line, get the start/end indices of each number
## and the indices of all symbols (non-numbers, non-`.`s) 
## for all numbers, check if there is a symbol in the indices immediately before or after
## if not, check each previous/next line for symbols in the between (number start index - 1), (number end index +1) 
import re 

running = 0
for i in range(0, len(ipt)):
    line = ipt[i]
    prevLine = "." * len(line) if i == 0 else ipt[i-1] 
    nextLine = "." * len(line) if i == (len(ipt) - 1) else ipt[i+1] 

    print(f"LINE: {line}")

    matches = re.finditer("\d+", line)
    for match in matches: 
        print(f"    checking Match: {match.group(0)}")
        chunkStart = max(0, match.start(0) - 1)
        chunkEnd = min(len(line), match.end(0) + 1)

        print(f"    chunkStart: {chunkStart}, chunkEnd: {chunkEnd}")

        prevChunk = prevLine[chunkStart:chunkEnd]
        print(f"    prevChunk: {prevChunk}")
        thisChunk = line[chunkStart:chunkEnd]
        print(f"    thisChunk: {thisChunk}")
        nextChunk = nextLine[chunkStart:chunkEnd] 
        print(f"    nextChunk: {nextChunk}")
        
        allChars = prevChunk + thisChunk + nextChunk 

        if any([not x in ".0123456789" for x in allChars]): 
            running += int(match.group())

print(f"pt1: {running}")


#### pt 2

## similar to above, but now we're gonna search for gears, and see if there are any numbers in the windows around them 
## we're gonna be quite compute-wasteful as we potentially check each line for numbers up to three times, but i'm not bothered 
running = 0

for i in range(0, len(ipt)): 
    line = ipt[i]
    prevLine = "." * len(line) if i == 0 else ipt[i-1]
    nextLine = "." * len(line) if i == (len(ipt) - 1) else ipt[i+1]


    gears = re.finditer("\*", line)

    for gear in gears:
        gearIndex = gear.start(0)
        window = [gearIndex - 1, gearIndex, gearIndex + 1]

        prevNums = re.finditer("\d+", prevLine)
        thisNums = re.finditer("\d+", line)
        nextNums = re.finditer("\d+", nextLine)

        multipliers = []

        ## check prev line first
        for match in list(prevNums) + list(thisNums) + list(nextNums):
            if (match.start(0) in window) or (match.end(0) - 1 in window):
                multipliers.append(int(match.group()))


        if len(multipliers) == 2: 
            print()
            print(f"PREV: {prevLine}")
            print(f"THIS: {line}")
            print(f"NEXT: {nextLine}")
            print(f"    found multipliers: {multipliers}")
            print()
            running += multipliers[0] * multipliers[1] 

print(f"pt2: {running}")

