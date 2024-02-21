import pygame, sys, boardComponents
# Initialising the pygame window
pygame.init()
clock = pygame.time.Clock()

screenWidth, screenHeight = 1000, 1000
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('Chess')


board = boardComponents.Board()

def InstallBoardInLoop():
    # Puts both coloured tile set together on the screen
    InstallWhiteTiles()
    InstallBlackTiles()


def InstallBlackTiles():
    # Initialising the space of a tile on the x and y axis
    aTileSpace = 100
    
    # Declaring the inital start position, counter and if the tile needs indenting
    startingPositionX, startingPositionY = 100,100
    blackCounter = 0
    tileNeedsIndenting = True
    
    # This nested loop slots the tiles in the correct spaces on the chess board 
    for i in range(8):
        for j in range(8):
            if not(j % 2 == 0):
                if blackCounter % 4 == 0 and not blackCounter == 0:
                    if tileNeedsIndenting:
                        startingPositionX = 200
                    else:
                        startingPositionX = 100
                    startingPositionY += 100
                    screen.blit(board.blackTiles[board.boardLogicArray[i][j]], (startingPositionX, startingPositionY))
                    blackCounter += 1
                    tileNeedsIndenting = False
                else:
                    if tileNeedsIndenting:
                        startingPositionX = 200
                        screen.blit(board.blackTiles[board.boardLogicArray[i][j]], (startingPositionX, startingPositionY))
                        blackCounter += 1
                        tileNeedsIndenting = False
                        
                    else:
                        screen.blit(board.blackTiles[board.boardLogicArray[i][j]], (startingPositionX+(aTileSpace*2), startingPositionY))
                        blackCounter += 1
                        if blackCounter % 8 == 0:
                            tileNeedsIndenting = True
                        
                        startingPositionX += (aTileSpace*2)

def InstallWhiteTiles():
    # Initialising the space of a tile on the x and y axis
    aTileSpace = 100
    
    # Declaring the inital start position, counter and if the tile needs indenting
    startingPositionY = 100
    startingPositionX = 100
    tileNeedsIndenting = False
    whiteCounter = 4
    
    # This nested loop slots the tiles in the correct spaces on the chess board 
    for i in range(8):
        for j in range(8):
            if j % 2 == 0 or j == 0:
                if whiteCounter % 4 == 0 and not whiteCounter == 4:
                    if tileNeedsIndenting:
                        startingPositionX = 200
                    else:
                        startingPositionX = 100
                    startingPositionY += 100
                    screen.blit(board.whiteTiles[board.boardLogicArray[i][j]], (startingPositionX,startingPositionY))
                    whiteCounter += 1
                    tileNeedsIndenting = False
                else:
                    if whiteCounter == 4:
                        screen.blit(board.whiteTiles[board.boardLogicArray[i][j]], (startingPositionX,startingPositionY))
                        whiteCounter += 1
                    else:
                        screen.blit(board.whiteTiles[board.boardLogicArray[i][j]], (startingPositionX+(aTileSpace*2), startingPositionY))
                        whiteCounter += 1
                        if whiteCounter % 8 == 0:
                            tileNeedsIndenting = True
                        startingPositionX += (aTileSpace*2)       

# Pygame game loop
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((255,255,255))
    InstallBoardInLoop()
    
    pygame.display.flip()
    clock.tick(60)
    
            