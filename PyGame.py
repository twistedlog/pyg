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

	    self.pellet_sprites.draw(self.screen)
	    self.snake_sprites.draw(self.screen)
	    pygame.display.flip()

    def LoadSprites(self):
	""" Load the sprite we need"""
	self.snake = Snake()
	self.snake_sprites = pygame.sprite.RenderPlain((self.snake))
	"""figure out how many pellets we can display"""
	nNumHorizontal = int(self.width/64)
	nNumVertical = int(self.height/64)
	"""Create the pellet group"""
	self.pellet_sprites = pygame.sprite.Group()
	"""Create all the palletes and add them to the pallet_sprites group"""
	for x in range(nNumHorizontal):
	    for y in range(nNumVertical):
	        self.pellet_sprites.add(Pellet(pygame.Rect(x*64,y*64,64,64)))

class Snake(pygame.sprite.Sprite):
    """This is out snake that will be moved around the screen"""
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
	self.image,self.rect=load_image('snake.png',-1)
	self.pellets =0

class Pellet(pygame.sprite.Sprite):

    def __init__(self,rect=None):
	pygame.sprite.Sprite.__init__(self)
	self.image,self.rect = load_image('pellet.png',-1)
	if rect !=None:
	    self.rect = rect

if __name__ == "__main__":
    MainWindow = PyManMain()
    MainWindow.MainLoop()
