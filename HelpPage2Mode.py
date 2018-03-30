############################################################################################
# helpPage2 mode
# This is the second page of help menu
# Introduce some functions of pressing keys
############################################################################################

from drawBackgroundAnimationsTimer import*
from drawBackgroundAnimations import *

def helpPage2MousePressed(event, data):
    # Click the BACK TO MENU button and go back to menu
    if 110 < event.x < 230 and 530 < event.y < 550:
           data.mode = 'menu'
    # Click the NEXT PAGE button and go to next help page
    if 110 < event.x < 230 and 570 < event.y < 590:
           data.mode = 'helpPage1'

def helpPage2KeyPressed(event, data):
    pass
    
def helpPage2TimerFired(data):
    drawBackgroundAnimationsTimer(data)
    
def helpPage2RedrawAll(canvas,data):
    color = 'black'
    # background
    canvas.create_image(data.width/2,data.height/2,image=data.helpBGImage)
    # The title
    canvas.create_text(300,45,text='HELP',font='fixedsys 25 roman',fill=color)
    # Some tips
    # Line 1
    canvas.create_text(50,80,anchor='nw',
    text='Go into a wormhole, and you',font='fixedsys 15',fill=color)
    canvas.create_text(50,100,anchor='nw',
    text='will be sent out from another end.',font='fixedsys 15',fill=color)
    canvas.create_text(50,120,anchor='nw',
    text='Wormholes appear in pairs.',font='fixedsys 15',fill=color)
    canvas.create_image(470,115,image = data.arrowImage)
    canvas.create_image(520,100,image = data.wormholeAImage)
    canvas.create_image(520,130,image = data.wormholeBImage)
    # Line 2
    canvas.create_text(50,160,anchor='nw',
    text='Rings will appear at the boundary',font='fixedsys 15',fill=color)
    canvas.create_text(50,180,anchor='nw',
    text='of the map, you can make a loop by them.',font='fixedsys 15',fill=color)
    canvas.create_image(470,180,image = data.arrowImage)
    canvas.create_image(520,180,image = data.scrollImage)
    # Line 3
    canvas.create_text(50,220,anchor='nw',
    text='The traps stays good before triggered.',font='fixedsys 15',fill=color)
    canvas.create_text(50,240,anchor='nw',
    text='Once triggered, they will block your way.',font='fixedsys 15',fill=color)
    canvas.create_image(470,240,image = data.arrowImage)
    canvas.create_image(520,225,image = data.trap1Image)
    canvas.create_image(520,255,image = data.trap2Image)
    # Line 4
    canvas.create_text(50,270,anchor='nw',
    text='Here are some shortcuts:',font='fixedsys 15',fill=color)
    canvas.create_text(50,290,anchor='nw',
    text='Press \'R\' to replay the current level;',font='fixedsys 15',fill=color)
    canvas.create_text(50,310,anchor='nw',
    text='Press \'P\' to pause the current level;',font='fixedsys 15',fill=color)
    canvas.create_text(50,330,anchor='nw',
    text='Press \'C\' to clear the map you just built;',font='fixedsys 15',fill=color)
    # Line 5
    canvas.create_text(50,360,anchor='nw',
    text='In BUILD MY MAZE mode, follow the instructions,',font='fixedsys 15',fill=color)
    canvas.create_text(50,380,anchor='nw',
    text='and build your exclusive AMAZING maze!!!',font='fixedsys 15',fill=color)
    # Line 6
    canvas.create_text(50,410,anchor='nw',
    text='PLAY NOW and HAVE FUN!',font='fixedsys 15',fill=color)
    
    
    # BACK TO MENU button
    canvas.create_text(200,540,text='BACK TO MENU',font='fixedsys 15',fill=color)
    canvas.create_image(120,540,image = data.menuButtonImage)
    # PREV PAGE button
    canvas.create_text(200,580,text='PREV PAGE',font='fixedsys 15',fill=color)
    canvas.create_image(120,580,image = data.prevButtonImage)
    # DRAW A DOG!
    drawDog(canvas,data)