############################################################################################
# This is pause mode
# After pressing 'P', the game will be paused
# 1.BACK TO GAME
# 2.BACK TO MENU
# 3.HELP
############################################################################################

from drawBackgroundAnimationsTimer import*
from drawBackgroundAnimations import *

def pauseMousePressed(event, data):
    if event.x < 440 and event.x > 160 and \
       event.y < 260 and event.y > 180:
           data.mode = 'playGame'
    if event.x < 440 and event.x > 160 and \
       event.y < 390 and event.y > 310:
           data.mode = 'menu'
    if event.x < 440 and event.x > 160 and \
       event.y < 520 and event.y > 440:
           data.mode = 'helpPage1'

def pauseKeyPressed(event, data):
    pass

def pauseTimerFired(data):
    drawBackgroundAnimationsTimer(data)

def pauseRedrawAll(canvas, data):
    color = 'white'
    # background
    canvas.create_image(data.width/2,data.height/2,image=data.playBGImage)
    # title
    canvas.create_text(300,105,text='PAUSE',font='fixedsys 25',fill=color)
    # BACK TO GAME button
    canvas.create_text(300,220,text='BACK TO GAME',font='fixedsys 20',fill=color)
    canvas.create_image(180,220,image = data.prevButtonImage)
    # BACK TO MENU button
    canvas.create_text(300,350,text='BACK TO MENU',font='fixedsys 20',fill=color)
    canvas.create_image(180,350,image = data.menuButtonImage)
    # HELP button
    canvas.create_text(300,480,text='HELP',font='fixedsys 20',fill=color)
    canvas.create_image(180,480,image = data.helpButtonImage)
    drawSnowflakes(canvas,data)