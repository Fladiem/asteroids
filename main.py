# this allows us to use code from
# the open-source pygame library throughout this file
# 
import pygame
from constants import *
from circleshape import CircleShape
from player import *
from asteroid import *
from asteroid_field import AsteroidField

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    

    updatable = pygame.sprite.Group()    #Creating groups
    drawable = pygame.sprite.Group()    #my_group = pygame.sprite.Group()
    asteroids_g = pygame.sprite.Group() # group for Asteroids(CircleShape) class

    Player.containers = (updatable, drawable)   #Player.containers = group a, group b   
                                                #Adds all instances of Player class to Groups in ()
    Asteroid.containers = (asteroids_g, updatable, drawable)

    AsteroidField.containers = (updatable)
    
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield1 = AsteroidField()
    
    while True:
        for event in pygame.event.get(): #Allows the close button [X] on the window to close the window
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000 #Sets framerate to 60 and sets dt to number of seconds since clock.tick() was called.
        screen.fill((0,0,0))  #Fills screen with the color black
        updatable.update(dt)  #calls update() method for updatable group
        for ast in asteroids_g:
            ast.collision(player1)
            if ast.collision(player1) == True:
                print ("Game over!")
                raise SystemExit
        for obj in drawable:
            obj.draw(screen)
        #player1.draw(screen)  #draw player triangle, replaced by obj.draw for optimization
        pygame.display.flip()  #Refreshes the screen
        
        """clock.tick(60)    #Sets framerate to 60
        dt = clock.get_time() / 1000  #sets dt to the number of seconds since clock.tick() was called"""
        

    
if __name__ == "__main__":   #This ensures the main() function is only called when 
    main()                    #this file is run directly. main() will not be imported
                                #as a module.