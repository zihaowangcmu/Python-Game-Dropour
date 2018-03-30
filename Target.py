#############################################################################################
# This is class Target.
# Target is the itme the player wants to reach.
# As long as all the targets are collected, the current level is finished,
# and the player goes to the next level.
# Check if the drop collide with target, the target vanishes and the player
# get a point.
# When the point reaches the number of total targets, the player complete this level
#############################################################################################

class Target():
    def __init__(target):
        target.r = 10
        target.mapDict = dict()
        
        target.mapDict[-1] = [] # prepared for BUILD MY MAZE mode
        target.mapDict[0] = [] # prepared for BUILD MY MAZE mode
        target.mapDict[1] = [(7,10),(13,10),(11,9),(11,11)]
        target.mapDict[2] = [(7,8),(12,8),(11,10),(9,12)]
        target.mapDict[3] = [(12,7),(7,10),(15,10),(7,12)]
        target.mapDict[4] = [(10,10),(12,11)]
        target.mapDict[5] = [(11,10),(8,10),(9,12)]
        target.mapDict[6] = [(12,10),(10,12),(8,10),(10,8)]
        target.mapDict[7] = [(11,10),(12,12)]
        target.mapDict[8] = [(8,12)]
            
    def draw(canvas,data):
        for pair in data.currentTargetMap:
            x = pair[0]
            y = pair[1]
            canvas.create_image(30*(x-1)+15,30*(y-1)+15,image=data.targetImage)