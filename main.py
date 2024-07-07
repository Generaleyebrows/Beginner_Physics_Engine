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
        velocity_vec_y = 0
        gravity = 1

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
                    velocity_vec_x = dx * 2 # Set initial Velocity
                    velocity_vec_y = dy * 2
                elif event.type == pygame.MOUSEMOTION and moving: # Every time object is moved by mouse, gravity restarts
                    
                    rect_1.move_ip(event.rel)
                    
                    dx, dy = event.rel # Change in mouse movement for one frame
                    
            if rect_1.y < display_h-50 and moving == False: # rectangle is let go, trajectory is calculated
                
                velocity_vec_y += gravity # Accelerate
                
                rect_1.move_ip(velocity_vec_x, velocity_vec_y)

            # Bottom Border Collision
            if rect_1.y > display_h-50:
                rect_1.y = display_h-50

            # Top Border Collision
            if rect_1.y < 0:
                rect_1.y = 1
                velocity_vec_y = 1
            
            # Left Border Collision
            if rect_1.x < 0:
                rect_1.x = 0
                velocity_vec_x = -(velocity_vec_x * 0.5)

            # Right Border Collision
            if rect_1.x > display_w:
                rect_1.x = display_w - 50
                velocity_vec_x = -(velocity_vec_x * 0.5)
            
            
            pygame.display.update()
            clock.tick(60)
       
            
MainEvent().Main()