__author__ = 'Sam Vitello'

import nimble
from nimble import cmds
from random import randint

def createBubbles(time):
    #Make Column of Water
    """r=3
    h=10
    water = cmds.polyCylinder(r=r, h=h)
    cmds.move(0,5,0)

    Without a material it doesn't look fantastic
    Material best created and assigned manually
    """


    #Bubble Creation
    """
    Creates bubble (of raidus size .3) Keystroking is assigned from the top down
    """
    for i in range(0,time/2):
        #Get psudo-random motion paths for each bubble
        startTime = randint(0,time-20)
        xVariation = randint(-1,1)
        zVariation = randint(-1,1)
        startX = randint(-5,5)
        startZ = randint(-5,5)

        #create bubble
        r=.3
        c = cmds.polySphere(r=r)
        cmds.move(startX,10,startZ)
        cmds.setAttr(c[0]+".visibility",0)
        cmds.setKeyframe(time=startTime+45)
        cmds.setAttr(c[0]+".visibility",1)
        cmds.rotate(145,0,0)
        cmds.scale(1,.8,1)
        cmds.setKeyframe(time=startTime+40)
        cmds.move(startX+xVariation,6,startZ+zVariation)
        cmds.rotate(75,0,0)
        cmds.setKeyframe(time=startTime+30)
        cmds.move(startX,2,startZ)
        cmds.rotate(0,0,0)
        cmds.setKeyframe(time=startTime+20)
        cmds.move(startX,0,startZ)
        cmds.scale(.2,.2,.2)
        cmds.setKeyframe(time=startTime+1)


