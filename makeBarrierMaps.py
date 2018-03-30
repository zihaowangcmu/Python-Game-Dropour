############################################################################################
# These functions create the barrier maps includes bricks and legal sides of spikes
# These maps are actually used in judging the updated status of water drop
# EBM: barriers which can stop moving of the water drop FROM WEST TO EAST(RIGHT direction), include the spikes if the direction is suited for this situation, meaning spikes whose spine does NOT pointing WEST!!!
# news are short version for north east west south
############################################################################################

from Brick import Brick
from Spike import Spike
import copy

def makeBarrierMaps(brickMaps,spikeMaps,direction,levels):
    if direction == 'east':
        return makeEBM(brickMaps,spikeMaps,levels)
    elif direction == 'west':
        return makeWBM(brickMaps,spikeMaps,levels)
    elif direction == 'north':
        return makeNBM(brickMaps,spikeMaps,levels)
    elif direction == 'south':
        return makeSBM(brickMaps,spikeMaps,levels)
        
def makeEBM(brickMaps,spikeMaps,levels):
    EBM = copy.deepcopy(brickMaps)
    for i in range(1,levels):
        for pair in spikeMaps[i]:
            if pair[2] != 'w':
                newX,newY = pair[0],pair[1]
                EBM[i].append((newX,newY))
    return EBM

def makeWBM(brickMaps,spikeMaps,levels):
    BM = copy.deepcopy(brickMaps)
    for i in range(1,levels):
        for pair in spikeMaps[i]:
            if pair[2] != 'e':
                newX,newY = pair[0],pair[1]
                BM[i].append((newX,newY))
    return BM
    
def makeNBM(brickMaps,spikeMaps,levels):
    BM = copy.deepcopy(brickMaps)
    for i in range(1,levels):
        for pair in spikeMaps[i]:
            if pair[2] != 's':
                newX,newY = pair[0],pair[1]
                BM[i].append((newX,newY))
    return BM
    
def makeSBM(brickMaps,spikeMaps,levels):
    BM = copy.deepcopy(brickMaps)
    for i in range(1,levels):
        for pair in spikeMaps[i]:
            if pair[2] != 'n':
                newX,newY = pair[0],pair[1]
                BM[i].append((newX,newY))
    return BM