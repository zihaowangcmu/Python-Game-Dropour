############################################################################################
# play mode!!!
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

def playGameMousePressed(event, data):
    pass

def recordPlayback(data):
    data.step += 1
    data.playbackMap[0].append(data.step)
    data.playbackMap[1].append(data.drop.direction)
    data.playbackMap[2].append(data.playTime*data.timerDelay)
    
def playGameKeyPressed(event, data):
    # Control the drop direction with wasd
    # When the water drop is moving, you can't control the direction anymore
    if event.keysym == 'd':
        if data.drop.direction == None:
            data.drop.direction = 'Right'
            recordPlayback(data)
    if event.keysym == 'a':
        if data.drop.direction == None:
            data.drop.direction = 'Left'
            recordPlayback(data)
    if event.keysym == 'w':
        if data.drop.direction == None:
            data.drop.direction = 'Up'
            recordPlayback(data)
    if event.keysym == 's':
        if data.drop.direction == None:
            data.drop.direction = 'Down'
            recordPlayback(data)
    # Realize some additional function
    # Press R to restart
    if event.keysym == 'r':
        data.currentScore = 0
        data.drop = copy.deepcopy(data.dropMapDict[data.level])
        data.currentTargetMap = copy.deepcopy(data.targetMapDict[data.level])
        data.currentTrigeredMap = []
        updatePlaybackThings(data)
        updateAllSpikeRealatedMaps(data)
    # Press P to pause
    if event.keysym == 'p':
        data.mode = 'pause'
    
def playGameTimerFired(data):
    data.playTime += 1
    drawBackgroundAnimationsTimer(data)
    # The drop's movement
    # now just consider one drop
    # For the 4 following if statement, each one:
    # the first if check if the drop will be scrolled
    # the second if check if it is pierced
    # the third one check if it collide with a wall
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
        if data.level != -1: # the customized map does not count
            data.accumulatedScore += 1
        if data.currentTargetMap == []:
            if data.level+1 == 0:
                # short for customizedMapVictory
                data.mode = 'CMVictory'
            elif data.level+1 != data.totalLevels:
                data.mode = 'interval'
            else:
                data.mode = 'clearance'

def playGameRedrawAll(canvas, data):
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
    drawBestSolution(canvas,data)