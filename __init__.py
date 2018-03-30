############################################################################################
# The tkinter frame work is cited from CMU 15112 website!
# The mode dispatcher frame work is cited from CMU 15112 website!
# The pictures used are cited from websites, whose specific url are listed ahead of the according lines.
# Modes are considered
# NOTICE1: data.dropMapDict is slightly different from other mapDict, it is a dict of instanses of Drop class (POSITION: init(data))
# NOTICE2: the maps are brought in with copy.deepcopy(), so that no alias will be introduced
# NOTICE3: the data.currentBrikMaps is old version. Since the non-spine sides are using the same algorithm to judge collision, they should be added into the brickmaps. New version:data.currentSouthBrickMaps,data.currentNorthBrickMaps,    data.currentEastBrickMaps,data.currentWestBrickMaps.
# NOTICE4: all the positions of the items are represented in (x,y), meaning the row/col indices, which actually means the 30*(x-1)+15,30*(y-1)+15 on the map
# NOTICE5: if a new item is added, remember to modify 3 update functions!
############################################################################################

from tkinter import *
import winsound
from MenuMode import *
from playGameMode import *
from HelpPage1Mode import *
from HelpPage2Mode import *
from AboutMeMode import *
from BuildMyMazeMode import *
from PauseMode import *
from CustomizedMapVictoryMode import *
from IntervalMode import *
from ClearanceMode import *
from PlaybackMode import *
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
import copy

