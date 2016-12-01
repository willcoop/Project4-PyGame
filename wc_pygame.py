import os, sys
import pygame
from pygame import *
from pygame.sprite import *
from pygame.locals import * 

class main:

    def __init__(self, width=500, height=480):
        pygame.init() #initialize Pygame
        pygame.display.set_caption('Coops Game')


        #setting window size
        self.width = width
        self.height = height

        #creating screen
        self.screen = pygame.display.set_mode((self.width, self.height))
        

class Snake:
#create Snake
    def __init__(self, surface):
        self.surface = surface
        self.x = surface.get_width() / 2
        self.y = surface.get_width() / 2
        self.length = pieceSize
        self.grow_to = pieceSize*2
        self.xVel = 0
        self.yVel = -pieceSize
        self.body = []
        self.head = None
        self.crashed = False
        self.color = WHITE

    def keys(self):

        key = pygame.key.get_pressed()
        dist = 1
        if key[pygame.K_DOWN]:
            self.y += dist
        if key[pygame.K_UP]:
            self.y -= dist
        if key[pygame.K_RIGHT]:
            self.x += dist
        if key[pygame.K_LEFT]:
            self.y -= dist

    def draw(self, surface):
        surface.blit(self.image,(self.x,self.y))






