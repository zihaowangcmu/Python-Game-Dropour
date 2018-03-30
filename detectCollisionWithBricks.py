############################################################################################
# For the below 4 functions,
# The map is bricks' map.
# They seperately check the collision with the bricks, since the condition are not the same.
# If collide, return True; else return False
############################################################################################

from Drop import Drop
from Brick import Brick

def doesCollideWithRightBricks(drop,map):
    for item in map:
        if item[0]>drop.x and drop.y == item[1] and \
        item[0]-drop.x<1+drop.speed:
            return True
    return False
    
def doesCollideWithLeftBricks(drop,map):
    for item in map:
        if item[0]<drop.x and drop.y == item[1] and \
        drop.x-item[0]<1+drop.speed:
            return True
    return False

def doesCollideWithUpBricks(drop,map):
    for item in map:
        if item[1]<drop.y and drop.x == item[0] and \
        drop.y-item[1]<1+drop.speed:
            return True
    return False
    
def doesCollideWithDownBricks(drop,map):
    for item in map:
        if item[1]>drop.y and drop.x == item[0] and \
        item[1]-drop.y<1+drop.speed:
            return True
    return False