#############################################################################################
# This function make the drop map for each level
# The (x,y) indicates the row/col indices
# So that the actual position is (15+30*x,15+30*y)
#############################################################################################

from Drop import *

dropMapDict = dict()

drop_1 = Drop(-1,-1) # prepared for BUILD MY MAZE mode
drop0 = Drop(-1,-1) # prepared for BUILD MY MAZE mode
drop1 = Drop(9,10)
drop2 = Drop(7,10)
drop3 = Drop(13,10)
drop4 = Drop(9,12)
drop5 = Drop(13,12)
drop6 = Drop(10,10)
drop7 = Drop(9,10)
drop8 = Drop(7,9)

dropMapDict[-1] = drop_1 # prepared for BUILD MY MAZE mode
dropMapDict[0] = drop0 # prepared for BUILD MY MAZE mode
dropMapDict[1] = drop1
dropMapDict[2] = drop2
dropMapDict[3] = drop3
dropMapDict[4] = drop4
dropMapDict[5] = drop5
dropMapDict[6] = drop6
dropMapDict[7] = drop7
dropMapDict[8] = drop8