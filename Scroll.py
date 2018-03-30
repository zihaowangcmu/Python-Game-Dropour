#############################################################################################
# This is class scroll
# When the drop moves to the scroll positions, the direction keeps the same while it moves from the side of the screnn to another side
#############################################################################################

class Scroll():
    def __init__(scroll):
        scroll.mapDict = dict()
        
        scroll.mapDict[-1] = []# prepared for BUILD MY MAZE mode
        scroll.mapDict[0] = []# prepared for BUILD MY MAZE mode
        scroll.mapDict[1] = []
        scroll.mapDict[2] = \
        [(5,8),(5,9),(5,10),(5,11),(5,12),(5,13),
        (15,8),(15,9),(15,10),(15,11),(15,12),(15,13)]
        scroll.mapDict[3] = \
        [(7,7),(16,10),(4,10),(16,12),(4,12),(7,13)]
        scroll.mapDict[4] = []
        scroll.mapDict[5] = []
        scroll.mapDict[6] = [(7,8),(13,8)]
        scroll.mapDict[7] = \
        [(7,9),(8,10),(8,11),(7,12),(14,9),(13,10),(13,11),(14,12),
        (9,7),(10,8),(11,8),(12,7),(9,14),(10,13),(11,13),(12,14)]
        scroll.mapDict[8] = \
        [(6,10),(6,11),(6,12),(15,10),(15,11),(15,12),
        (8,8),(9,8),(10,8),(11,8),(12,8),(13,8),(14,8),
        (8,13),(9,13),(10,13),(11,13),(12,13),(13,13),(14,13),]
        
    def draw(canvas,data):
        for pair in data.currentScrollMap:
            x = pair[0]
            y = pair[1]
            canvas.create_image(30*(x-1)+15,30*(y-1)+15,image=data.scrollImage)