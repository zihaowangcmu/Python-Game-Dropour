#############################################################################################
# This is the class Drop
# This class defines the movement of drop
#############################################################################################

class Drop():
    
    def __init__(drop,x,y):
        drop.x = x
        drop.y = y
        drop.r = 15
        drop.speed = 0.5 # 1 maens 1 time of 30
        drop.direction = None
        
    def draw(canvas,data):
        x = data.drop.x
        y = data.drop.y
        canvas.create_image(30*(x-1)+15,30*(y-1)+15,image = data.dropImage)