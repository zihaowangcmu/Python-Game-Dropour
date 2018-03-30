############################################################################################
# helpPage1 mode
# This is the first page of help menu
# Introduce somt items and how to play
############################################################################################

from drawBackgroundAnimationsTimer import*
from drawBackgroundAnimations import *

def helpPage1MousePressed(event, data):
    # Click the BACK TO MENU button and go back to menu
    if 110 < event.x < 230 and 530 < event.y < 550:
           data.mode = 'menu'
    # Click the NEXT PAGE button and go to next help page
    if 110 < event.x < 230 and 570 < event.y < 590:
           data.mode = 'helpPage2'

def helpPage1KeyPressed(event, data):
    pass
    
def helpPage1TimerFired(data):
    drawBackgroundAnimationsTimer(data)
    
def helpPage1RedrawAll(canvas,data):
    color = 'black'
    # background
    canvas.create_image(data.width/2,data.height/2,image=data.helpBGImage)
    # The title
    canvas.create_text(300,45,text='HELP',font='fixedsys 25 roman',fill=color)
    # Some tips
    # Line 1
    canvas.create_text(50,80,anchor='nw',text='In this game, you are going to',
    font='fixedsys 15',fill=color)
    canvas.create_text(50,100,anchor='nw',text='control the water drop.',
    font='fixedsys 15',fill=color)
    canvas.create_image(470,100,image = data.arrowImage)
    canvas.create_image(520,100,image = data.dropImage)
    # Line 2
    canvas.create_text(50,130,anchor='nw',
    text='Press \'w\', \'s\', \'a\', \'d\' to move',font='fixedsys 15',fill=color)
    canvas.create_text(50,150,anchor='nw',
    text='up, down, left and right.',font='fixedsys 15',fill=color)
    canvas.create_image(470,150,image = data.arrowImage)
    canvas.create_image(520,150,image = data.wasdImage)
    # Line 3
    canvas.create_text(50,180,anchor='nw',
    text='When the drop is moving,',font='fixedsys 15',fill=color)
    canvas.create_text(50,200,anchor='nw',
    text='you can\'t change its direction,',font='fixedsys 15',fill=color)
    canvas.create_text(50,220,anchor='nw',
    text='until it stops somewhere.',font='fixedsys 15',fill=color)
    # Line 4
    canvas.create_text(50,250,anchor='nw',
    text='When the drop hits a brick,',font='fixedsys 15',fill=color)
    canvas.create_text(50,270,anchor='nw',
    text='the drop stops right there.',font='fixedsys 15',fill=color)
    canvas.create_image(470,270,image = data.arrowImage)
    canvas.create_image(520,270,image = data.brickImage)
    # Line 5
    canvas.create_text(50,300,anchor='nw',
    text='Try to reach all the stars on the map.',
    font='fixedsys 15',fill=color)
    canvas.create_image(470,305,image = data.arrowImage)
    canvas.create_image(520,305,image = data.targetImage)
    # Line 6
    canvas.create_text(50,330,anchor='nw',
    text='When all of them are reached,',font='fixedsys 15',fill=color)
    canvas.create_text(50,350,anchor='nw',
    text='you will make it to next level!',font='fixedsys 15',fill=color)
    # Line 7
    canvas.create_text(50,380,anchor='nw',
    text='Try to avoid the bomb!',font='fixedsys 15',fill=color)
    canvas.create_image(470,385,image = data.arrowImage)
    canvas.create_image(520,385,image = data.bombImage)
    # Line 7
    canvas.create_text(50,410,anchor='nw',
    text='Also, try to avoid the spikes,',font='fixedsys 15',fill=color)
    canvas.create_text(50,430,anchor='nw',
    text='but you are safe unless facing the tip.',font='fixedsys 15',fill=color)
    canvas.create_image(470,430,image = data.arrowImage)
    canvas.create_image(520,430,image = data.spikeNorthImage)
    # BACK TO MENU button
    canvas.create_text(200,540,text='BACK TO MENU',font='fixedsys 15',fill=color)
    canvas.create_image(120,540,image = data.menuButtonImage)
    # NEXT PAGE button
    canvas.create_text(200,580,text='NEXT PAGE',font='fixedsys 15',fill=color)
    canvas.create_image(120,580,image = data.nextButtonImage)
    # DRAW A DOG!
    drawDog(canvas,data)