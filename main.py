import pygame
import time
from sys import exit

pygame.init()

# Display information
display_w = 800
display_h = 400
window = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption("Beginner Physics Engine")

# Clock
clock = pygame.time.Clock()

# Objects
rect_1 = pygame.Rect(300,display_h-50,50,50)

class MainEvent():
    
    def __init__(self):
        
        self.gravity_var = 0.01
        self.t0 = time.time()


    def Main(self):
        
        moving = False
        
        while True:

            window.fill(pygame.Color(0,0,0,0))
            pygame.draw.rect(window, 'Red', rect_1)
            
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
                
            if rect_1.y < display_h-50 and moving == False: # gravity occuring until object hits ground
                    
                t1 = time.time()
        
                if t1 - self.t0 >= 0.01: # if time elapsed > 10 milisecond
                    self.gravity_var += 0.0981 # object falls down at 0.0981 meters/10 milisecond
                    # pygame does not accept y coordinate change less than 0.01, but ∆y is kept at 0.0981
                    rect_1.move_ip(0, self.gravity_var)
                    self.t0 = t1
                
            elif pygame.MOUSEMOTION and moving: # every time object is moved by mouse, gravity restarts
                self.gravity_var = 0.01
        
            pygame.display.update()
            clock.tick(60)
            

MainEvent().Main()