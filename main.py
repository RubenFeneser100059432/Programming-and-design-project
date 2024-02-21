import pygame, sys, boardComponents
# Initialising the pygame window
pygame.init()
clock = pygame.time.Clock()

screenWidth, screenHeight = 1000, 1000
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('Chess')

testTile = boardComponents.Tiles((0,0,0), ('a',1))


# Pygame game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((255,255,255))
    screen.blit(testTile.surface, (0,400))
    pygame.display.flip()
    clock.tick(60)
    
            