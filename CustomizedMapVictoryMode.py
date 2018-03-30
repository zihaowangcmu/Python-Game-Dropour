############################################################################################
# customized map victory
# if the customized level(that is -1) is completed, this page will be displayed!
############################################################################################

import copy
from updateAllMapDicts import *
from updateAllCurrentGeneralMaps import *
from updateAllSpikeRealatedMaps import *
from updatePlaybackThings import *
from drawBackgroundAnimationsTimer import*
from drawBackgroundAnimations import *

def CMVictoryMousePressed(event, data):
    # Click the START JOURNEY button and play!!!
    if 160 < event.x < 440 and 200 < event.y < 300:
        data.mode = 'playGame'
        data.level = 1
        updatePlaybackThings(data)
        updateAllCurrentGeneralMaps(data)
        updateAllSpikeRealatedMaps(data)
        
    # Click the PLAYBACK button and review your tour
    if 160 < event.x < 440 and 300 < event.y < 400:
        data.mode = 'playback'
        data.currentScore = 0
        # this time, playTime record the replaying time 
        # so that the game displays correctly
        data.playTime = 0
        updateAllCurrentGeneralMaps(data)
        updateAllSpikeRealatedMaps(data)
    
    # Click the BUILD ANOTHER MAZE button to customize a map
    elif 160 < event.x < 440 and 400 < event.y < 500:
        data.mode = 'buildMyMaze'
        data.level = -1
        updatePlaybackThings(data)
        updateAllCurrentGeneralMaps(data)
        updateAllSpikeRealatedMaps(data)
    
    # Click the MENU button to go to menu page
    elif 160 < event.x < 440 and 500 < event.y < 600:
        data.mode = 'menu'
        updatePlaybackThings(data)

def CMVictoryKeyPressed(event, data):
    pass

def CMVictoryTimerFired(data):
    drawBackgroundAnimationsTimer(data)
    
def CMVictoryRedrawAll(canvas, data):
    color = 'white'
    # The background
    canvas.create_image(data.width/2,data.height/2,image=data.playBGImage)
    # The title
    canvas.create_text(300,80,text = 'Congratulations!',font='fixedsys 40',fill=color)
    canvas.create_text(300,140,text = 'Nice Map!',font='fixedsys 40',fill=color)
    # START JOURNEY button
    canvas.create_text(300,250,text='START JOURNEY',font='fixedsys 20',fill=color)
    # PLAYBACK button
    canvas.create_text(300,350,text='PLAYBACK',font='fixedsys 20',fill=color)
    # BUILD ANOTHER MAZE button
    canvas.create_text(300,450,text='BUILD ANOTHER MAZE',font='fixedsys 20',fill=color)
    # MENU button
    canvas.create_text(300,550,text='MENU',font='fixedsys 20',fill=color)
    # some animation
    drawSnowflakes(canvas,data)