import pygame
from enemy import *
from player import *
from projectile import *
#PLEase import_programs == (pygame) 🙏🙏😌

#startup - - - -
pygame.init()
pygame.display.set_caption("Bootleg Space Invaders")  # sets the window title
screen = pygame.display.set_mode((0, 0), 1500,1000)
screen.fill((0,0,0))
#for a game like this i dont think we should do fullscreen, it would just be easier to do a set size
gameover = False #variable to run our game loop
enemyList = []
projectileList = []

for i in range(0,5,1):
    for a in range (0,19,1):
        pass
        #add to list enemy(pos = a * 10, use if elif statements to decide type)
for i in range(0,4,1):
    pass
    #add barier to list


while not gameover: #GAME LOOP############################################################
    clock.tick(60)      #FPS  why they do that???? hiw is it vertical
                        #wdym? i just put the 60 in ⁐s
#render 

for enemy in enemyList:
    enemy.draw()
for projectile in projectileList:
    projectile.draw()