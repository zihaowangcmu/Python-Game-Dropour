############################################################################################
# This is playback mode
# playback your last tour and try to improve that!
# the playback things will be updated when:1.you die; 2.you restart; 3.you go to next level
############################################################################################

import copy
import winsound
from Drop import Drop
from DropMap import *
from Brick import Brick
from Scroll import Scroll
from Target import Target
from Spike import Spike
from Bomb import Bomb
from WormholeA import WormholeA
from WormholeB import WormholeB
from Trap import Trap
from modify import *
from detectCollisionWithBricks import *
from detectCollisionWithTargets import *
from detectPiercedBySpikes import *
from detectExplosion import *
from updateAllMapDicts import *
from updateAllCurrentGeneralMaps import *
from updateAllSpikeRealatedMaps import *
from updatePlaybackThings import *
from drawBackgroundAnimationsTimer import*
from drawBackgroundAnimations import *
from dropAction import *

def playbackMousePressed(event, data):
    pass

def playbackKeyPressed(event, data):
    pass

def playbackTimerFired(data):
    data.playTime += 1
    drawBackgroundAnimationsTimer(data)
    # The drop's movement
    # now just consider one drop
    # For the 4 following if statement, each one:
    # the first if check if the drop will be scrolled
    # the second if check if it is pierced
    # the third one check if it collide with a wall
    if data.playTime*data.timerDelay in data.playbackMap[2]:
        data.currentIndex = data.playbackMap[2].index(data.playTime*data.timerDelay)
        data.drop.direction = data.playbackMap[1][data.currentIndex]
    if data.drop.direction == 'Right':
        if (data.drop.x,data.drop.y) in data.currentScrollMap:
            for pair in data.currentScrollMap:
                if data.drop.y == pair[1] and data.drop.x != pair[0]:
                    data.drop.x = pair[0]
                    break
        wormholeAction(data)
        trapAction(data)
        if isPierced(data.drop,data.currentWSM,data.drop.direction) or \
        isExploded(data.drop,data.currentBombMap):
            destructiveAction(data)
        else:
            if not doesCollideWithRightBricks(data.drop,data.currentEBM):
                data.drop.x += data.drop.speed
            else:
                data.drop.direction = None
                data.drop.x = modifiedCoord(data.drop.x)
                
    elif data.drop.direction == 'Left':
        if (data.drop.x,data.drop.y) in data.currentScrollMap:
            for pair in data.currentScrollMap:
                if data.drop.y == pair[1] and data.drop.x != pair[0]:
                    data.drop.x = pair[0]
                    break
        wormholeAction(data)
        trapAction(data)
        if isPierced(data.drop,data.currentESM,data.drop.direction) or \
        isExploded(data.drop,data.currentBombMap):
            destructiveAction(data)
        else:
            if not doesCollideWithLeftBricks(data.drop,data.currentWBM):
                data.drop.x -= data.drop.speed
            else:
                data.drop.direction = None
                data.drop.x = modifiedCoord(data.drop.x)
            
    elif data.drop.direction == 'Up':
        if (data.drop.x,data.drop.y) in data.currentScrollMap:
            for pair in data.currentScrollMap:
                if data.drop.x == pair[0] and data.drop.y != pair[1]:
                    data.drop.y = pair[1]
                    break
        wormholeAction(data)
        trapAction(data)
        if isPierced(data.drop,data.currentSSM,data.drop.direction) or \
           isExploded(data.drop,data.currentBombMap):
               destructiveAction(data)
        else:
            if not doesCollideWithUpBricks(data.drop,data.currentNBM):
                data.drop.y -= data.drop.speed
            else:
                data.drop.direction = None
                data.drop.y = modifiedCoord(data.drop.y)
            
    elif data.drop.direction == 'Down':
        if (data.drop.x,data.drop.y) in data.currentScrollMap:
            for pair in data.currentScrollMap:
                if data.drop.x == pair[0] and data.drop.y != pair[1]:
                    data.drop.y = pair[1]
                    break
        wormholeAction(data)
        trapAction(data)
        if isPierced(data.drop,data.currentNSM,data.drop.direction) or \
           isExploded(data.drop,data.currentBombMap):
               destructiveAction(data)
        else:
            if not doesCollideWithDownBricks(data.drop,data.currentSBM):
                data.drop.y += data.drop.speed
            else:
                data.drop.direction = None
                data.drop.y = modifiedCoord(data.drop.y)
            
    # the target situation
    # get a point if a target is reached
    # switch to next level if get all targets
    # This time, all map will be reload to fit for the current level
    if doesCollideWithTarget(data.drop,data.currentTargetMap) != -1:
        reachedTarget = doesCollideWithTarget(data.drop,data.currentTargetMap)
        data.currentTargetMap.pop(reachedTarget)
        data.currentScore += 1
        if data.currentTargetMap == []:
            if data.level+1 == 0:
                # short for customizedMapVictory
                data.mode = 'CMVictory'
            elif data.level+1 != data.totalLevels:
                data.mode = 'interval'
            else:
                data.mode = 'clearance'

def playbackRedrawAll(canvas, data):
    canvas.create_image(data.width/2,data.height/2,image=data.playBGImage)
    drawSnowflakes(canvas,data)
    Drop.draw(canvas,data)
    Brick.draw(canvas,data)
    Target.draw(canvas,data)
    Scroll.draw(canvas,data)
    drawScore(canvas,data)
    drawLevel(canvas,data)
    Spike.draw(canvas,data)
    Bomb.draw(canvas,data)
    WormholeA.draw(canvas,data)
    WormholeB.draw(canvas,data)
    Trap.draw(canvas,data)
    drawPlaybackTable(canvas,data)