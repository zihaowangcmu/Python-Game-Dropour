#############################################################################################
# This is class Trap.
#############################################################################################

class Trap():
    def __init__(trap):
        trap.mapDict = dict()
        
        trap.mapDict[-1] = [] # prepared for BUILD MY MAZE mode
        trap.mapDict[0] = [] # prepared for BUILD MY MAZE mode
        trap.mapDict[1] = []
        trap.mapDict[2] = []
        trap.mapDict[3] = []
        trap.mapDict[4] = []
        trap.mapDict[5] = []
        trap.mapDict[6] = [(10,11),(10,9),(9,10),(11,10)]
        trap.mapDict[7] = [(10,10),(9,12),(12,9),(11,11)]
        trap.mapDict[8] = []
            
    def draw(canvas,data):
        for pair in data.currentTrapMap:
            x = pair[0]
            y = pair[1]
            canvas.create_image(30*(x-1)+15,30*(y-1)+15,image=data.trap1Image)
        for pair in data.currentTrigeredMap:
            x = pair[0]
            y = pair[1]
            canvas.create_image(30*(x-1)+15,30*(y-1)+15,image=data.trap2Image)