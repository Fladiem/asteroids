import pygame
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED
from constants import SHOT_RADIUS
from constants import PLAYER_SHOOT_COOLDOWN
from circleshape import CircleShape
from shot import Shot
#def __init__(self, x, y, radius): This is CircleShape's constructor


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 1   #inconsistent behavior, multiple bullets at first press of SPACE
        
    
    def triangle(self):  # provided by BootDev, needed to draw a triangle
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(dt - (dt * 2))
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt)

        if self.timer > 0:  #Move to def shoot()? Seems slightly more efficient.
            pass
        elif keys[pygame.K_SPACE]:
            self.shoot(self.position, self.position, SHOT_RADIUS)

    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, positionx, positiony, radius):
        #if self.timer > 0:    #Behavior consistently inconsistent, can be here or in def update()?
            #return
        new_shot = Shot(positionx, positiony, radius)  #does not seem to actually use positiony, but argument is required for Shot's super().__init__
        new_shot.velocity = (pygame.Vector2(0, 1).rotate(self.rotation)) * PLAYER_SHOOT_SPEED
        self.timer += PLAYER_SHOOT_COOLDOWN