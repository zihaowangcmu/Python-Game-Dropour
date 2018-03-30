#############################################################################################
# This function detects if the bomb explode
#############################################################################################

from Drop import Drop
from Bomb import Bomb

def isExploded(drop,map):
    for pair in map:
        x1 = pair[0]
        y1 = pair[1]
        x2 = drop.x
        y2 = drop.y
        if (x1 == x2 and abs(y2-y1)<1) or (y1 == y2 and abs(x1-x2)<1):
            return True
    return False