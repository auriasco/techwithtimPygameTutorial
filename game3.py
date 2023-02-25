import pygame
import math as m
import pygame.draw as d
pygame.init()

def create_sprite(self):
    pygame.draw.circle(self,(255,0,0),(x-20,y+100),20)
    pygame.draw.rect(self,(255,0,0),(x-45,y+120,50,50))

def test_ellipse(self):
    d.surf = pygame.Surface((320, 200))
    win = d.surf
    x = 50
    y = 50
    width = 40
    height = 60
    vel = 5

    run = True
    while run:
        pygame.time.delay(100)
        pygame.Surface((320,200))
        pygame.draw.ellipse(win, (255, 0, 0), (10, 10, 25, 20))
        pygame.draw.rect(win, (255,0,0),(x,y,width,height))
        #pygame.draw.circle(win,(255,0,0),(30,30,20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #win.fill((0,0,0))
    
    pygame.display.update()

#win = pygame.display.set_mode((500,500))
#test_ellipse(win,d)
#pygame.quit
win2 = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True
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
    win2.fill((0,0,0))
    
    #test_ellipse()

    
    #pygame.draw.rect(win2, (255,0,0),(x,y,width,height))
    #pygame.draw.ellipse(win2,(255,0,0),(x+100,y-100,width,height))
    #pygame.draw.circle(win2,(255,0,0),(x-20,y+100),20)
    #pygame.draw.rect(win2,(255,0,0),(x-45,y+120,50,50))
    create_sprite(win2)
    #pass window object to function to create sprite
    pygame.display.update()
pygame.quit
