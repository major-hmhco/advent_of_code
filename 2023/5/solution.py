with open('./input.txt') as f:
    ipt = [x.strip() for x in f.readlines()]


#### pt 1
seeds = ipt.pop(0)
seeds = [int(seed) for seed in seeds.lstrip("seeds: ").split(" ")]

conversions = {}
for line in ipt:
    if line == '': 
        continue 
    if line.endswith(":"):
        line = line.rstrip(" map:").split("-to-")
        conversionSource = line[0]
        conversionDestination = line[1]
        conversions[conversionSource] = {
                'dest': conversionDestination,
                'ranges': []
        }
        continue 
    line = line.split(" ")
    destRangeStart = int(line[0])
    sourceRangeStart = int(line[1])
    rangeLength = int(line[2])
    conversions[conversionSource]['ranges'].append({
                'sourceStart': sourceRangeStart,
                'sourceEnd': sourceRangeStart + (rangeLength - 1),
                'destStart': destRangeStart,
                'rangeLength': rangeLength,
    })


locations = []
for seed in seeds: 
    value = seed 
    source = 'seed'
    while source != 'location': 
        found = False
        print(f"searching for {value} in {source}")
        for rang in conversions[source]['ranges']: 
            if not rang['sourceStart'] <= value <= rang['sourceEnd']:
                continue
            value = rang['destStart'] + (value - rang['sourceStart']) 
            print(f"    new value: {value}")
            source = conversions[source]['dest'] 
            print(f"    new source {source}")
            found = True
            break
        if not found:
            source = conversions[source]['dest']

    locations.append(value)

print(f"{locations}")
print(f"Pt1: {min(locations)}")



#### pt2
with open('./input.txt') as f:
    ipt = [x.strip() for x in f.readlines()]

seeds = ipt.pop(0)
seeds = [int(seed) for seed in seeds.lstrip("seeds: ").split(" ")]
seedRanges = [[seeds[i],seeds[i+1]] for i in range(0, len(seeds), 2)]
print(f"ranges: {seedRanges}")
print(f"check total: {sum([x[1] for x in seedRanges])}")

locations = []
minimum = 10000000000000000000000000000000000000000000000000000000000000 
for r in seedRanges: 
    for seed in range(r[0], r[0]+r[1]):
        value = seed
        source = 'seed'
        while source != 'location':
            for rang in conversions[source]['ranges']:
                if not rang['sourceStart'] <= value <= rang['sourceEnd']:
                    continue
                value = rang['destStart'] + (value - rang['sourceStart'])
                break
            source = conversions[source]['dest']

        minimum = min(minimum, value)

print(f"Pt2: {minimum}")