####################################
# init
####################################
def init(data):
    data.mode = 'menu' # This is the menu mode
    data.level = -1 # make the level be -1 to be used for BUILD MY MAZE mode!
    data.totalLevels = 9 # this is 1 larger than the actual levels, for convenient usage.
    data.currentScore = 0
    data.accumulatedScore = 0
    data.currentIndex = -1 # record playback index
    data.playbackMap = [[],[],[]] # record your last solution
    data.playTime = 0 # record yout tour-time
    data.step = 0 # record your tour step index
    data.MINSteps = {-1:"?",1:"5",2:"7",3:"3",4:"7",5:"6",6:"7",7:"3",8:"3"}
    
    # initialize the time of background animation
    data.snowflakeTime = 0
    data.fallingLeavesTime = 0
    data.dogTime = 0
    
    # record the occupied positions with the item name
    # used in deleting items
    # the first element is set to be (-1,-1), and it is reserved for record drop
    # since drop is different from others, only one drop can exist, this makes finding
    # and checking drop position easy
    data.occupiedMap = [(-1,-1,'drop')]
    # record the occupied positions only, no more items can be placed overlap
    # used in placing items. The (-1,-1) is the same as data.occupiedMap
    data.occupiedCoordinatesMap = [(-1,-1)]
    data.currentItem = None # describe the current selected item in BUILD MY MAZE mode
    # This image is cited from https://play.blocksworld.com/play?world_id=26183522
    data.dropImage = PhotoImage(file='pictures/drop.gif')
    # The following 3 images are cited from https://gamejolt.com/games/erayu/109632
    data.menuBGImage = PhotoImage(file='pictures/menuBG.png')
    data.playBGImage = PhotoImage(file='pictures/playBG.png')
    data.helpBGImage = PhotoImage(file='pictures/helpBG.png')
    data.aboutmeBGImage = PhotoImage(file='pictures/aboutmeBG.png')
    # This image is cited from https://www.roblox.com/library/170321226/sanic-ring-1
    data.scrollImage = PhotoImage(file='pictures/scrollImage.gif')
    # This image is cited from http://img.neoseeker.com/v_concept_art.php?caid=36373
    data.brickImage = PhotoImage(file='pictures/brick.png')
    # This image is cited from 
    # https://www.brik.co/blogs/pixel-art/super-mario-galaxy-luma-star-pixel-art
    data.targetImage = PhotoImage(file='pictures/target.gif')
    # The following four images are modified from 
    # https://www.brik.co/blogs/pixel-art/candy-corn-pixel-art
    data.spikeNorthImage = PhotoImage(file='pictures/spikeNorth.gif')
    data.spikeSouthImage = PhotoImage(file='pictures/spikeSouth.gif')
    data.spikeEastImage = PhotoImage(file='pictures/spikeEast.gif')
    data.spikeWestImage = PhotoImage(file='pictures/spikeWest.gif')
    # This image is cited from http://piq.codeus.net/picture/327376/med_pack
    data.crossImage = PhotoImage(file='pictures/cross.png')
    # This image is cited from http://piq.codeus.net/picture/8582/bomb
    data.bombImage = PhotoImage(file='pictures/bomb.png')
    # This image is cited from https://www.thinglink.com/scene/657786259783024642
    data.wormholeAImage = PhotoImage(file='pictures/wormholeA.png')
    # This image is edited from https://www.thinglink.com/scene/657786259783024642
    data.wormholeBImage = PhotoImage(file='pictures/wormholeB.png')
    # This image is cited from https://lowpolypix.deviantart.
    # com/art/Super-Dragonsin-Saga-Items-Free-Use-345202858
    data.trap1Image = PhotoImage(file='pictures/trap1.png')
    # This image is cited from https://lowpolypix.deviantart.
    # com/art/Super-Dragonsin-Saga-Items-Free-Use-345202858
    data.trap2Image = PhotoImage(file='pictures/trap2.png')
    # This image is cited from https://www.redbubble.com/fr/people/thesaurusrex/works
    # /21656630-wasd-keys-black?p=womens-relaxed-fit
    data.wasdImage = PhotoImage(file='pictures/wasd.png')
    # This image is cited from http://photobucket.com/gifs/pink%20arrow%20pixel
    data.arrowImage = PhotoImage(file='pictures/arrow.png')
    # This image is cited from https://opengameart.org/content/home-button-pixel
    data.menuButtonImage = PhotoImage(file='pictures/menuButton.png')
    # The following 2 images are cited from 
    # https://opengameart.org/content/restart-button-pixel
    data.nextButtonImage = PhotoImage(file='pictures/nextButton.png')
    data.prevButtonImage = PhotoImage(file='pictures/prevButton.png')
    # This image is cited from 
    # https://free.clipartof.com/details/12-Free-Vector-Illustration-Of-A-Question-Mark-Icon
    data.helpButtonImage = PhotoImage(file='pictures/helpButton.png')
    # This image is cited from http://pixelartmaker.com/art/2fec8acf327f433
    data.playbackButtonImage = PhotoImage(file='pictures/playback.png')
    
    # The following 4 images are cited from
    # http://www.dickbaldwin.com/XNA/XNA0122/XNA0122.htm
    data.dog1Image = PhotoImage(file='pictures/dog1.png')
    data.dog2Image = PhotoImage(file='pictures/dog2.png')
    data.dog3Image = PhotoImage(file='pictures/dog3.png')
    data.dog4Image = PhotoImage(file='pictures/dog4.png')
    
    
    # The next 4 images are cited from 
    # https://mrbubblewand.wordpress.com/2010/01/18/animation-magic_004/
    data.snowflake1Image = PhotoImage(file='pictures/snow1.png')
    data.snowflake2Image = PhotoImage(file='pictures/snow2.png')
    data.snowflake3Image = PhotoImage(file='pictures/snow3.png')
    data.snowflake4Image = PhotoImage(file='pictures/snow4.png')
    # The next 4 images are cited and eidted from
    # https://www.pinterest.com/pin/375839531394461912/
    data.leaf1Image = PhotoImage(file='pictures/leaf1.png')
    data.leaf2Image = PhotoImage(file='pictures/leaf2.png')
    data.leaf3Image = PhotoImage(file='pictures/leaf3.png')
    data.leaf4Image = PhotoImage(file='pictures/leaf4.png')
    
    data.dropMapDict = dropMapDict
    data.brick = Brick()
    data.scroll = Scroll()
    data.target = Target()
    data.spike = Spike()
    data.bomb = Bomb()
    data.wormholeA = WormholeA()
    data.wormholeB = WormholeB()
    data.trap = Trap()
    
    # update all the maps!
    updateAllMapDicts(data)
    updateAllCurrentGeneralMaps(data)
    
    ### The following 2 blocks will not affected by adding new classes ###
    # data.ESM/WSM/NSM/SSM are short for data.East/West/North/SouthSpikeMap
    # get spike maps which are seperated by 4 directions!
    data.ESM = makeSpikeMaps(data.spikeMapDict,'east',data.totalLevels)
    data.WSM = makeSpikeMaps(data.spikeMapDict,'west',data.totalLevels)
    data.NSM = makeSpikeMaps(data.spikeMapDict,'north',data.totalLevels)
    data.SSM = makeSpikeMaps(data.spikeMapDict,'south',data.totalLevels)
    
    # data.EBM/WBM/NBM/SBM are short for data.East/West/North/SouthBrickMap
    data.EBM = makeBarrierMaps(data.brickMapDict,data.spikeMapDict,'east',data.totalLevels)
    data.WBM = makeBarrierMaps(data.brickMapDict,data.spikeMapDict,'west',data.totalLevels)
    data.NBM = makeBarrierMaps(data.brickMapDict,data.spikeMapDict,'north',data.totalLevels)
    data.SBM = makeBarrierMaps(data.brickMapDict,data.spikeMapDict,'south',data.totalLevels)
    
    # update spike related maps!
    updateAllSpikeRealatedMaps(data)
    
    pass
