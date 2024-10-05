import pygame
import sys
from pygame import Vector2 as vtr
from pygame import time 
import math


# initilising pygame
pygame.init()

# defining screen size
screen_height = 500
screen_width = 1200
screen = pygame.display.set_mode((screen_width, screen_height))

# objects properties

position_body = vtr(248,0)
position_secbody = vtr(600,100)
clock = pygame.time.Clock()
jumping = True

side = 20

movement = True

# function to draw body 1
def body():
    Colour = (255,0,0)
    body = pygame.draw.circle(screen,Colour,position_body,(side))
    return body  

# function to draw body 2 
def sec_body():
    sec_body = pygame.draw.circle(screen,(0,255,0),position_secbody,side)
    return sec_body
    
# funciton calculate the distance b\w objects
def distancebtw():
    distance = math.sqrt((((position_body.x) - (position_secbody.x))**2) + (((position_body.y) - (position_secbody.y))**2) )
    return distance

# funtion for decting collision
def collision():
    global movement
    if distancebtw() <= 40:
        if position_body.x > position_secbody.x  and distancebtw() <= 40 :
            position_body.x += 1
            position_secbody.x -= 1
        elif position_body.x < position_secbody.x and distancebtw() <= 40:
            position_body.x -= 1
            position_secbody.x += 1
        movement = False
    return movement , position_body.x , position_secbody.x

# initlilaizing some importnt variables 
velocity_y1,velocity_y2  = 0,0
acceleration_y = 0.5

#main loop
while True:
    screen.fill((0, 0, 0))  
    
    body()
    sec_body()

    keys = pygame.key.get_pressed() 

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    collision()
# freefall
    # for body 1    
    velocity_y1 += acceleration_y 
    position_body.y += velocity_y1
    # for body 2
    velocity_y2 += acceleration_y
    position_secbody.y += velocity_y2
        
    # bounce back 
    if position_body.y + side > screen_height  :
        position_body.y = screen_height - side
        velocity_y1 = -velocity_y1/1.5
    if  position_secbody.y + side > screen_height:
        position_secbody.y = screen_height - side
        velocity_y2 = -velocity_y2/1.5

    # motion in left or right 
    if keys[pygame.K_LEFT] and movement :
        position_body.x -= 10
        
    elif keys[pygame.K_RIGHT] and movement :
        position_body.x += 10
        
    # for jump 
    if keys[pygame.K_SPACE]  and position_body.y >= screen_height - side:
        while jumping:
            jumping = False
            velocity_y1 = -10
            break
        jumping = True

    movement = True

    pygame.display.update()
    clock.tick(60)