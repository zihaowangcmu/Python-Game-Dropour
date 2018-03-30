##############################################################################################
# This is about me mode
# Just have some fun!
##############################################################################################

def aboutMeMousePressed(event, data):
    # Click the BACK TO MENU button and go back to menu
    if 200 < event.x < 380 and 580 < event.y < 620:
           data.mode = 'menu'

def aboutMeKeyPressed(event, data):
    pass

def aboutMeTimerFired(data):
    pass

def aboutMeRedrawAll(canvas, data):
    color = 'saddle brown'
    canvas.create_image(data.width/2,data.height/2,image=data.aboutmeBGImage)
    # The title
    canvas.create_text(300,45,text='ABOUT ME',font='fixedsys 25',fill=color)
    # Line 1
    canvas.create_text(20,80,anchor='nw',
    text='This is the term project',font='fixedsys 25',fill=color)
    canvas.create_text(20,130,anchor='nw',
    text='for CMU 15-112.',font='fixedsys 25',fill=color)
    # Line 2
    canvas.create_text(20,380,anchor='nw',
    text='Producer: Zihao Wang',font='fixedsys 15',fill=color)
    # Line 3
    canvas.create_text(20,430,anchor='nw',
    text='Andrew ID: zwang2',font='fixedsys 15',fill=color)
    # Line 4
    canvas.create_text(20,480,anchor='nw',
    text='Hope you love this game!',font='fixedsys 15',fill=color)
    canvas.create_text(420,480,anchor='nw',
    text='Have fun!',font='fixedsys 15',fill=color)
    
    
    # BACK TO MENU button
    canvas.create_text(300,600,text='BACK TO MENU',font='fixedsys 15',fill=color)
    canvas.create_image(200,600,image = data.menuButtonImage)