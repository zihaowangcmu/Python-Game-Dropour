#############################################################################################
# This is class WormholeA.
# When the drop come to the worm hole, it will go out from another end while the direction remains the same.
# This is one end of wormhole
# The other end is WormholeB
#############################################################################################

class WormholeA():
    
    mapDict = dict()
    def __init__(wormholeA):
        wormholeA.mapDict[-1] = []
        wormholeA.mapDict[0] = []
        wormholeA.mapDict[1] = []
        wormholeA.mapDict[2] = []
        wormholeA.mapDict[3] = []
        wormholeA.mapDict[4] = [(12,9)]
        wormholeA.mapDict[5] = [(7,10)]
        wormholeA.mapDict[6] = []
        wormholeA.mapDict[7] = []
        wormholeA.mapDict[8] = []
        
    def draw(canvas,data):
        for pair in data.currentWormholeAMap:
            x = pair[0]
            y = pair[1]
            canvas.create_image(30*(x-1)+15,30*(y-1)+15,image=data.wormholeAImage)