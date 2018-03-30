#############################################################################################
# This function update all the playback related things
#############################################################################################

def updatePlaybackThings(data):
    data.currentIndex = -1
    data.playTime = 0
    # data.playbackMap[0] records the current step
    # data.playbackMap[1] records the current direction
    # data.playbackMap[2] records the current time
    data.playbackMap = [[],[],[]]
    data.step = 0