__author__ = 'Sam Vitello'

import nimble
from nimble import cmds


def createBubble():
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
    r=.3
    c = cmds.polySphere(r=r)
    cmds.move(0,10,0)
    cmds.setAttr(c[0]+".visibility",0)
    cmds.setKeyframe(time=45)
    cmds.setAttr(c[0]+".visibility",1)
    cmds.rotate(145,0,0)
    cmds.scale(1,.8,1)
    cmds.setKeyframe(time=40)
    cmds.move(2,6,0)
    cmds.rotate(75,0,0)
    cmds.setKeyframe(time=30)
    cmds.move(0,2,0)
    cmds.rotate(0,0,0)
    cmds.setKeyframe(time=20)
    cmds.move(0,0,0)
    cmds.scale(.2,.2,.2)
    cmds.setKeyframe(time=1)


