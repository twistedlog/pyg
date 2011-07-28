import os , sys
import pygame
from pygame.locals import *

if not pygame.font: print 'warning fonts disabled'
if not pygame.mixer: print 'warning, sounds disabled'

class PyManMain:
    """ The Main PyMan Class - This class handels the main
     initializtion and creating of the game."""
    def __init__(self,width=640,height=480):
	"""Initialize"""
	"""Initialize Pygame"""
	pygame.init()
	"""Set the window size"""
	self.width=width
	self.height=height
	"""Create the screen"""
	self.screen = pygame.display.set_mode((self.width,self.height))

    def MainLoop(self):
	"""This is the Main Loop of the game"""
	while 1:
	    for event in pygame.event.get():
		if event.type == pygame.QUIT:
		    sys.exit()

if __name__ == "__main__":
    MainWindow = PyManMain()
    MainWindow.MainLoop()
