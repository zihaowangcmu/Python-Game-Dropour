############################################################################################
# This is the class Brick
# This class defines the maps of places of bricks of different levels!
# Also, define some common forms of bricks
############################################################################################

import copy

class Brick():
    
    def __init__(brick):
        brick.width = 30
        brick.height = 30
        # brick.level = level # the level will be changed, so build a class Level later
        brick.mapDict = dict()
        
        brick.mapDict[-1] = [] # prepared for BUILD MY MAZE mode
        brick.mapDict[0] = [] # prepared for BUILD MY MAZE mode
        brick.mapDict[1] = \
        [(7,8),(8,8),(9,8),(10,8),(11,8),(12,8),(13,8),(6,9),(14,9),(5,10),
        (14,10),(15,10),(6,11),(12,11),(14,11),(7,12),(8,12),(9,12),(10,12),
        (11,12),(12,12),(13,12)]
        brick.mapDict[2] = \
        [(5,7),(6,7),(7,7),(8,7),(9,7),(10,7),(11,7),(12,7),(13,7),(14,7),
        (15,7),(16,7),(9,8),(10,8),(11,8),(10,9),(10,10),(10,11),(10,12),
        (10,13),(10,14),(9,13),(11,13),(12,13),(5,14),(6,14),(7,14),(8,14),
        (9,14),(10,14),(11,14),(12,14),(13,14),(14,14),(15,14),(16,14),(7,11),
        (14,11)]
        brick.mapDict[3] = \
        [(13,7),(14,7),(15,7),(16,7),(6,8),(7,8),(8,8),(15,8),(16,8),(8,9),
        (9,9),(15,9),(16,9),(8,10),(9,10),(9,11),(8,11),(15,11),(16,11),
        (12,13),(13,13),(14,13),(15,13),(16,13)]
        brick.mapDict[4] = \
        [(8,8),(9,8),(10,8),(11,8),(12,8),(8,13),(9,13),(10,13),(11,13),(12,13),
        (7,9),(7,10),(7,11),(7,12),(13,9),(13,10),(13,11),(13,12),
        (8,11),(12,10),(11,10),(11,11),(10,11),(10,12)]
        brick.mapDict[5] = \
        [(5,9),(5,10),(5,11),(6,8),(6,9),(6,10),(6,11),(6,12),(7,7),(8,7),(9,7),
        (7,13),(8,13),(9,13),(13,7),(14,7),(9,9),(10,8),(10,9),(10,10),(10,11),
        (10,12),(11,8),(11,9),(11,12),(11,11),(12,8),(12,9),(12,12),(12,11),(13,13),
        (14,13),(15,8),(15,9),(15,10),(15,11),(15,12),(16,9),(16,10),(16,11)]
        brick.mapDict[6] = \
        [(7,7),(8,7),(9,7),(10,7),(11,7),(12,7),(13,7),(7,13),(8,13),(9,13),
        (10,13),(11,13),(12,13),(13,13),(7,9),(7,10),(7,11),(7,12),(13,9),
        (13,10),(13,11),(13,12),(8,12),(12,12),(9,8),(9,9),(9,11),(11,9),(11,11)]
        brick.mapDict[7] = []
        brick.mapDict[8] = \
        [(6,8),(6,9),(7,8),(7,12),(15,13),(14,11),(12,11),(13,9)]

    # def __hash__(brick):
    #     return hash((brick))
        
    def draw(canvas,data):
        for pair in data.currentBrickMap:
            x = pair[0]
            y = pair[1]
            canvas.create_image(30*(x-1)+15,30*(y-1)+15,image=data.brickImage)