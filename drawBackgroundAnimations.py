############################################################################################
# This function draws the animated images and some texts on background
############################################################################################

# drawScore displays your score
def drawScore(canvas,data):
    color = 'beige'
    canvas.create_text(130,615,text='Collected Stars: %s'%data.currentScore,
    font='fixedsys 15',fill=color)
    
# drawLevel displays your level
def drawLevel(canvas,data):
    color = 'beige'
    canvas.create_text(520,615,text='Level: %s'%data.level,
    font='fixedsys 15',fill=color)

def drawBestSolution(canvas,data):
    color = 'beige'
    canvas.create_text(350,615,text='MIN Steps: %s'%data.MINSteps[data.level],
    font='fixedsys 15',fill=color)

def drawPlaybackTable(canvas,data):
    # following 4 lines indicates the start location of the printed texts
    x1 = 200
    x2 = 300
    x3 = 400
    starty = 70
    color = 'white'
    canvas.create_text(x2,30,text='Your Tour:',font='fixedsys 15',fill=color)
    canvas.create_text(x1,50,text='STEP',font='fixedsys 15',fill=color)
    canvas.create_text(x2,50,text='ACTION',font='fixedsys 15',fill=color)
    canvas.create_text(x3,50,text='TIME(ms)',font='fixedsys 15',fill=color)
    if data.currentIndex != -1:
        for i in range(data.currentIndex+1):
            y = starty + 20*i
            if y >= 190:
                y += 200
            step = data.playbackMap[0][i]
            action = data.playbackMap[1][i]
            time = data.playbackMap[2][i]
            canvas.create_text(x1,y,text=step,font='fixedsys 15',fill=color)
            canvas.create_text(x2,y,text=action,font='fixedsys 15',fill=color)
            canvas.create_text(x3,y,text=time,font='fixedsys 15',fill=color)

def drawSnowflakes(canvas,data):
    if data.snowflakeTime//8 == 0 or data.snowflakeTime//8 == 6:
        snowflake = data.snowflake1Image
    elif data.snowflakeTime//8 == 1 or data.snowflakeTime//8 == 5:
        snowflake = data.snowflake2Image
    elif data.snowflakeTime//8 == 2 or data.snowflakeTime//8 == 4:
        snowflake = data.snowflake3Image
    elif data.snowflakeTime//8 == 3:
        snowflake = data.snowflake4Image
    snowflakesMap = \
    [(100,100),(130,160),(500,600),(70,250),(150,420),(300,40),(360,120),(500,80)
    ]
    for pair in snowflakesMap:
        x = pair[0]
        y = pair[1]
        canvas.create_image(x,y,image = snowflake)
        
def drawFallingLeaves(canvas,data):
    initialPositionMap = [(50,100),(180,20),(350,300),(520,480)]
    leafImageMap = [data.leaf1Image,data.leaf2Image,data.leaf3Image,data.leaf4Image]
    for i in range(4):
        x = initialPositionMap[i][0]
        y = (initialPositionMap[i][1] + data.fallingLeavesTime*10)%data.height
        canvas.create_image(x,y,image = leafImageMap[i])
        
def drawDog(canvas,data):
    if data.dogTime//4 == 0:
        dog = data.dog1Image
    elif data.dogTime//4 == 1:
        dog = data.dog2Image
    elif data.dogTime//4 == 2:
        dog = data.dog3Image
    elif data.dogTime//4 == 3:
        dog = data.dog4Image
    canvas.create_image(300,540,image = dog)