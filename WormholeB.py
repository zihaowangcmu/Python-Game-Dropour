#############################################################################################
# This is class WormholeB.
# When the drop come to the worm hole, it will go out from another end while the direction remains the same.
# This is one end of wormhole
# The other end is WormholeA
#############################################################################################

class WormholeB():
    
    mapDict = dict()
    def __init__(wormholeB):
        wormholeB.mapDict[-1] = []
        wormholeB.mapDict[0] = []
        wormholeB.mapDict[1] = []
        wormholeB.mapDict[2] = []
        wormholeB.mapDict[3] = []
        wormholeB.mapDict[4] = [(11,12)]
        wormholeB.mapDict[5] = [(14,10)]
        wormholeB.mapDict[6] = []
        wormholeB.mapDict[7] = []
        wormholeB.mapDict[8] = []
        
    def draw(canvas,data):
        for pair in data.currentWormholeBMap:
            x = pair[0]
            y = pair[1]
            canvas.create_image(30*(x-1)+15,30*(y-1)+15,image=data.wormholeBImage)