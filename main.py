import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

rect_1 = pygame.Rect(300,350,50,50)
moving = False

gravity = 0

while True:
        
    screen.fill(pygame.Color(0,0,0,0))
    pygame.draw.rect(screen, 'Red', rect_1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and rect_1.collidepoint(event.pos):
            moving = True
        elif event.type == pygame.MOUSEBUTTONUP:
            moving = False
        elif event.type == pygame.MOUSEMOTION and moving: # why elif used instead of if, what's the different?   
            rect_1.move_ip(event.rel)
            
    if rect_1.y < 350 and moving == False: # gravity occuring until object hits ground
        rect_1.move_ip(0, 1)
        
    pygame.display.update()
    clock.tick(60)