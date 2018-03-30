###########################################################################################
# build my maze mode
# In this mode, the player can add the items so that they can create the maze themselves
###########################################################################################

from tkinter import *
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
from makeBarrierMaps import *
from makeSpikeMaps import *
from updateAllMapDicts import *
from updateAllCurrentGeneralMaps import *
from updateAllSpikeRealatedMaps import *
from drawBackgroundAnimationsTimer import*
from drawBackgroundAnimations import *

def buildMyMazeMousePressed(event, data):
    if 20 < event.x < 180 and 580 < event.y < 620:
        data.mode = 'playGame'
        data.level = -1
    elif 420 < event.x < 580 and 580 < event.y < 620:
        data.mode = 'menu'
    elif data.width/15-15 < event.x < data.width/15+15 and \
    1*data.height/10-15 < event.y < 1*data.height/10+15:
        data.currentItem = 'drop'
    elif data.width/15-15 < event.x < data.width/15+15 and \
    2*data.height/10-15 < event.y < 2*data.height/10+15:
        data.currentItem = 'brick'
    elif data.width/15-15 < event.x < data.width/15+15 and \
    3*data.height/10-15 < event.y < 3*data.height/10+15:
        data.currentItem = 'target'
    elif data.width/15-15 < event.x < data.width/15+15 and \
    4*data.height/10-15 < event.y < 4*data.height/10+15:
        data.currentItem = 'scroll'
    elif data.width/15-15 < event.x < data.width/15+15 and \
    5*data.height/10-15 < event.y < 5*data.height/10+15:
        data.currentItem = 'spikeNorth'
    elif data.width/15-15 < event.x < data.width/15+15 and \
    6*data.height/10-15 < event.y < 6*data.height/10+15:
        data.currentItem = 'spikeSouth'
    elif data.width/15-15 < event.x < data.width/15+15 and \
    7*data.height/10-15 < event.y < 7*data.height/10+15:
        data.currentItem = 'spikeEast'
    elif data.width/15-15 < event.x < data.width/15+15 and \
    8*data.height/10-15 < event.y < 8*data.height/10+15:
        data.currentItem = 'spikeWest'
    elif data.width/6-15 < event.x < data.width/6+15 and \
    1*data.height/10-15 < event.y < 1*data.height/10+15:
        data.currentItem = 'cross'
    elif data.width/6-15 < event.x < data.width/6+15 and \
    2*data.height/10-15 < event.y < 2*data.height/10+15:
        data.currentItem = 'bomb'
    elif data.width/6-15 < event.x < data.width/6+15 and \
    3*data.height/10-15 < event.y < 3*data.height/10+15:
        data.currentItem = 'wormholeA'
    elif data.width/6-15 < event.x < data.width/6+15 and \
    4*data.height/10-15 < event.y < 4*data.height/10+15:
        data.currentItem = 'wormholeB'
    elif data.width/6-15 < event.x < data.width/6+15 and \
    5*data.height/10-15 < event.y < 5*data.height/10+15:
        data.currentItem = 'trap'
    elif 150 < event.x < 600 and 120 < event.y < 570:
        (x,y) = (event.x//30+1,event.y//30+1)
        if data.currentItem == 'drop':
            if (x,y) not in data.occupiedCoordinatesMap:
                data.dropMapDict[-1] = Drop(x,y)
                data.drop = copy.deepcopy(data.dropMapDict[-1])
                data.occupiedMap[0] = (x,y,data.currentItem)
                data.occupiedCoordinatesMap[0] = (x,y)
        elif data.currentItem == 'brick':
            if (x,y) not in data.occupiedCoordinatesMap:
                data.brickMapDict[-1].append((x,y))
                data.currentBrickMap = copy.deepcopy(data.brickMapDict[-1])
                data.EBM[-1].append((x,y))
                data.WBM[-1].append((x,y))
                data.NBM[-1].append((x,y))
                data.SBM[-1].append((x,y))
                data.currentEBM = copy.deepcopy(data.EBM[-1])
                data.currentWBM = copy.deepcopy(data.WBM[-1])
                data.currentNBM = copy.deepcopy(data.NBM[-1])
                data.currentSBM = copy.deepcopy(data.SBM[-1])
                updateOccupiedRecord(data,x,y)
        elif data.currentItem == 'target':
            if (x,y) not in data.occupiedCoordinatesMap:
                data.targetMapDict[-1].append((x,y))
                data.currentTargetMap = copy.deepcopy(data.targetMapDict[-1])
                updateOccupiedRecord(data,x,y)
        elif data.currentItem == 'scroll':
            if (x,y) not in data.occupiedCoordinatesMap:
                data.scrollMapDict[-1].append((x,y))
                data.currentScrollMap = copy.deepcopy(data.scrollMapDict[-1])
                updateOccupiedRecord(data,x,y)
        elif data.currentItem == 'spikeNorth':
            if (x,y) not in data.occupiedCoordinatesMap:
                data.NSM[-1].append((x,y))
                data.currentNSM = copy.deepcopy(data.NSM[-1])
                data.spikeMapDict[-1].append((x,y,'n'))
                data.currentSpikeMap = copy.deepcopy(data.spikeMapDict[-1])
                data.EBM[-1].append((x,y))
                data.WBM[-1].append((x,y))
                data.NBM[-1].append((x,y))
                data.currentEBM = copy.deepcopy(data.EBM[-1])
                data.currentWBM = copy.deepcopy(data.WBM[-1])
                data.currentNBM = copy.deepcopy(data.NBM[-1])
                updateOccupiedRecord(data,x,y)
        elif data.currentItem == 'spikeSouth':
            if (x,y) not in data.occupiedCoordinatesMap:
                data.SSM[-1].append((x,y))
                data.currentSSM = copy.deepcopy(data.SSM[-1])
                data.spikeMapDict[-1].append((x,y,'s'))
                data.currentSpikeMap = copy.deepcopy(data.spikeMapDict[-1])
                data.EBM[-1].append((x,y))
                data.WBM[-1].append((x,y))
                data.SBM[-1].append((x,y))
                data.currentEBM = copy.deepcopy(data.EBM[-1])
                data.currentWBM = copy.deepcopy(data.WBM[-1])
                data.currentSBM = copy.deepcopy(data.SBM[-1])
                updateOccupiedRecord(data,x,y)
        elif data.currentItem == 'spikeEast':
            if (x,y) not in data.occupiedCoordinatesMap:
                data.ESM[-1].append((x,y))
                data.currentESM = copy.deepcopy(data.ESM[-1])
                data.spikeMapDict[-1].append((x,y,'e'))
                data.currentSpikeMap = copy.deepcopy(data.spikeMapDict[-1])
                data.EBM[-1].append((x,y))
                data.NBM[-1].append((x,y))
                data.SBM[-1].append((x,y))
                data.currentEBM = copy.deepcopy(data.EBM[-1])
                data.currentNBM = copy.deepcopy(data.NBM[-1])
                data.currentSBM = copy.deepcopy(data.SBM[-1])
                updateOccupiedRecord(data,x,y)
        elif data.currentItem == 'spikeWest':
            if (x,y) not in data.occupiedCoordinatesMap:
                data.WSM[-1].append((x,y))
                data.currentWSM = copy.deepcopy(data.WSM[-1])
                data.spikeMapDict[-1].append((x,y,'w'))
                data.currentSpikeMap = copy.deepcopy(data.spikeMapDict[-1])
                data.WBM[-1].append((x,y))
                data.NBM[-1].append((x,y))
                data.SBM[-1].append((x,y))
                data.currentWBM = copy.deepcopy(data.WBM[-1])
                data.currentNBM = copy.deepcopy(data.NBM[-1])
                data.currentSBM = copy.deepcopy(data.SBM[-1])
                updateOccupiedRecord(data,x,y)
        elif data.currentItem == 'bomb':
            if (x,y) not in data.occupiedCoordinatesMap:
                data.bombMapDict[-1].append((x,y))
                data.currentBombMap = copy.deepcopy(data.bombMapDict[-1])
                updateOccupiedRecord(data,x,y)
        elif data.currentItem == 'wormholeA':
            if (x,y) not in data.occupiedCoordinatesMap:
                data.wormholeAMapDict[-1].append((x,y))
                data.currentWormholeAMap = copy.deepcopy(data.wormholeAMapDict[-1])
                updateOccupiedRecord(data,x,y)
        elif data.currentItem == 'wormholeB':
            if (x,y) not in data.occupiedCoordinatesMap:
                data.wormholeBMapDict[-1].append((x,y))
                data.currentWormholeBMap = copy.deepcopy(data.wormholeBMapDict[-1])
                updateOccupiedRecord(data,x,y)
        elif data.currentItem == 'trap':
            if (x,y) not in data.occupiedCoordinatesMap:
                data.trapMapDict[-1].append((x,y))
                data.currentTrapMap = copy.deepcopy(data.trapMapDict[-1])
                updateOccupiedRecord(data,x,y)
        # delete items!
        elif data.currentItem == 'cross':
            if (x,y) in data.occupiedCoordinatesMap:
                # delete drop is diferent
                if data.occupiedCoordinatesMap.index((x,y)) == 0:
                    data.occupiedCoordinatesMap[0] = (-1,-1)
                    data.occupiedMap[0] = [(-1,-1,'drop')]
                    data.dropMapDict[-1] = Drop(-1,-1)
                    data.drop = copy.deepcopy(data.dropMapDict[data.level])
                # delete other items
                else:
                    deleteIndex = data.occupiedCoordinatesMap.index((x,y))
                    deleteItem = data.occupiedMap[deleteIndex][2]
                    if deleteItem == 'target':
                        data.targetMapDict[-1].remove((x,y))
                        data.currentTargetMap = copy.deepcopy(data.targetMapDict[-1])
                        deleteOccupiedRecord(data,deleteIndex)
                    elif deleteItem == 'scroll':
                        data.scrollMapDict[-1].remove((x,y))
                        data.currentScrollMap = copy.deepcopy(data.scrollMapDict[-1])
                        deleteOccupiedRecord(data,deleteIndex) 
                    elif deleteItem == 'brick':
                        data.brickMapDict[-1].remove((x,y))
                        data.currentBrickMap = copy.deepcopy(data.brickMapDict[-1])
                        data.EBM[-1].remove((x,y))
                        data.WBM[-1].remove((x,y))
                        data.NBM[-1].remove((x,y))
                        data.SBM[-1].remove((x,y))
                        data.currentEBM = copy.deepcopy(data.EBM[-1])
                        data.currentWBM = copy.deepcopy(data.WBM[-1])
                        data.currentNBM = copy.deepcopy(data.NBM[-1])
                        data.currentSBM = copy.deepcopy(data.SBM[-1])
                        deleteOccupiedRecord(data,deleteIndex)
                    elif deleteItem == 'spikeNorth':
                        data.NSM[-1].remove((x,y))
                        data.currentNSM = copy.deepcopy(data.NSM[-1])
                        data.spikeMapDict[-1].remove((x,y,'n'))
                        data.currentSpikeMap = copy.deepcopy(data.spikeMapDict[-1])
                        data.EBM[-1].remove((x,y))
                        data.WBM[-1].remove((x,y))
                        data.NBM[-1].remove((x,y))
                        data.currentEBM = copy.deepcopy(data.EBM[-1])
                        data.currentWBM = copy.deepcopy(data.WBM[-1])
                        data.currentNBM = copy.deepcopy(data.NBM[-1])
                        deleteOccupiedRecord(data,deleteIndex)
                    elif deleteItem == 'spikeSouth':
                        data.SSM[-1].remove((x,y))
                        data.currentSSM = copy.deepcopy(data.SSM[-1])
                        data.spikeMapDict[-1].remove((x,y,'s'))
                        data.currentSpikeMap = copy.deepcopy(data.spikeMapDict[-1])
                        data.EBM[-1].remove((x,y))
                        data.WBM[-1].remove((x,y))
                        data.SBM[-1].remove((x,y))
                        data.currentEBM = copy.deepcopy(data.EBM[-1])
                        data.currentWBM = copy.deepcopy(data.WBM[-1])
                        data.currentSBM = copy.deepcopy(data.SBM[-1])
                        deleteOccupiedRecord(data,deleteIndex)
                    elif deleteItem == 'spikeEast':
                        data.ESM[-1].remove((x,y))
                        data.currentESM = copy.deepcopy(data.ESM[-1])
                        data.spikeMapDict[-1].remove((x,y,'e'))
                        data.currentSpikeMap = copy.deepcopy(data.spikeMapDict[-1])
                        data.EBM[-1].remove((x,y))
                        data.NBM[-1].remove((x,y))
                        data.SBM[-1].remove((x,y))
                        data.currentEBM = copy.deepcopy(data.EBM[-1])
                        data.currentNBM = copy.deepcopy(data.NBM[-1])
                        data.currentSBM = copy.deepcopy(data.SBM[-1])
                        deleteOccupiedRecord(data,deleteIndex)
                    elif deleteItem == 'spikeWest':
                        data.WSM[-1].remove((x,y))
                        data.currentWSM = copy.deepcopy(data.WSM[-1])
                        data.spikeMapDict[-1].remove((x,y,'w'))
                        data.currentSpikeMap = copy.deepcopy(data.spikeMapDict[-1])
                        data.WBM[-1].remove((x,y))
                        data.NBM[-1].remove((x,y))
                        data.SBM[-1].remove((x,y))
                        data.currentWBM = copy.deepcopy(data.WBM[-1])
                        data.currentNBM = copy.deepcopy(data.NBM[-1])
                        data.currentSBM = copy.deepcopy(data.SBM[-1])
                        deleteOccupiedRecord(data,deleteIndex)
                    elif deleteItem == 'bomb':
                        data.bombMapDict[-1].remove((x,y))
                        data.currentBombMap = copy.deepcopy(data.bombMapDict[-1])
                        deleteOccupiedRecord(data,deleteIndex)
                    elif deleteItem == 'wormholeA':
                        data.wormholeAMapDict[-1].remove((x,y))
                        data.currentWormholeAMap = copy.deepcopy(data.wormholeAMapDict[-1])
                        deleteOccupiedRecord(data,deleteIndex)
                    elif deleteItem == 'wormholeB':
                        data.wormholeBMapDict[-1].remove((x,y))
                        data.currentWormholeBMap = copy.deepcopy(data.wormholeBMapDict[-1])
                        deleteOccupiedRecord(data,deleteIndex)
                    
                

# update the data.occupiedMap and data.occupiedCoordinatesMap
def updateOccupiedRecord(data,x,y):
    data.occupiedMap.append((x,y,data.currentItem))
    data.occupiedCoordinatesMap.append((x,y))

def deleteOccupiedRecord(data,deleteIndex):
    data.occupiedMap.pop(deleteIndex)
    data.occupiedCoordinatesMap.pop(deleteIndex)
    
def buildMyMazeKeyPressed(event, data):
    if event.keysym == 'c':
        data.currentItem = None
        data.occupiedMap = [(-1,-1,'drop')]
        data.occupiedCoordinatesMap = [(-1,-1)]
        
        data.dropMapDict[-1] = Drop(-1,-1)
        data.drop = copy.deepcopy(data.dropMapDict[-1])
        updateAllMapDicts(data)
        updateAllCurrentGeneralMaps(data)
        
        data.EBM[-1] = []
        data.WBM[-1] = []
        data.NBM[-1] = []
        data.SBM[-1] = []
        data.ESM[-1] = []
        data.WSM[-1] = []
        data.NSM[-1] = []
        data.SSM[-1] = []
        
        updateAllSpikeRealatedMaps(data)

def buildMyMazeTimerFired(data):
    drawBackgroundAnimationsTimer(data)

def buildMyMazeRedrawAll(canvas, data):
    color = 'beige'
    # the background must be draw first!
    canvas.create_image(data.width/2,data.height/2,image=data.playBGImage)
    # the grid for user to place item
    for i in range(15):
        x = 150+30*i
        y = 120+30*i
        canvas.create_line(x,120,x,540,fill=color)
        canvas.create_line(150,y,570,y,fill=color)
    canvas.create_text(360,15,text='Click the items on the left,',
    font='fixedsys 15',fill=color)
    canvas.create_text(360,45,text='then click on the grid to place it.',
    font='fixedsys 15',fill=color)
    canvas.create_text(360,75,
    text='To delete the item, first click the red cross,',
    font='fixedsys 15',fill=color)
    canvas.create_text(360,105,
    text='then click on the item on the board to delete it.',
    font='fixedsys 15',fill=color)
    canvas.create_image(data.width/15,1*data.height/10,image=data.dropImage)
    canvas.create_image(data.width/15,2*data.height/10,image=data.brickImage)
    canvas.create_image(data.width/15,3*data.height/10,image=data.targetImage)
    canvas.create_image(data.width/15,4*data.height/10,image=data.scrollImage)
    canvas.create_image(data.width/15,5*data.height/10,image=data.spikeNorthImage)
    canvas.create_image(data.width/15,6*data.height/10,image=data.spikeSouthImage)
    canvas.create_image(data.width/15,7*data.height/10,image=data.spikeEastImage)
    canvas.create_image(data.width/15,8*data.height/10,image=data.spikeWestImage)
    canvas.create_image(data.width/6, 1*data.height/10,image=data.crossImage)
    canvas.create_image(data.width/6, 2*data.height/10,image=data.bombImage)
    canvas.create_image(data.width/6, 3*data.height/10,image=data.wormholeAImage)
    canvas.create_image(data.width/6, 4*data.height/10,image=data.wormholeBImage)
    canvas.create_image(data.width/6, 5*data.height/10,image=data.trap1Image)
    canvas.create_text(100,600,text='PLAY MY GAME!',font='fixedsys 15',fill=color)
    canvas.create_text(300,590,text='PRESS \'C\'',font='fixedsys 15',fill=color)
    canvas.create_text(300,610,text='TO CLEAR BOARD',font='fixedsys 15',fill=color)
    canvas.create_text(500,600,text='MENU',font='fixedsys 15',fill=color)
    Drop.draw(canvas,data)
    Brick.draw(canvas,data)
    Target.draw(canvas,data)
    Scroll.draw(canvas,data)
    Spike.draw(canvas,data)
    Bomb.draw(canvas,data)
    WormholeA.draw(canvas,data)
    WormholeB.draw(canvas,data)
    Trap.draw(canvas,data)
    drawSnowflakes(canvas,data)