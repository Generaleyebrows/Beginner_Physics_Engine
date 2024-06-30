import pygame
from sys import exit
import time

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

rect_1 = pygame.Rect(300,350,50,50)
moving = False

gravity = 0.01

start = time.time()

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
        elif event.type == pygame.MOUSEMOTION and moving: # why elif used instead of if, what's the difference?   
            rect_1.move_ip(event.rel)
            
    if rect_1.y < 350 and moving == False: # gravity occuring until object hits ground
        
        t = time.time()
        
        if t - start >= 0.01: # if time elapsed > 10 milisecond
            gravity += 0.0981 # object falls down at 0.0981 meters/10 milisecond
            # pygame does not accept y coordinate change less than 0.01, but ∆y is kept at 0.0981
            rect_1.move_ip(0, gravity)
            start = t
            
    elif pygame.MOUSEMOTION and moving:
        gravity = 0.01
        
    pygame.display.update()
    clock.tick(60)