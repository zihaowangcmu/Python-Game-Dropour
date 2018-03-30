############################################################################################
# This is interval mode.
# If you finish one level, and you don't clear them all, then you will jump to this page.
############################################################################################

import copy
from updateAllMapDicts import *
from updateAllCurrentGeneralMaps import *
from updateAllSpikeRealatedMaps import *
from updatePlaybackThings import *
from drawBackgroundAnimationsTimer import*
from drawBackgroundAnimations import *

def intervalMousePressed(event, data):
    # Click the PLAYBACK button and review your tour
    if 160 < event.x < 440 and 280 < event.y < 360:
        data.mode = 'playback'
        data.currentScore = 0
        # this time, playTime record the replaying time 
        # so that the game displays correctly
        data.playTime = 0
        updateAllCurrentGeneralMaps(data)
        updateAllSpikeRealatedMaps(data)
    
    # Click the CONTINUE button to go to next level
    if 160 < event.x < 440 and 360 < event.y < 440:
        data.level += 1
        data.mode = 'playGame'
        data.currentScore = 0
        updatePlaybackThings(data)
        updateAllCurrentGeneralMaps(data)
        updateAllSpikeRealatedMaps(data)

    # Click the MENU button to go to menu page
    elif 160 < event.x < 440 and 440 < event.y < 520:
        data.mode = 'menu'

def intervalKeyPressed(event, data):
    pass
    
def intervalTimerFired(data):
    drawBackgroundAnimationsTimer(data)

def intervalRedrawAll(canvas, data):
    color = 'white'
    # The background
    canvas.create_image(data.width/2,data.height/2,image=data.playBGImage)
    # The title
    canvas.create_text(300,170,text = 'Good Game!',font='fixedsys 40',fill=color)
    # PLAYBACK button
    canvas.create_text(300,320,text='PLAYBACK',font='fixedsys 20',fill=color)
    canvas.create_image(200,320,image = data.playbackButtonImage)
    # CONTINUE button
    canvas.create_text(300,400,text='CONTINUE',font='fixedsys 20',fill=color)
    canvas.create_image(200,400,image = data.nextButtonImage)
    # MENU button
    canvas.create_text(300,480,text='MENU',font='fixedsys 20',fill=color)
    canvas.create_image(200,480,image = data.menuButtonImage)
    drawSnowflakes(canvas,data)