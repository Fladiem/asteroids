# this allows us to use code from
# the open-source pygame library throughout this file
# 
import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get(): #Allows the close button [X] on the window to close the window
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))  #Fills screen with the color black
        pygame.display.flip()  #Refreshes the screen

    
if __name__ == "__main__":   #This ensure the main() function is only called when 
    main()                    #this file is run directly. main() will not be imported
                                #as a module.