#############################################################################################
# this is function updateAllSpikeRealatedMaps
#############################################################################################

import copy

def updateAllSpikeRealatedMaps(data):
    # these are used to detect collision
    data.currentEBM = copy.deepcopy(data.EBM[data.level])
    data.currentWBM = copy.deepcopy(data.WBM[data.level])
    data.currentNBM = copy.deepcopy(data.NBM[data.level])
    data.currentSBM = copy.deepcopy(data.SBM[data.level])
    
    # these are used to detect piereced by spikes
    data.currentESM = copy.deepcopy(data.ESM[data.level])
    data.currentWSM = copy.deepcopy(data.WSM[data.level])
    data.currentNSM = copy.deepcopy(data.NSM[data.level])
    data.currentSSM = copy.deepcopy(data.SSM[data.level])