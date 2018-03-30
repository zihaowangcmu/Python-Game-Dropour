###############################################################################################
# This function detedts if the drop reaches the targets
# If a target is reached, the target no longer exists, and you get one point
###############################################################################################

from Drop import Drop
from Target import Target

def doesCollideWithTarget(drop,map):
    for i in range(len(map)):
        if abs(drop.x-map[i][0])<=5/6 and abs(drop.y-map[i][1])<=5/6:
            return i
    return -1