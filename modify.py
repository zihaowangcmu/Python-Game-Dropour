###############################################################################################
# This function modify the coordinates of the water drop to a decent position.
# In this game, the side length of the brick(square) is 30.
# Also, the radius of the water drop is 30.
# This means the (x,y) must be 30*n+15, where n belongs to [1,18],
# which is closed on both sides.
# We force the (x,y) to convert to the nearest reasonable position.
# On one side, the drop looks nice
# On the other hand, it ensures the correcness of the function used for check collision
# Still, it realizes the bouncing back effect surprisingly??????
###############################################################################################

def modifiedCoord(x):
    return round(x)