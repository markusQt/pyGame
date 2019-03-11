import pygame
import time

pygame.init()

mWindow = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()
x = 50
y = 50

width = 40
height = 60

vel = 5
run = True
while run :
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
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

    mWindow.fill((0,0,0))                                        
    pygame.draw.rect(mWindow,(255,0,0),(x,y,width,height))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit
