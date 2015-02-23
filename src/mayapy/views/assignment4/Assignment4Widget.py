__author__ = 'Sam Vitello'


import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget
from mayapy.views.assignment4.shaders import *



class Assignment4Widget(PyGlassWidget):
    """A class for Assignment 1"""

    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment1Widget."""
        super(Assignment4Widget, self).__init__(parent, **kwargs)
        self.materialOptions = ["Green Plastic","Tarnished Wood","Shiny Gold","Scratched Metal"]
        self.objectOptions = ["Pyramid","Sphere","Ring","Snowman"]
        self.executeBtn.clicked.connect(self._handleExecute)
        self.homeBtn.clicked.connect(self._handleReturnHome)
        for i in range(0,len(self.materialOptions)):
            self.materialSel.insertItem(i,self.materialOptions[i])
        for j in range(0,len(self.objectOptions)):
            self.objectSel.insertItem(j,self.objectOptions[j])
        self.obj = None
        self.mat = None


    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')

    def _handleExecute(self):
        if self.objectSel.currentIndex() == 0:
            self.obj = createPyramid()
        elif self.objectSel.currentIndex() == 1:
            self.obj = createSphere()
        elif self.objectSel.currentIndex() == 2:
            self.obj = createRing()
        elif self.objectSel.currentIndex() == 3:
            self.obj = createSnowman()

        if self.materialSel.currentIndex() == 0:
            self.mat = createPlasticShader()
        elif self.materialSel.currentIndex() == 1:
            self.mat = createWoodShader()
        elif self.materialSel.currentIndex() == 2:
            self.mat = createGold()
        elif self.materialSel.currentIndex() == 3:
            self.mat = createDirtyMetal()

        assignMaterial(self.obj, self.mat)


def createSnowman():
    bottom = cmds.polySphere(r=3)
    middle = cmds.polySphere(r=2)
    top = cmds.polySphere(r=1.5)

    cmds.select(middle)
    cmds.move(0,4,0)

    cmds.select(top)
    cmds.move(0,7,0)

    snowman = cmds.polyUnite(bottom,middle,top, n='snowman')

    return snowman

def createPyramid():
    pyr = cmds.polyPyramid()
    return pyr

def createSphere():
    sphere = cmds.polySphere(r=2)
    return sphere

def createRing():
    ring = cmds.polyPipe(r=2)
    return ring



