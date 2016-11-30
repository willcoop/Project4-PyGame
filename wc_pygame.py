import os, sys
import pygame
from pygame import *
from pygame.sprite import *
from pygame.locals import * 

class main:

    def __init__(self, width=500, height=480):
        pygame.init() #initialize Pygame

        #setting window size
        self.width = width
        self.height = height

        #creating screen
        self.screen = pygame.display.set_mode((self.width, self.height))

    def MainLoop(self):
    	"""Main loop of game"""
    	while 1:
    		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
    				sys.exit()


    

class Snake(pygame.sprite.Sprite):
    "This is our snake that will move around the screen"

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('ship.png')
        self.pellets = 0