

with open('./input.txt') as f:
    lines = [x.strip('\n') for x in f.readlines()]
lines[1]


## pt 1 
nums = "0123456789"
allnums = []
for line in lines:
    linenums = [char for char in line if char in nums]
    if not len(linenums):
        continue
    bignumstr = linenums[0] + linenums[-1]
    bignum = int(bignumstr)
    allnums.append(bignum)
print(f"pt 1: {sum(allnums)}")



## pt 2 
import re 

numchars = {
    "1": 1,
    "2": 2,
    "3": 3, 
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}
numstrings = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

allnums = []
## find the number start indices (both for digits and words)
## sort them to get first and last 
## catenate, convert to int, add to set 
## sum set 
## alternatively, could be more memory-safe, and keep a running total, 
# reading one line from file at a time 
# and incrementing running total
# /shrug 

for line in lines:
    numindices = {} 
    ## because these maps don't collide, i could just merge the two maps and run this loop once across the whole thing 
    ## this wouldn't affect performance but it would look a bit neater 
    for numstr, numnum in numstrings.items():
        indices = [match.start(0) for match in re.finditer(numstr, line)]
        for index in indices:
            numindices[index] = numnum 
    for numchar, numnum in numchars.items(): 
        indices = [match.start(0) for match in re.finditer(numchar, line)]
        for index in indices:
            numindices[index] = numnum
    if not len(numindices): 
        continue 
    sortedindices = sorted(numindices.keys())
    first = sortedindices[0]
    last = sortedindices[-1]
    allnums.append(int(str(numindices[first]) + str(numindices[last])))

print(f"pt 2: {sum(allnums)}")



