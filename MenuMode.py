############################################################################################
# menu mode
# There are four buttons here:
# 1.START JOURNEY
# 2.HELP
# 3.BUILD MY MAZE
# 4.ABOUT ME
############################################################################################

import copy
from updateAllMapDicts import *
from updateAllCurrentGeneralMaps import *
from updateAllSpikeRealatedMaps import *
from drawBackgroundAnimationsTimer import*
from drawBackgroundAnimations import *

def menuMousePressed(event,data):
    # Click the START JOURNEY button and play!!!
    if 160 < event.x < 440 and 190 < event.y < 250:
           data.mode = 'playGame'
           # modify here to test!
           data.level = 1
           updateAllCurrentGeneralMaps(data)
           updateAllSpikeRealatedMaps(data)
           

    # Click the HELP button and learn how to play
    elif 160 < event.x < 440 and 290 < event.y < 350:
           data.mode = 'helpPage1'
           
    # Click the BUILD MY MAZE button to customize a map
    elif 160 < event.x < 440 and 390 < event.y < 450:
           data.mode = 'buildMyMaze'
           data.level = -1
           updateAllCurrentGeneralMaps(data)
           updateAllSpikeRealatedMaps(data)
           
    # Click the ABOUT ME button and learn about this game
    elif 160 < event.x < 440 and 490 < event.y < 550:
           data.mode = 'aboutMe'
    
def menuKeyPressed(event, data):
    pass
    
def menuTimerFired(data):
    drawBackgroundAnimationsTimer(data)
    
def menuRedrawAll(canvas, data):
    color = 'floral white'
    # The background
    canvas.create_image(data.width/2,data.height/2,image=data.menuBGImage)
    # The title
    canvas.create_text(300,80,text = 'Dropour',
    font='fixedsys 40',fill=color)
    # START JOURNEY button
    canvas.create_text(300,220,text='START JOURNEY',font='fixedsys 20',fill=color)
    # HELP button
    canvas.create_text(300,320,text='HELP',font='fixedsys 20',fill=color)
    # BUILD MY MAZE button
    canvas.create_text(300,420,text='BUILD MY MAZE',font='fixedsys 20',fill=color)
    # ABOUT ME button
    canvas.create_text(300,520,text='ABOUT ME',font='fixedsys 20',fill=color)
    drawFallingLeaves(canvas,data)