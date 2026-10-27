import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()  #Ensures asteroid is always deleted when appropriate
        if self.radius <= ASTEROID_MIN_RADIUS:  #Specifies that small asteroids simply self.kill()
            return
        else:  #else statement not needed here based on solution notes, possible negatives to this approach?

            new_radius = self.radius - ASTEROID_MIN_RADIUS #Sets split asteroids to be one size smaller than the original
            random_angle = random.uniform(20, 50) #provides a randomized angle for rotate()
            vector = self.velocity.rotate(random_angle)  #creates a new vector for use in new asteroid's .velocity
            negative_vector = self.velocity.rotate(-random_angle) #creates new vector that mirrors the first

            split_asteroid1 = Asteroid(self.position, self.position, new_radius)  #These are the new asteroid objects created upon split
            split_asteroid2 = Asteroid(self.position, self.position, new_radius)  #Still needs second seemingly unused self.position to avoid error?
            #solution_asteroid = Asteroid(self.posiiton.x, self.position.y, new_radius)
            split_asteroid1.velocity = vector * 1.2
            split_asteroid2.velocity = negative_vector * 1.2





        
   