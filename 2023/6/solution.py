#!python3

with open('./input.txt') as f: 
    ipt = [x.strip() for x in f.readlines()] 

#### pt1

def parseRaces(lines): 
    times = [int(x.strip()) for x in lines[0].lstrip("Time:").split()]
    distances = [int(x.strip()) for x in lines[1].lstrip("Distance:").split()]
    return [{'time': time, 'distance': distance} for time, distance in zip(times, distances)]

races = parseRaces(ipt)

## S = Tt - t^2
def getDistance(T, t): 
    return t * (T - t)

def possibleDistances(race): 
    return [getDistance(race['time'], time) for time in range(1, race['time'])]

recordBeaters = [len([x for x in possibleDistances(race) if x > race['distance']]) for race in races] 

from math import prod 
print(f"Pt1: {recordBeaters}")
print(f"Pt1: {prod(recordBeaters)}")



#### pt2 
def parseRace(lines):
    time = int(lines[0].lstrip("Time:").replace(" ", ""))
    distance = int(lines[1].lstrip("Distance:").replace(" ", ""))
    return time, distance
    
winners = 0
time, distance = parseRace(ipt)
for r in range(1, time):
    if getDistance(time, r) > distance:
        winners += 1
print(f"Pt2: {winners}")

