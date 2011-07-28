from helpers import *
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
	"""Load All of our sprites"""
	self.LoadSprites()
	while 1:
	    for event in pygame.event.get():
		if event.type == pygame.QUIT:
		    sys.exit()

	    self.snake_sprites.draw(self.screen)
	    pygame.display.flip()

    def LoadSprites(self):
	""" Load the sprite we need"""
	self.snake = Snake()
	self.snake_sprites = pygame.sprite.RenderPlain((self.snake))
class Snake(pygame.sprite.Sprite):
    """This is out snake that will be moved around the screen"""
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
	self.image,self.rect=load_image('snake.png',-1)
	self.pellets =0

if __name__ == "__main__":
    MainWindow = PyManMain()
    MainWindow.MainLoop()
