import pygame
import time

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Test Window")
clock = pygame.time.Clock();

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    print(event)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
