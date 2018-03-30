############################################################################################
# This is class bomb
# if you collide with it, you die
############################################################################################

class Bomb():
    
    mapDict = dict()
    def __init__(bomb):
        bomb.mapDict[-1] = [] # prepared for BUILD MY MAZE mode
        bomb.mapDict[0] = [] # prepared for BUILD MY MAZE mode
        bomb.mapDict[1] = []
        bomb.mapDict[2] = []
        bomb.mapDict[3] = []
        bomb.mapDict[4] = []
        bomb.mapDict[5] = []
        bomb.mapDict[6] = []
        bomb.mapDict[7] = []
        bomb.mapDict[8] = []
        
    def draw(canvas,data):
        for pair in data.currentBombMap:
            x = pair[0]
            y = pair[1]
            canvas.create_image(30*(x-1)+15,30*(y-1)+15,image=data.bombImage)