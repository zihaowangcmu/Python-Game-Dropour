############################################################################################
# This is clearance mode.
# This page appears when you finish all the levels!
############################################################################################

import copy
from updateAllMapDicts import *
from updateAllCurrentGeneralMaps import *
from updateAllSpikeRealatedMaps import *
from updatePlaybackThings import *
from drawBackgroundAnimationsTimer import*
from drawBackgroundAnimations import *

def clearanceMousePressed(event, data):
    if 160 < event.x < 440 and 290 < event.y < 350:
        data.mode = 'playback'
        data.currentScore = 0
        # this time, playTime record the replaying time 
        # so that the game displays correctly
        data.playTime = 0
        updateAllCurrentGeneralMaps(data)
        updateAllSpikeRealatedMaps(data)
        
    elif 160 < event.x < 440 and 370 < event.y < 430:
        data.mode = 'menu'

def clearanceKeyPressed(event, data):
    pass

def clearanceTimerFired(data):
    drawBackgroundAnimationsTimer(data)

def clearanceRedrawAll(canvas, data):
    color = 'white'
    # background
    canvas.create_image(data.width/2,data.height/2,image=data.playBGImage)
    # The title
    canvas.create_text(300,80,text = 'Congratulations!',font='fixedsys 40',fill=color)
    canvas.create_text(300,150,text = 'Game Cleared!',font='fixedsys 40',fill=color)
    # Your score
    canvas.create_text(300,240,text = 'Your Total Score is:',font='fixedsys 25',fill=color)
    canvas.create_text(300,270,text = data.accumulatedScore,font='fixedsys 25',fill=color)
    # PLAYBACK button
    canvas.create_text(300,340,text='PLAYBACK',font='fixedsys 20',fill=color)
    canvas.create_image(200,340,image = data.playbackButtonImage)
    # MENU button
    canvas.create_text(300,410,text='MENU',font='fixedsys 20',fill=color)
    canvas.create_image(200,410,image = data.menuButtonImage)
    drawSnowflakes(canvas,data)