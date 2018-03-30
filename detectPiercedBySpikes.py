#############################################################################################
# This function check if the drop collides with a spike.
# If returning True, the drop breaks and the game restarts.
#############################################################################################

from Drop import Drop
from Spike import Spike

def isPierced(drop,map,direction):
    if direction == 'Right' or direction == 'Left':
        return isPiercedWhenMovingHorizontally(drop,map)
    if direction == 'Up' or direction == 'Down':
        return isPiercedWhenMovingVertically(drop,map)
        
def isPiercedWhenMovingHorizontally(drop,map):
    for pair in map:
        if drop.y == pair[1] and abs(pair[0]-drop.x) < 1:
            return True
    return False
    
def isPiercedWhenMovingVertically(drop,map):
    for pair in map:
        if drop.x == pair[0] and abs(pair[1]-drop.y) < 1:
            return True
    return False