####################################
# mode dispatcher
# The mode dispatcher frame work is copied from CMU 15112 website!
####################################
def mousePressed(event, data):
    if (data.mode == "menu"):         menuMousePressed(event, data)
    elif (data.mode == "playGame"):   playGameMousePressed(event, data)
    elif (data.mode == "helpPage1"):  helpPage1MousePressed(event, data)
    elif (data.mode == "helpPage2"):  helpPage2MousePressed(event, data)
    elif (data.mode == "pause"):      pauseMousePressed(event, data)
    elif (data.mode == "aboutMe"):    aboutMeMousePressed(event, data)
    elif (data.mode == "buildMyMaze"):buildMyMazeMousePressed(event, data)
    elif (data.mode == "CMVictory"):  CMVictoryMousePressed(event, data)
    elif (data.mode == "interval"):   intervalMousePressed(event, data)
    elif (data.mode == "clearance"):  clearanceMousePressed(event, data)
    elif (data.mode == "playback"):   playbackMousePressed(event, data)
    

def keyPressed(event, data):
    if (data.mode == "menu"):         menuKeyPressed(event, data)
    elif (data.mode == "playGame"):   playGameKeyPressed(event, data)
    elif (data.mode == "helpPage1"):  helpPage1KeyPressed(event, data)
    elif (data.mode == "helpPage2"):  helpPage2KeyPressed(event, data)
    elif (data.mode == "pause"):      pauseKeyPressed(event, data)
    elif (data.mode == "aboutMe"):    aboutMeKeyPressed(event, data)
    elif (data.mode == "buildMyMaze"):buildMyMazeKeyPressed(event, data)
    elif (data.mode == "CMVictory"):  CMVictoryKeyPressed(event, data)
    elif (data.mode == "interval"):   intervalKeyPressed(event, data)
    elif (data.mode == "clearance"):  clearanceKeyPressed(event, data)
    elif (data.mode == "playback"):   playbackKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "menu"):         menuTimerFired(data)
    elif (data.mode == "playGame"):   playGameTimerFired(data)
    elif (data.mode == "helpPage1"):  helpPage1TimerFired(data)
    elif (data.mode == "helpPage2"):  helpPage2TimerFired(data)
    elif (data.mode == "pause"):      pauseTimerFired(data)
    elif (data.mode == "aboutMe"):    aboutMeTimerFired(data)
    elif (data.mode == "buildMyMaze"):buildMyMazeTimerFired(data)
    elif (data.mode == "CMVictory"):  CMVictoryTimerFired(data)
    elif (data.mode == "interval"):   intervalTimerFired(data)
    elif (data.mode == "clearance"):  clearanceTimerFired(data)
    elif (data.mode == "playback"):   playbackTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "menu"):         menuRedrawAll(canvas, data)
    elif (data.mode == "playGame"):   playGameRedrawAll(canvas, data)
    elif (data.mode == "helpPage1"):  helpPage1RedrawAll(canvas, data)
    elif (data.mode == "helpPage2"):  helpPage2RedrawAll(canvas, data)
    elif (data.mode == "pause"):      pauseRedrawAll(canvas, data)
    elif (data.mode == "aboutMe"):    aboutMeRedrawAll(canvas, data)
    elif (data.mode == "buildMyMaze"):buildMyMazeRedrawAll(canvas, data)
    elif (data.mode == "CMVictory"):  CMVictoryRedrawAll(canvas, data)
    elif (data.mode == "interval"):   intervalRedrawAll(canvas, data)
    elif (data.mode == "clearance"):  clearanceRedrawAll(canvas, data)
    elif (data.mode == "playback"):   playbackRedrawAll(canvas, data)

####################################
# use the run function as-is
# This is copied from CMU 15112 website!
####################################

def run(width=500, height=500):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Create root before calling init (so we can create images in init)
    root = Toplevel()
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 30 # milliseconds
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed

def main():
    winsound.PlaySound("sound/bgm.wav", winsound.SND_ASYNC|winsound.SND_LOOP|winsound.SND_FILENAME|winsound.SND_NOSTOP)
    run(600, 630)

if __name__ == '__main__':
    main()