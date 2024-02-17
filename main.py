import pygame, sys
from boardComponents import Tiles, Board
# Initialising the pygame window
pygame.init()
clock = pygame.time.Clock()

screenWidth, screenHeight = 1000, 1000
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('Chess')




# Pygame game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.flip()
    clock.tick(60)
    
            