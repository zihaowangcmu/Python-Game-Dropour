############################################################################################
# Actions judging the status of drop
# Detect if the drop is destructed or sent through wormholes or triggered a trap
############################################################################################

import copy
from updatePlaybackThings import *

def destructiveAction(data):
    data.currentScore = 0
    data.drop = copy.deepcopy(data.dropMapDict[data.level])
    data.currentTargetMap = copy.deepcopy(data.targetMapDict[data.level])
    data.currentTrigeredMap = []
    updatePlaybackThings(data)

def wormholeAction(data):
    (x,y) = (data.drop.x,data.drop.y)
    if (x,y) in data.currentWormholeAMap:
        wormholeIndex = data.currentWormholeAMap.index((x,y))
        if wormholeIndex < len(data.currentWormholeBMap):
            (data.drop.x,data.drop.y) = data.currentWormholeBMap[wormholeIndex]
    elif (x,y) in data.currentWormholeBMap:
        wormholeIndex = data.currentWormholeBMap.index((x,y))
        if wormholeIndex < len(data.currentWormholeAMap):
            (data.drop.x,data.drop.y) = data.currentWormholeAMap[wormholeIndex]
        
def trapAction(data):
    (x,y) = (data.drop.x,data.drop.y)
    if (x,y) in data.currentTrapMap:
        data.currentEBM.append((x,y))
        data.currentWBM.append((x,y))
        data.currentNBM.append((x,y))
        data.currentSBM.append((x,y))
        data.currentTrigeredMap.append((x,y))