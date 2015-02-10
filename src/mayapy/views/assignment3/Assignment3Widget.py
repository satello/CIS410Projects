__author__ = 'Sam'


import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget
from mayapy.views.assignment3.bubble import *
from mayapy.views.assignment3.bubbles import *


class Assignment3Widget(PyGlassWidget):
    """A class for Assignment 1"""

    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment1Widget."""
        super(Assignment3Widget, self).__init__(parent, **kwargs)
        self.bubbleBtn.clicked.connect(self._handleBubbleButton)
        self.bubblesBtn.clicked.connect(self._handleBubblesButton)
        self.homeBtn.clicked.connect(self._handleReturnHome)

    def _handleBubbleButton(self):
        createBubble()

    def _handleBubblesButton(self):
        time = self.animationLength.value()
        createBubbles(time)

    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')