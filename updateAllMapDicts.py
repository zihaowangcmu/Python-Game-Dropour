#############################################################################################
# this is function updateAllMapDicts
#############################################################################################

import copy

def updateAllMapDicts(data):
    
    # pass all the maps of different items
    data.dropMapDict = copy.deepcopy(data.dropMapDict) # pass all the drop maps
    data.brickMapDict = copy.deepcopy(data.brick.mapDict) # pass all the brick maps
    data.scrollMapDict = copy.deepcopy(data.scroll.mapDict) # pass all the brick maps
    data.targetMapDict = copy.deepcopy(data.target.mapDict) # pass all the target maps
    data.spikeMapDict = copy.deepcopy(data.spike.mapDict) # pass all the spike maps
    data.bombMapDict = copy.deepcopy(data.bomb.mapDict) # pass all the bomb maps
    data.wormholeAMapDict = copy.deepcopy(data.wormholeA.mapDict) # pass all the whA maps
    data.wormholeBMapDict = copy.deepcopy(data.wormholeB.mapDict) # pass all the whB maps
    data.trapMapDict = copy.deepcopy(data.trap.mapDict) # pass all the trap maps