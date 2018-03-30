############################################################################################
# calculate time of the animations of backgrounds
############################################################################################

def drawBackgroundAnimationsTimer(data):
    data.snowflakeTime += 1
    data.fallingLeavesTime += 1
    data.dogTime += 1
    if data.snowflakeTime == 49:
        data.snowflakeTime = 0
    if data.dogTime == 16:
        data.dogTime = 0