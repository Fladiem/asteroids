import pygame
from constants import SHOT_RADIUS
#from constants import PLAYER_SHOOT_SPEED  needed by player.py, not shot.py
from circleshape import CircleShape

class Shot(CircleShape):
    #Copied code from Asteroid class, needs editing
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) 
#^^^^^ This __init__ is what appears to be causing shot() to need two positional arguments

    """def __init__(self, x, y, ):
        super().__init__(x, y, SHOT_RADIUS)"""
    
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)