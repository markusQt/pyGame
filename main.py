import pygame
import time
import random

pygame.init()

display_width = 1200
display_height = 800
black = (0,0,0)
white = (255,255,255)
green = (75,255,3)
red = (255,0,0)
blau = (0,0,128)

shuttle = pygame.image.load('assets/shuttle.png')
shuttle_width = 65
shuttle_heigth = 70

mWindow = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Space Patrol")
clock = pygame.time.Clock()


width = 40
height = 60

def funcObject(posX,posY,objectW,objectH,objectColor):
    pygame.draw.rect(mWindow,objectColor,(posX,posY,objectW,objectH))
    
    

def funcExit():
    pygame.quit()
    quit()

def text_objects (text,font):
    textSurface = font.render(text,True,black)
    return textSurface , textSurface.get_rect()
    

def  message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    textSurface , textRect = text_objects(text,largeText)
    textRect.center = ((display_width/2),(display_height/2))
    mWindow.blit(textSurface,textRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('BOOOOOM!')

def funcShuttle(x,y):
    mWindow.blit(shuttle,(x,y))

def game_loop():
    run = True
    x = (display_width*0.45)
    y = (display_height*0.8)
    
    object_width = 20
    object_height = 60
    object_startx = random.randrange((0 + object_width), (display_width - object_width))
    object_starty = - (10 + object_height)
    object_speed = 7
    vel = 5

    while run :
        object_starty += object_speed
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                funcExit()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
             y -= vel
        if keys[pygame.K_DOWN]:
             y += vel
        if keys[pygame.K_RIGHT]:
             x += vel
        if keys[pygame.K_LEFT]:
             x -= vel
        if keys[pygame.K_ESCAPE]:
            run = False
            funcExit()

        mWindow.fill(blau)

        funcObject(object_startx,object_starty,20,50,green)

        if x < 0:
            x = 0

        if  x > (display_width - shuttle_width):
            x = display_width - shuttle_width
            
        if y < 0:
            y = 0

        if y > (display_height - shuttle_heigth) :
            y = display_height - shuttle_heigth           
        
        funcShuttle(x,y)

        
        if object_starty > display_height + 5:
              object_startx = random.randrange((0 + object_width), (display_width - object_width))
              object_starty = - (10 + object_height)    

        if y <  (object_starty + object_height ) and  object_starty < (y + shuttle_heigth) and (x +shuttle_width) > object_startx and x < (object_startx + object_width):
            crash()
        
        pygame.display.update()
        clock.tick(100)

game_loop()        
pygame.quit()
quit()
