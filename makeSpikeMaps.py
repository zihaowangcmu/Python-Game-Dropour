############################################################################################
# These functions create the spike maps of 4 directions
# ESM: The spikes whose spine points EAST
# Others are named in the same way
############################################################################################

from Spike import Spike

def makeSpikeMaps(spikeMaps,direction,levels):
    if direction == 'east':
        return makeESM(spikeMaps,levels)
    elif direction == 'west':
        return makeWSM(spikeMaps,levels)
    elif direction == 'north':
        return makeNSM(spikeMaps,levels)
    elif direction == 'south':
        return makeSSM(spikeMaps,levels)

def makeESM(spikeMaps,levels):
    SM = dict()
    for i in range(-1,levels):
        SM[i] = []
        for pair in spikeMaps[i]:
            if pair[2] == 'e':
                newX,newY = pair[0],pair[1]
                SM[i].append((newX,newY))
    return SM

def makeWSM(spikeMaps,levels):
    SM = dict()
    for i in range(-1,levels):
        SM[i] = []
        for pair in spikeMaps[i]:
            if pair[2] == 'w':
                newX,newY = pair[0],pair[1]
                SM[i].append((newX,newY))
    return SM

def makeNSM(spikeMaps,levels):
    SM = dict()
    for i in range(-1,levels):
        SM[i] = []
        for pair in spikeMaps[i]:
            if pair[2] == 'n':
                newX,newY = pair[0],pair[1]
                SM[i].append((newX,newY))
    return SM

def makeSSM(spikeMaps,levels):
    SM = dict()
    for i in range(-1,levels):
        SM[i] = []
        for pair in spikeMaps[i]:
            if pair[2] == 's':
                newX,newY = pair[0],pair[1]
                SM[i].append((newX,newY))
    return SM