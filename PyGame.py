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
	pygame.key.set_repeat(500,30)
	
	self.background = pygame.Surface(self.screen.get_size())
	self.background = self.background.convert()
	self.background.fill((0,0,0))
	while 1:
	    for event in pygame.event.get():
		if event.type == pygame.QUIT:
		    sys.exit()
		elif event.type == KEYDOWN:
		    if ((event.key == K_RIGHT)
		    or (event.key == K_LEFT)
  		    or (event.key == K_UP)
		    or (event.key == K_DOWN)):
			self.snake.move(event.key)

	    lstCols = pygame.sprite.spritecollide(self.snake,self.pellet_sprites,True)
	    self.snake.pellets = self.snake.pellets + len(lstCols)
	    self.screen.blit(self.background,(0,0))
	    if pygame.font:
		font = pygame.font.Font(None,36)
		text = font.render("Pellets %s" % self.snake.pellets,1,(255,0,0))
		textpos = text.get_rect(centerx=self.background.get_width()/2)
		self.screen.blit(text,textpos)
		
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
	self.x_dist = 5
	self.y_dist = 5
    def move(self,key):
	xMove=0
	yMove=0
	if(key ==K_RIGHT):	
	    xMove = self.x_dist
	elif(key == K_LEFT):
	    xMove = -self.x_dist
	elif (key==K_UP):
	    yMove = -self.y_dist
	elif(key == K_DOWN):
	    yMove = self.y_dist
	self.rect.move_ip(xMove,yMove)	
class Pellet(pygame.sprite.Sprite):

    def __init__(self,rect=None):
	pygame.sprite.Sprite.__init__(self)
	self.image,self.rect = load_image('pellet.png',-1)
	if rect !=None:
	    self.rect = rect

if __name__ == "__main__":
    MainWindow = PyManMain()
    MainWindow.MainLoop()
