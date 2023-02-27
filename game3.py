import pygame
import math as m
import numpy as np
import random as r
pygame.init()

def create_sprite(self):
    scaling_f = 2
    h_width = 4*scaling_f
    b_width = 10*scaling_f
    b_length = b_width+5*scaling_f
    pygame.draw.circle(self,(255,0,0),(x-4*scaling_f,y+20*scaling_f),h_width)
    pygame.draw.rect(self,(255,0,0),(x-9*scaling_f,y+24*scaling_f,b_width,b_length))
def bottom_top(self):
    scaling_f = 2
    block_length = 5*scaling_f
    pygame.draw.rect(self,(255,0,0),(0,0,500,50))
    pygame.draw.rect(self,(255,0,0),(0,450,500,50))
def row1(self,n,i):
    #row_length = r.randint(10,50)
    pygame.draw.rect(self,(255,0,0),(0,i,n,25))
    pygame.draw.rect(self,(0,0,255),(n,i,500-n,25))
def row2(self,n,j):
    pygame.draw.rect(self,(255,0,0),(0,j,n,25))
    t = 0 # length of blue block, n is the starting position
    if (j > 300 and j < 350):
        t = 500-t
    else:
        t = n+25
    pygame.draw.rect(self,(0,0,255),(n,j,t,25))   
    pygame.draw.rect(self,(255,0,0),(t,j,500-t,25))
  
def create_3dM(size):
    return np.zeros((size,size,size)) 

def maze(self):
    bottom_top(self)
    create_3dM(500)
    #row1(self,100,275)
    #row1(self,100,300)
    for i in range(250,400):
        #row2(self,10,i)
        if(i > 300):
            row2(self,10,i) #win, starting column, row
        else:
            row2(self,10,i)

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("MazeGame")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True
win.fill((0,0,0))

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.key.get_focused()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    win.fill((0,0,0))
    
    #test_ellipse()

    
    #pygame.draw.rect(win2, (255,0,0),(x,y,width,height))
    #pygame.draw.ellipse(win2,(255,0,0),(x+100,y-100,width,height))
    #pygame.draw.circle(win2,(255,0,0),(x-20,y+100),20)
    #pygame.draw.rect(win2,(255,0,0),(x-45,y+120,50,50))
    
    maze(win)
    create_sprite(win)
    #pass window object to function to create sprite
    pygame.display.update()

pygame.quit
