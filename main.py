import pygame
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
                elif event.type == pygame.MOUSEMOTION and moving: #every time object is moved by mouse, gravity restarts
                    
                    rect_1.move_ip(event.rel)
                    
                    dx, dy = event.rel # change in mouse movement for one frame
                    
            if rect_1.y < display_h-50 and moving == False: # rectangle is let go, trajectory is calculated
                
                gravity = 9.81
                velocity_vec_x = dx
                velocity_vec_y = dy/60
                
                velocity_vec_x += velocity_vec_x
                velocity_vec_y += gravity
                
                rect_1.move_ip(velocity_vec_x, velocity_vec_y)

            pygame.display.update()
            clock.tick(60)
       
            
MainEvent().Main()