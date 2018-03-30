#############################################################################################
# this is function updateAllCurrentGeneralMaps
#############################################################################################

import copy

def updateAllCurrentGeneralMaps(data):
    
    # this is the current drop for this level
    data.drop = copy.deepcopy(data.dropMapDict[data.level])
    data.currentTargetMap = copy.deepcopy(data.targetMapDict[data.level])
    data.currentSpikeMap = copy.deepcopy(data.spikeMapDict[data.level])
    data.currentScrollMap = copy.deepcopy(data.scrollMapDict[data.level])
    data.currentBombMap = copy.deepcopy(data.bombMapDict[data.level])
    data.currentWormholeAMap = copy.deepcopy(data.wormholeAMapDict[data.level])
    data.currentWormholeBMap = copy.deepcopy(data.wormholeBMapDict[data.level])
    data.currentTrapMap = copy.deepcopy(data.trapMapDict[data.level])
    data.currentTrigeredMap = []
    data.currentScore = 0
    # this is only used to draw briks
    data.currentBrickMap = copy.deepcopy(data.brickMapDict[data.level])