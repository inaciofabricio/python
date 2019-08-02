import pygame, sys
from classes import *
from process import process
SCREENWIDTH,SCREENHEIGHT = 640,360
pygame.init()
WIDTH,HEIGHT = 640,360
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
clock = pygame.time.Clock()
FPS = 24

total_frames = 0

background = pygame.image.load("images/forest.jpg")
bug = Bug(0,SCREENHEIGHT - 40,40,40,"images/bug.png")

while True:
    process(bug,FPS,total_frames)

    #LOGIC

    bug.motion(SCREENWIDTH,SCREENHEIGHT)
    Fly.movement(SCREENWIDTH)
    BugProjectile.movement()
    total_frames += 1
    #LOGIC
    #DRAW

    screen.blit(background,(0,0))
    BaseClass.allsprites.draw(screen)

    pygame.display.flip()

    #DRAW

    clock.tick(FPS)
