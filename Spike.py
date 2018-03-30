############################################################################################
# This is class Splike
# When the water drop go straight to the spike, you died
# But you can safely stop at the other sides
# (x,y,direction of spike)
# The DeadMode will be added later
############################################################################################

class Spike():
    
    mapDict = dict()
    def __init__(spike):
        spike.mapDict[-1] = [] # prepared for BUILD MY MAZE mode
        spike.mapDict[0] = [] # prepared for BUILD MY MAZE mode
        spike.mapDict[1] = []
        spike.mapDict[2] = []
        spike.mapDict[3] = [(13,8,'s'),(10,9,'e'),(10,10,'e'),(10,11,'e')]
        spike.mapDict[4] = []
        spike.mapDict[5] = [(7,8,'s')]
        spike.mapDict[6] = []
        spike.mapDict[7] = []
        spike.mapDict[8] = []
            
    def draw(canvas,data):
        # draw spikes according to their directions
        for pair in data.currentSpikeMap:
            x = pair[0]
            y = pair[1]
            direction = pair[2]
            if direction == 'e':
                canvas.create_image(30*(x-1)+15,30*(y-1)+15,image=data.spikeEastImage)
            elif direction == 'w':
                canvas.create_image(30*(x-1)+15,30*(y-1)+15,image=data.spikeWestImage)
            elif direction == 's':
                canvas.create_image(30*(x-1)+15,30*(y-1)+15,image=data.spikeSouthImage)
            elif direction == 'n':
                canvas.create_image(30*(x-1)+15,30*(y-1)+15,image=data.spikeNorthImage)