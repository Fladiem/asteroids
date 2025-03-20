# this allows us to use code from
# the open-source pygame library throughout this file
# 
import pygame
from constants import *
from circleshape import CircleShape
from player import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get(): #Allows the close button [X] on the window to close the window
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))  #Fills screen with the color black
        player1.draw(screen)  #draw player triangle
        pygame.display.flip()  #Refreshes the screen
        dt = clock.tick(60) / 1000 #Sets framerate to 60 and sets dt to number of seconds since clock.tick() was called.
        """clock.tick(60)    #Sets framerate to 60
        dt = clock.get_time() / 1000  #sets dt to the number of seconds since clock.tick() was called"""
        

    
if __name__ == "__main__":   #This ensures the main() function is only called when 
    main()                    #this file is run directly. main() will not be imported
                                #as a module.