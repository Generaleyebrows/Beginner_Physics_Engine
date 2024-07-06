import pygame
import time
from sys import exit
import math

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
    
    def trajectory(self, x, g, v, theta): # gravity, velocity, angle
        return x*math.tan(theta) - ((g*math.pow(x, 2))/(2*math.pow(v, 2))*(math.pow(math.cos(theta), 2)))
    
    def Main(self):
        
        traj_x = 0 # trajectory coordinates for rect_1.move_ip()
        traj_y = 0
        velocity = 0.01
        angle = 0
        
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
                    
                    self.gravity_var = -0.0981
                    
                    dx = event.rel[0] # created for initial velocity
                    mx, my = event.pos # coordinates for arctan to create angle
                    real_my = display_h - my # my is opposite is movement to a normal graph, so it's reversed
                    
                    print(f"mx = {mx}")
                    print(f"my = {real_my}")
                    print(f"angle = {math.atan2(real_my, mx)}")
                    
            if rect_1.y < display_h-50 and moving == False: # rectangle is let go, trajectory is calculated
                
                velocity = abs(dx)+0.01 # stop it from ever being 0
                    
                angle = math.atan2(real_my, mx)
                                
                t1 = time.time()

                if t1 - self.t0 >= 0.01: # if time elapsed > 10 milisecond
                    traj_x = rect_1.x*0.01
                    self.gravity_var-=9.81*0.01
                    traj_y = self.trajectory(traj_x, self.gravity_var, velocity, angle)
                    rect_1.move_ip(traj_x, traj_y)
                    
                    self.t0 = t1      

            pygame.display.update()
            clock.tick(60)
            

MainEvent().Main()