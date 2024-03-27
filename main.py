import pygame, sys, boardComponents, chessPieces

pygame.init()
clock =  pygame.time.Clock()
screenWidth, screenHeight = 1000, 1000
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('2-Player Chess')


global whichPlayersTurn

whichPlayersTurn = 'white'
row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
capturedBlackPieces = []
capturedWhitePieces = []

# Setting up board

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

# Pawn methods

def CreateWhitePawns():
    global whitePawn1, whitePawn2, whitePawn3, whitePawn4, whitePawn5, whitePawn6, whitePawn7, whitePawn8
    
    # Creates 8 pawns objects
    # Initialised with their starting position and their position on the logic array
    whitePawn1 = chessPieces.Pawn("white", ("a", 2), 6, 0, True)
    whitePawn2 = chessPieces.Pawn("white", ("b", 2), 6, 1, True)
    whitePawn3 = chessPieces.Pawn("white", ("c", 2), 6, 2, True)
    whitePawn4 = chessPieces.Pawn("white", ("d", 2), 6, 3, True)
    whitePawn5 = chessPieces.Pawn("white", ("e", 2), 6, 4, True)
    whitePawn6 = chessPieces.Pawn("white", ("f", 2), 6, 5, True)
    whitePawn7 = chessPieces.Pawn("white", ("g", 2), 6, 6, True)
    whitePawn8 = chessPieces.Pawn("white", ("h", 2), 6, 7, True)
    
def CreateBlackPawns():
  
 
   global blackPawn1, blackPawn2, blackPawn3, blackPawn4, blackPawn5, blackPawn6, blackPawn7, blackPawn8
   
   # Creates 8 pawns using the pawn class,
   # initialised with their starting position and their position on the logic array
   blackPawn1 = chessPieces.Pawn("black", ("a", 7), 1, 0, True)
   blackPawn2 = chessPieces.Pawn("black", ("b", 7), 1, 1, True)
   blackPawn3 = chessPieces.Pawn("black", ("c", 7), 1, 2, True)
   blackPawn4 = chessPieces.Pawn("black", ("d", 7), 1, 3, True)
   blackPawn5 = chessPieces.Pawn("black", ("e", 7), 1, 4, True)
   blackPawn6 = chessPieces.Pawn("black", ("f", 7), 1, 5, True)
   blackPawn7 = chessPieces.Pawn("black", ("g", 7), 1, 6, True)
   blackPawn8 = chessPieces.Pawn("black", ("h", 7), 1, 7, True)
   
def PutAllPawnsOnTheBoard():
    # All pawn rectangles are tied to their surface and then put on the screen
    screen.blit(blackPawn1.surface, blackPawn1.rect)
    screen.blit(blackPawn2.surface, blackPawn2.rect)
    screen.blit(blackPawn3.surface, blackPawn3.rect)
    screen.blit(blackPawn4.surface, blackPawn4.rect)
    screen.blit(blackPawn5.surface, blackPawn5.rect)
    screen.blit(blackPawn6.surface, blackPawn6.rect)
    screen.blit(blackPawn7.surface, blackPawn7.rect)
    screen.blit(blackPawn8.surface, blackPawn8.rect)
    
    
    screen.blit(whitePawn1.surface, whitePawn1.rect)
    screen.blit(whitePawn2.surface, whitePawn2.rect)
    screen.blit(whitePawn3.surface, whitePawn3.rect)
    screen.blit(whitePawn4.surface, whitePawn4.rect)
    screen.blit(whitePawn5.surface, whitePawn5.rect)
    screen.blit(whitePawn6.surface, whitePawn6.rect)
    screen.blit(whitePawn7.surface, whitePawn7.rect)
    screen.blit(whitePawn8.surface, whitePawn8.rect)

def CollidingWithAPawn(turn, whereMouseIs):    
    # Detects if the mouse collideds with a pawn so they can be moved
    if turn == "white":
        if whitePawn1.rect.collidepoint(whereMouseIs) or whitePawn2.rect.collidepoint(whereMouseIs) or whitePawn3.rect.collidepoint(whereMouseIs) or whitePawn4.rect.collidepoint(whereMouseIs) or whitePawn5.rect.collidepoint(whereMouseIs) or whitePawn6.rect.collidepoint(whereMouseIs) or whitePawn7.rect.collidepoint(whereMouseIs) or whitePawn8.rect.collidepoint(whereMouseIs):
            return True
        else:
            return False
    elif turn == "black":
        if blackPawn1.rect.collidepoint(whereMouseIs) or blackPawn2.rect.collidepoint(whereMouseIs) or blackPawn3.rect.collidepoint(whereMouseIs) or blackPawn4.rect.collidepoint(whereMouseIs) or blackPawn5.rect.collidepoint(whereMouseIs) or blackPawn6.rect.collidepoint(whereMouseIs) or blackPawn7.rect.collidepoint(whereMouseIs) or blackPawn8.rect.collidepoint(whereMouseIs):     
            return True
        else:
            return False

def WhichPawnIsCollidedWith(turn, whereMouseIs):
        # Determines which pawn is collided with specifically so the correct pawn can be moved
        
        if turn == "white":
            if whitePawn1.rect.collidepoint(whereMouseIs):
                return 1
            if whitePawn2.rect.collidepoint(whereMouseIs):
                return 2
            if whitePawn3.rect.collidepoint(whereMouseIs):
                return 3
            if whitePawn4.rect.collidepoint(whereMouseIs):
                return 4
            if whitePawn5.rect.collidepoint(whereMouseIs):
                return 5
            if whitePawn6.rect.collidepoint(whereMouseIs):
                return 6
            if whitePawn7.rect.collidepoint(whereMouseIs):
                return 7
            if whitePawn8.rect.collidepoint(whereMouseIs):
                return 8
        elif turn == "black":
            if blackPawn1.rect.collidepoint(whereMouseIs):
                return 1
            if blackPawn2.rect.collidepoint(whereMouseIs):
                return 2
            if blackPawn3.rect.collidepoint(whereMouseIs):
                return 3
            if blackPawn4.rect.collidepoint(whereMouseIs):
                return 4
            if blackPawn5.rect.collidepoint(whereMouseIs):
                return 5
            if blackPawn6.rect.collidepoint(whereMouseIs):
                return 6
            if blackPawn7.rect.collidepoint(whereMouseIs):
                return 7
            if blackPawn8.rect.collidepoint(whereMouseIs):
                return 8

def WhereCanPawnMove(turn, whichPawn):
    # Pawns can at most move two spaces forward or take diagonally one space in two directions so 4 moves are possible
    # The first two moves are linear and the next two are diagonal
    fourMoves = [(0,0), (0,0), (0,0), (0,0)]
    
    if turn == 'white':
        if whichPawn == 1:
            if whitePawn1.onBoard:
                if whitePawn1.firstMove: # If it is the pawns first move they can move two spaces
                    for x in range(1,3):
                        if x < 3:
                            if whitePawn1.indexIOnLogicArray - x >= 0:
                                if rectLogicArray[whitePawn1.indexIOnLogicArray - x][whitePawn1.indexJOnLogicArray] == 0:
                                    fourMoves[x-1] =  AdjustPositionAfterMove(whitePawn1.indexIOnLogicArray - x, whitePawn1.indexJOnLogicArray)
                                elif rectLogicArray[whitePawn1.indexIOnLogicArray - x][whitePawn1.indexJOnLogicArray] != 0:
                                    break
                        # If the pawn is taking diagonally
                        if whitePawn1.indexIOnLogicArray - 1 >= 0 and whitePawn1.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[whitePawn1.indexIOnLogicArray - 1][whitePawn1.indexJOnLogicArray + 1] < 0:
                                fourMoves[2] =  AdjustPositionAfterMove(whitePawn1.indexIOnLogicArray - 1, whitePawn1.indexJOnLogicArray+1)
                        if whitePawn1.indexIOnLogicArray - 1 >= 0 and whitePawn1.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[whitePawn1.indexIOnLogicArray - 1][whitePawn1.indexJOnLogicArray - 1] < 0:
                                fourMoves[3] =  AdjustPositionAfterMove(whitePawn1.indexIOnLogicArray - 1, whitePawn1.indexJOnLogicArray-1)
                    
                    return fourMoves
                    
                else: # Moves after the first move
                    if whitePawn1.indexIOnLogicArray - 1 >= 0:
                        if rectLogicArray[whitePawn1.indexIOnLogicArray - 1][whitePawn1.indexJOnLogicArray] == 0:
                            fourMoves[0] =  AdjustPositionAfterMove(whitePawn1.indexIOnLogicArray - 1, whitePawn1.indexJOnLogicArray)
                    if whitePawn1.indexIOnLogicArray - 1 >= 0 and whitePawn1.indexJOnLogicArray + 1 < 8:
                        if rectLogicArray[whitePawn1.indexIOnLogicArray - 1][whitePawn1.indexJOnLogicArray + 1] < 0:
                            fourMoves[2] =  AdjustPositionAfterMove(whitePawn1.indexIOnLogicArray - 1, whitePawn1.indexJOnLogicArray+1)
                    if whitePawn1.indexIOnLogicArray - 1 >= 0 and whitePawn1.indexJOnLogicArray - 1 >= 0:
                        if rectLogicArray[whitePawn1.indexIOnLogicArray - 1][whitePawn1.indexJOnLogicArray - 1] < 0:
                            fourMoves[3] =  AdjustPositionAfterMove(whitePawn1.indexIOnLogicArray - 1, whitePawn1.indexJOnLogicArray-1)
                    
                    return fourMoves
        
        if whichPawn == 2:
            if whitePawn2.onBoard:
                if whitePawn2.firstMove:
                    for x in range(1,3):
                        if x < 3:
                            if whitePawn2.indexIOnLogicArray - x >= 0:
                                if rectLogicArray[whitePawn2.indexIOnLogicArray - x][whitePawn2.indexJOnLogicArray] == 0:
                                    fourMoves[x-1] =  AdjustPositionAfterMove(whitePawn2.indexIOnLogicArray - x, whitePawn2.indexJOnLogicArray)
                                elif rectLogicArray[whitePawn2.indexIOnLogicArray - x][whitePawn2.indexJOnLogicArray] != 0:
                                    break
                        if whitePawn2.indexIOnLogicArray - 1 >= 0 and whitePawn2.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[whitePawn2.indexIOnLogicArray - 1][whitePawn2.indexJOnLogicArray + 1] < 0:
                                fourMoves[2] =  AdjustPositionAfterMove(whitePawn2.indexIOnLogicArray - 1, whitePawn2.indexJOnLogicArray+1)
                        if whitePawn2.indexIOnLogicArray - 1 >= 0 and whitePawn2.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[whitePawn2.indexIOnLogicArray - 1][whitePawn2.indexJOnLogicArray - 1] < 0:
                                fourMoves[3] =  AdjustPositionAfterMove(whitePawn2.indexIOnLogicArray - 1, whitePawn2.indexJOnLogicArray-1)
                    
                    return fourMoves
                    
                else:
                    if whitePawn2.indexIOnLogicArray - 1 >= 0:
                        if rectLogicArray[whitePawn2.indexIOnLogicArray - 1][whitePawn2.indexJOnLogicArray] == 0:
                            fourMoves[0] =  AdjustPositionAfterMove(whitePawn2.indexIOnLogicArray - 1, whitePawn2.indexJOnLogicArray)
                    if whitePawn2.indexIOnLogicArray - 1 >= 0 and whitePawn2.indexJOnLogicArray + 1 < 8:
                        if rectLogicArray[whitePawn2.indexIOnLogicArray - 1][whitePawn2.indexJOnLogicArray + 1] < 0:
                            fourMoves[2] =  AdjustPositionAfterMove(whitePawn2.indexIOnLogicArray - 1, whitePawn2.indexJOnLogicArray+1)
                    if whitePawn2.indexIOnLogicArray - 1 >= 0 and whitePawn2.indexJOnLogicArray - 1 >= 0:
                        if rectLogicArray[whitePawn2.indexIOnLogicArray - 1][whitePawn2.indexJOnLogicArray - 1] < 0:
                            fourMoves[3] =  AdjustPositionAfterMove(whitePawn2.indexIOnLogicArray - 1, whitePawn2.indexJOnLogicArray-1)
                    
                    return fourMoves
        
        if whichPawn == 3:
            if whitePawn3.onBoard:
                if whitePawn3.firstMove:
                    for x in range(1,3):
                        if x < 3:
                            if whitePawn3.indexIOnLogicArray - x >= 0:
                                if rectLogicArray[whitePawn3.indexIOnLogicArray - x][whitePawn3.indexJOnLogicArray] == 0:
                                    fourMoves[x-1] =  AdjustPositionAfterMove(whitePawn3.indexIOnLogicArray - x, whitePawn3.indexJOnLogicArray)
                                elif rectLogicArray[whitePawn3.indexIOnLogicArray - x][whitePawn3.indexJOnLogicArray] != 0:
                                    break
                        if whitePawn3.indexIOnLogicArray - 1 >= 0 and whitePawn3.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[whitePawn3.indexIOnLogicArray - 1][whitePawn3.indexJOnLogicArray + 1] < 0:
                                fourMoves[2] =  AdjustPositionAfterMove(whitePawn3.indexIOnLogicArray - 1, whitePawn3.indexJOnLogicArray+1)
                        if whitePawn3.indexIOnLogicArray - 1 >= 0 and whitePawn3.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[whitePawn3.indexIOnLogicArray - 1][whitePawn3.indexJOnLogicArray - 1] < 0:
                                fourMoves[3] =  AdjustPositionAfterMove(whitePawn3.indexIOnLogicArray - 1, whitePawn3.indexJOnLogicArray-1)
                    
                    return fourMoves
                    
                else:
                    if whitePawn3.indexIOnLogicArray - 1 >= 0:
                        if rectLogicArray[whitePawn3.indexIOnLogicArray - 1][whitePawn3.indexJOnLogicArray] == 0:
                            fourMoves[0] =  AdjustPositionAfterMove(whitePawn3.indexIOnLogicArray - 1, whitePawn3.indexJOnLogicArray)
                    if whitePawn3.indexIOnLogicArray - 1 >= 0 and whitePawn3.indexJOnLogicArray + 1 < 8:
                        if rectLogicArray[whitePawn3.indexIOnLogicArray - 1][whitePawn3.indexJOnLogicArray + 1] < 0:
                            fourMoves[2] =  AdjustPositionAfterMove(whitePawn3.indexIOnLogicArray - 1, whitePawn3.indexJOnLogicArray+1)
                    if whitePawn3.indexIOnLogicArray - 1 >= 0 and whitePawn3.indexJOnLogicArray - 1 >= 0:
                        if rectLogicArray[whitePawn3.indexIOnLogicArray - 1][whitePawn3.indexJOnLogicArray - 1] < 0:
                            fourMoves[3] =  AdjustPositionAfterMove(whitePawn3.indexIOnLogicArray - 1, whitePawn3.indexJOnLogicArray-1)
                    
                    return fourMoves
            
        if whichPawn == 4:
            if whitePawn4.onBoard:
                if whitePawn4.firstMove:
                    for x in range(1,3):
                        if x < 3:
                            if whitePawn4.indexIOnLogicArray - x >= 0:
                                if rectLogicArray[whitePawn4.indexIOnLogicArray - x][whitePawn4.indexJOnLogicArray] == 0:
                                    fourMoves[x-1] =  AdjustPositionAfterMove(whitePawn4.indexIOnLogicArray - x, whitePawn4.indexJOnLogicArray)
                                elif rectLogicArray[whitePawn4.indexIOnLogicArray - x][whitePawn4.indexJOnLogicArray] != 0:
                                    break
                        if whitePawn4.indexIOnLogicArray - 1 >= 0 and whitePawn4.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[whitePawn4.indexIOnLogicArray - 1][whitePawn4.indexJOnLogicArray + 1] < 0:
                                fourMoves[2] =  AdjustPositionAfterMove(whitePawn4.indexIOnLogicArray - 1, whitePawn4.indexJOnLogicArray+1)
                        if whitePawn4.indexIOnLogicArray - 1 >= 0 and whitePawn4.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[whitePawn4.indexIOnLogicArray - 1][whitePawn4.indexJOnLogicArray - 1] < 0:
                                fourMoves[3] =  AdjustPositionAfterMove(whitePawn4.indexIOnLogicArray - 1, whitePawn4.indexJOnLogicArray-1)
                    
                    return fourMoves
                    
                else:
                    if whitePawn4.indexIOnLogicArray - 1 >= 0:
                        if rectLogicArray[whitePawn4.indexIOnLogicArray - 1][whitePawn4.indexJOnLogicArray] == 0:
                            fourMoves[0] =  AdjustPositionAfterMove(whitePawn4.indexIOnLogicArray - 1, whitePawn4.indexJOnLogicArray)
                    if whitePawn4.indexIOnLogicArray - 1 >= 0 and whitePawn4.indexJOnLogicArray + 1 < 8:
                        if rectLogicArray[whitePawn4.indexIOnLogicArray - 1][whitePawn4.indexJOnLogicArray + 1] < 0:
                            fourMoves[2] =  AdjustPositionAfterMove(whitePawn4.indexIOnLogicArray - 1, whitePawn4.indexJOnLogicArray+1)
                    if whitePawn4.indexIOnLogicArray - 1 >= 0 and whitePawn4.indexJOnLogicArray - 1 >= 0:
                        if rectLogicArray[whitePawn4.indexIOnLogicArray - 1][whitePawn4.indexJOnLogicArray - 1] < 0:
                            fourMoves[3] =  AdjustPositionAfterMove(whitePawn4.indexIOnLogicArray - 1, whitePawn4.indexJOnLogicArray-1)
                    
                    return fourMoves
        
        if whichPawn == 5:
            if whitePawn5.onBoard:
                if whitePawn5.firstMove:
                    for x in range(1,3):
                        if x < 3:
                            if whitePawn5.indexIOnLogicArray - x >= 0:
                                if rectLogicArray[whitePawn5.indexIOnLogicArray - x][whitePawn5.indexJOnLogicArray] == 0:
                                    fourMoves[x-1] =  AdjustPositionAfterMove(whitePawn5.indexIOnLogicArray - x, whitePawn5.indexJOnLogicArray)
                                elif rectLogicArray[whitePawn5.indexIOnLogicArray - x][whitePawn5.indexJOnLogicArray] != 0:
                                    break
                        if whitePawn5.indexIOnLogicArray - 1 >= 0 and whitePawn5.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[whitePawn5.indexIOnLogicArray - 1][whitePawn5.indexJOnLogicArray + 1] < 0:
                                fourMoves[2] =  AdjustPositionAfterMove(whitePawn5.indexIOnLogicArray - 1, whitePawn5.indexJOnLogicArray+1)
                        if whitePawn5.indexIOnLogicArray - 1 >= 0 and whitePawn5.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[whitePawn5.indexIOnLogicArray - 1][whitePawn5.indexJOnLogicArray - 1] < 0:
                                fourMoves[3] =  AdjustPositionAfterMove(whitePawn5.indexIOnLogicArray - 1, whitePawn5.indexJOnLogicArray-1)
                    
                    return fourMoves
                    
                else:
                    if whitePawn5.indexIOnLogicArray - 1 >= 0:
                        if rectLogicArray[whitePawn5.indexIOnLogicArray - 1][whitePawn5.indexJOnLogicArray] == 0:
                            fourMoves[0] =  AdjustPositionAfterMove(whitePawn5.indexIOnLogicArray - 1, whitePawn5.indexJOnLogicArray)
                    if whitePawn5.indexIOnLogicArray - 1 >= 0 and whitePawn5.indexJOnLogicArray + 1 < 8:
                        if rectLogicArray[whitePawn5.indexIOnLogicArray - 1][whitePawn5.indexJOnLogicArray + 1] < 0:
                            fourMoves[2] =  AdjustPositionAfterMove(whitePawn5.indexIOnLogicArray - 1, whitePawn5.indexJOnLogicArray+1)
                    if whitePawn5.indexIOnLogicArray - 1 >= 0 and whitePawn5.indexJOnLogicArray - 1 >= 0:
                        if rectLogicArray[whitePawn5.indexIOnLogicArray - 1][whitePawn5.indexJOnLogicArray - 1] < 0:
                            fourMoves[3] =  AdjustPositionAfterMove(whitePawn5.indexIOnLogicArray - 1, whitePawn5.indexJOnLogicArray-1)
                    
                    return fourMoves
        
        if whichPawn == 6:
            if whitePawn6.onBoard:
                if whitePawn6.firstMove:
                    for x in range(1,3):
                        if x < 3:
                            if whitePawn6.indexIOnLogicArray - x >= 0:
                                if rectLogicArray[whitePawn6.indexIOnLogicArray - x][whitePawn6.indexJOnLogicArray] == 0:
                                    fourMoves[x-1] =  AdjustPositionAfterMove(whitePawn6.indexIOnLogicArray - x, whitePawn6.indexJOnLogicArray)
                                elif rectLogicArray[whitePawn6.indexIOnLogicArray - x][whitePawn6.indexJOnLogicArray] != 0:
                                    break
                        if whitePawn6.indexIOnLogicArray - 1 >= 0 and whitePawn6.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[whitePawn6.indexIOnLogicArray - 1][whitePawn6.indexJOnLogicArray + 1] < 0:
                                fourMoves[2] =  AdjustPositionAfterMove(whitePawn6.indexIOnLogicArray - 1, whitePawn6.indexJOnLogicArray+1)
                        if whitePawn6.indexIOnLogicArray - 1 >= 0 and whitePawn6.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[whitePawn6.indexIOnLogicArray - 1][whitePawn6.indexJOnLogicArray - 1] < 0:
                                fourMoves[3] =  AdjustPositionAfterMove(whitePawn6.indexIOnLogicArray - 1, whitePawn6.indexJOnLogicArray-1)
                    
                    return fourMoves
                    
                else:
                    if whitePawn6.indexIOnLogicArray - 1 >= 0:
                        if rectLogicArray[whitePawn6.indexIOnLogicArray - 1][whitePawn6.indexJOnLogicArray] == 0:
                            fourMoves[0] =  AdjustPositionAfterMove(whitePawn6.indexIOnLogicArray - 1, whitePawn6.indexJOnLogicArray)
                    if whitePawn6.indexIOnLogicArray - 1 >= 0 and whitePawn6.indexJOnLogicArray + 1 < 8:
                        if rectLogicArray[whitePawn6.indexIOnLogicArray - 1][whitePawn6.indexJOnLogicArray + 1] < 0:
                            fourMoves[2] =  AdjustPositionAfterMove(whitePawn6.indexIOnLogicArray - 1, whitePawn6.indexJOnLogicArray+1)
                    if whitePawn6.indexIOnLogicArray - 1 >= 0 and whitePawn6.indexJOnLogicArray - 1 >= 0:
                        if rectLogicArray[whitePawn6.indexIOnLogicArray - 1][whitePawn6.indexJOnLogicArray - 1] < 0:
                            fourMoves[3] =  AdjustPositionAfterMove(whitePawn6.indexIOnLogicArray - 1, whitePawn6.indexJOnLogicArray-1)
                    
                    return fourMoves
        
        if whichPawn == 7:
            if whitePawn7.onBoard:
                if whitePawn7.firstMove:
                    for x in range(1,3):
                        if x < 3:
                            if whitePawn7.indexIOnLogicArray - x >= 0:
                                if rectLogicArray[whitePawn7.indexIOnLogicArray - x][whitePawn7.indexJOnLogicArray] == 0:
                                    fourMoves[x-1] =  AdjustPositionAfterMove(whitePawn7.indexIOnLogicArray - x, whitePawn7.indexJOnLogicArray)
                                elif rectLogicArray[whitePawn7.indexIOnLogicArray - x][whitePawn7.indexJOnLogicArray] != 0:
                                    break
                        if whitePawn7.indexIOnLogicArray - 1 >= 0 and whitePawn7.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[whitePawn7.indexIOnLogicArray - 1][whitePawn7.indexJOnLogicArray + 1] < 0:
                                fourMoves[2] =  AdjustPositionAfterMove(whitePawn7.indexIOnLogicArray - 1, whitePawn7.indexJOnLogicArray+1)
                        if whitePawn7.indexIOnLogicArray - 1 >= 0 and whitePawn7.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[whitePawn7.indexIOnLogicArray - 1][whitePawn7.indexJOnLogicArray - 1] < 0:
                                fourMoves[3] =  AdjustPositionAfterMove(whitePawn7.indexIOnLogicArray - 1, whitePawn7.indexJOnLogicArray-1)
                    
                    return fourMoves
                    
                else:
                    if whitePawn7.indexIOnLogicArray - 1 >= 0:
                        if rectLogicArray[whitePawn7.indexIOnLogicArray - 1][whitePawn7.indexJOnLogicArray] == 0:
                            fourMoves[0] =  AdjustPositionAfterMove(whitePawn7.indexIOnLogicArray - 1, whitePawn7.indexJOnLogicArray)
                    if whitePawn7.indexIOnLogicArray - 1 >= 0 and whitePawn7.indexJOnLogicArray + 1 < 8:
                        if rectLogicArray[whitePawn7.indexIOnLogicArray - 1][whitePawn7.indexJOnLogicArray + 1] < 0:
                            fourMoves[2] =  AdjustPositionAfterMove(whitePawn7.indexIOnLogicArray - 1, whitePawn7.indexJOnLogicArray+1)
                    if whitePawn7.indexIOnLogicArray - 1 >= 0 and whitePawn7.indexJOnLogicArray - 1 >= 0:
                        if rectLogicArray[whitePawn7.indexIOnLogicArray - 1][whitePawn7.indexJOnLogicArray - 1] < 0:
                            fourMoves[3] =  AdjustPositionAfterMove(whitePawn7.indexIOnLogicArray - 1, whitePawn7.indexJOnLogicArray-1)
                    
                    return fourMoves
        
        if whichPawn == 8:
            if whitePawn8.onBoard:
                if whitePawn8.firstMove:
                    for x in range(1,3):
                        if x < 3:
                            if whitePawn8.indexIOnLogicArray - x >= 0:
                                if rectLogicArray[whitePawn8.indexIOnLogicArray - x][whitePawn8.indexJOnLogicArray] == 0:
                                    fourMoves[x-1] =  AdjustPositionAfterMove(whitePawn8.indexIOnLogicArray - x, whitePawn8.indexJOnLogicArray)
                                elif rectLogicArray[whitePawn8.indexIOnLogicArray - x][whitePawn8.indexJOnLogicArray] != 0:
                                    break
                        if whitePawn8.indexIOnLogicArray - 1 >= 0 and whitePawn8.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[whitePawn8.indexIOnLogicArray - 1][whitePawn8.indexJOnLogicArray + 1] < 0:
                                fourMoves[2] =  AdjustPositionAfterMove(whitePawn8.indexIOnLogicArray - 1, whitePawn8.indexJOnLogicArray+1)
                        if whitePawn8.indexIOnLogicArray - 1 >= 0 and whitePawn8.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[whitePawn8.indexIOnLogicArray - 1][whitePawn8.indexJOnLogicArray - 1] < 0:
                                fourMoves[3] =  AdjustPositionAfterMove(whitePawn8.indexIOnLogicArray - 1, whitePawn8.indexJOnLogicArray-1)
                    
                    return fourMoves
                    
                else:
                    if whitePawn8.indexIOnLogicArray - 1 >= 0:
                        if rectLogicArray[whitePawn8.indexIOnLogicArray - 1][whitePawn8.indexJOnLogicArray] == 0:
                            fourMoves[0] =  AdjustPositionAfterMove(whitePawn8.indexIOnLogicArray - 1, whitePawn8.indexJOnLogicArray)
                    if whitePawn8.indexIOnLogicArray - 1 >= 0 and whitePawn8.indexJOnLogicArray + 1 < 8:
                        if rectLogicArray[whitePawn8.indexIOnLogicArray - 1][whitePawn8.indexJOnLogicArray + 1] < 0:
                            fourMoves[2] =  AdjustPositionAfterMove(whitePawn8.indexIOnLogicArray - 1, whitePawn8.indexJOnLogicArray+1)
                    if whitePawn8.indexIOnLogicArray - 1 >= 0 and whitePawn8.indexJOnLogicArray - 1 >= 0:
                        if rectLogicArray[whitePawn8.indexIOnLogicArray - 1][whitePawn8.indexJOnLogicArray - 1] < 0:
                            fourMoves[3] =  AdjustPositionAfterMove(whitePawn8.indexIOnLogicArray - 1, whitePawn8.indexJOnLogicArray-1)
                    
                    return fourMoves

    elif turn == 'black':
        
        if whichPawn == 1:
            if blackPawn1.onBoard:
                if blackPawn1.firstMove:
                    for x in range(1,3):
                        if x < 3:
                            if blackPawn1.indexIOnLogicArray + x >= 0:
                                if rectLogicArray[blackPawn1.indexIOnLogicArray + x][blackPawn1.indexJOnLogicArray] == 0:
                                    fourMoves[x-1] =  AdjustPositionAfterMove(blackPawn1.indexIOnLogicArray + x, blackPawn1.indexJOnLogicArray)
                                elif rectLogicArray[blackPawn1.indexIOnLogicArray + x][blackPawn1.indexJOnLogicArray] != 0:
                                    break
                        if blackPawn1.indexIOnLogicArray + 1 < 8 and blackPawn1.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[blackPawn1.indexIOnLogicArray + 1][blackPawn1.indexJOnLogicArray + 1] > 0:
                                fourMoves[2] = AdjustPositionAfterMove(blackPawn1.indexIOnLogicArray + 1, blackPawn1.indexJOnLogicArray + 1)
                        if blackPawn1.indexIOnLogicArray + 1 < 8 and blackPawn1.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[blackPawn1.indexIOnLogicArray + 1][blackPawn1.indexJOnLogicArray - 1] > 0:
                                fourMoves[3] = AdjustPositionAfterMove(blackPawn1.indexIOnLogicArray + 1, blackPawn1.indexJOnLogicArray - 1)
                    
                    return fourMoves  
                else:
                    if blackPawn1.indexIOnLogicArray + 1 >= 0:
                            if rectLogicArray[blackPawn1.indexIOnLogicArray + 1][blackPawn1.indexJOnLogicArray] == 0:
                                fourMoves[0] =  AdjustPositionAfterMove(blackPawn1.indexIOnLogicArray + 1, blackPawn1.indexJOnLogicArray)
                    if blackPawn1.indexIOnLogicArray + 1 < 8 and blackPawn1.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[blackPawn1.indexIOnLogicArray + 1][blackPawn1.indexJOnLogicArray + 1] > 0:
                                fourMoves[2] = AdjustPositionAfterMove(blackPawn1.indexIOnLogicArray + 1, blackPawn1.indexJOnLogicArray + 1)
                    if blackPawn1.indexIOnLogicArray + 1 < 8 and blackPawn1.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[blackPawn1.indexIOnLogicArray + 1][blackPawn1.indexJOnLogicArray - 1] > 0:
                                fourMoves[3] = AdjustPositionAfterMove(blackPawn1.indexIOnLogicArray + 1, blackPawn1.indexJOnLogicArray - 1)   
                    return fourMoves 
        
        if whichPawn == 2:
            if blackPawn2.onBoard:
                if blackPawn2.firstMove:
                    for x in range(1,3):
                        if x < 3:
                            if blackPawn2.indexIOnLogicArray + x >= 0:
                                if rectLogicArray[blackPawn2.indexIOnLogicArray + x][blackPawn2.indexJOnLogicArray] == 0:
                                    fourMoves[x-1] =  AdjustPositionAfterMove(blackPawn2.indexIOnLogicArray + x, blackPawn2.indexJOnLogicArray)
                                elif rectLogicArray[blackPawn2.indexIOnLogicArray + x][blackPawn2.indexJOnLogicArray] != 0:
                                    break
                        if blackPawn2.indexIOnLogicArray + 1 < 8 and blackPawn2.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[blackPawn2.indexIOnLogicArray + 1][blackPawn2.indexJOnLogicArray + 1] > 0:
                                fourMoves[2] = AdjustPositionAfterMove(blackPawn2.indexIOnLogicArray + 1, blackPawn2.indexJOnLogicArray + 1)
                        if blackPawn2.indexIOnLogicArray + 1 < 8 and blackPawn2.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[blackPawn2.indexIOnLogicArray + 1][blackPawn2.indexJOnLogicArray - 1] > 0:
                                fourMoves[3] = AdjustPositionAfterMove(blackPawn2.indexIOnLogicArray + 1, blackPawn2.indexJOnLogicArray - 1)
                    
                    return fourMoves  
                else:
                    if blackPawn2.indexIOnLogicArray + 1 >= 0:
                            if rectLogicArray[blackPawn2.indexIOnLogicArray + 1][blackPawn2.indexJOnLogicArray] == 0:
                                fourMoves[0] =  AdjustPositionAfterMove(blackPawn2.indexIOnLogicArray + 1, blackPawn2.indexJOnLogicArray)
                    if blackPawn2.indexIOnLogicArray + 1 < 8 and blackPawn2.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[blackPawn2.indexIOnLogicArray + 1][blackPawn2.indexJOnLogicArray + 1] > 0:
                                fourMoves[2] = AdjustPositionAfterMove(blackPawn2.indexIOnLogicArray + 1, blackPawn2.indexJOnLogicArray + 1)
                    if blackPawn2.indexIOnLogicArray + 1 < 8 and blackPawn2.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[blackPawn2.indexIOnLogicArray + 1][blackPawn2.indexJOnLogicArray - 1] > 0:
                                fourMoves[3] = AdjustPositionAfterMove(blackPawn2.indexIOnLogicArray + 1, blackPawn2.indexJOnLogicArray - 1)   
                    return fourMoves
            
        if whichPawn == 3:
            if blackPawn3.onBoard:
                if blackPawn3.firstMove:
                    for x in range(1,3):
                        if x < 3:
                            if blackPawn3.indexIOnLogicArray + x >= 0:
                                if rectLogicArray[blackPawn3.indexIOnLogicArray + x][blackPawn3.indexJOnLogicArray] == 0:
                                    fourMoves[x-1] =  AdjustPositionAfterMove(blackPawn3.indexIOnLogicArray + x, blackPawn3.indexJOnLogicArray)
                                elif rectLogicArray[blackPawn3.indexIOnLogicArray + x][blackPawn3.indexJOnLogicArray] != 0:
                                    break
                        if blackPawn3.indexIOnLogicArray + 1 < 8 and blackPawn3.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[blackPawn3.indexIOnLogicArray + 1][blackPawn3.indexJOnLogicArray + 1] > 0:
                                fourMoves[2] = AdjustPositionAfterMove(blackPawn3.indexIOnLogicArray + 1, blackPawn3.indexJOnLogicArray + 1)
                        if blackPawn3.indexIOnLogicArray + 1 < 8 and blackPawn3.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[blackPawn3.indexIOnLogicArray + 1][blackPawn3.indexJOnLogicArray - 1] > 0:
                                fourMoves[3] = AdjustPositionAfterMove(blackPawn3.indexIOnLogicArray + 1, blackPawn3.indexJOnLogicArray - 1)
                    
                    return fourMoves  
                else:
                    if blackPawn3.indexIOnLogicArray + 1 >= 0:
                            if rectLogicArray[blackPawn3.indexIOnLogicArray + 1][blackPawn3.indexJOnLogicArray] == 0:
                                fourMoves[0] =  AdjustPositionAfterMove(blackPawn3.indexIOnLogicArray + 1, blackPawn3.indexJOnLogicArray)
                    if blackPawn3.indexIOnLogicArray + 1 < 8 and blackPawn3.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[blackPawn3.indexIOnLogicArray + 1][blackPawn3.indexJOnLogicArray + 1] > 0:
                                fourMoves[2] = AdjustPositionAfterMove(blackPawn3.indexIOnLogicArray + 1, blackPawn3.indexJOnLogicArray + 1)
                    if blackPawn3.indexIOnLogicArray + 1 < 8 and blackPawn3.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[blackPawn3.indexIOnLogicArray + 1][blackPawn3.indexJOnLogicArray - 1] > 0:
                                fourMoves[3] = AdjustPositionAfterMove(blackPawn3.indexIOnLogicArray + 1, blackPawn3.indexJOnLogicArray - 1)   
                    return fourMoves
        
        if whichPawn == 4:
            if blackPawn4.onBoard:
                if blackPawn4.firstMove:
                    for x in range(1,3):
                        if x < 3:
                            if blackPawn4.indexIOnLogicArray + x >= 0:
                                if rectLogicArray[blackPawn4.indexIOnLogicArray + x][blackPawn4.indexJOnLogicArray] == 0:
                                    fourMoves[x-1] =  AdjustPositionAfterMove(blackPawn4.indexIOnLogicArray + x, blackPawn4.indexJOnLogicArray)
                                elif rectLogicArray[blackPawn4.indexIOnLogicArray + x][blackPawn4.indexJOnLogicArray] != 0:
                                    break
                        if blackPawn4.indexIOnLogicArray + 1 < 8 and blackPawn4.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[blackPawn4.indexIOnLogicArray + 1][blackPawn4.indexJOnLogicArray + 1] > 0:
                                fourMoves[2] = AdjustPositionAfterMove(blackPawn4.indexIOnLogicArray + 1, blackPawn4.indexJOnLogicArray + 1)
                        if blackPawn4.indexIOnLogicArray + 1 < 8 and blackPawn4.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[blackPawn4.indexIOnLogicArray + 1][blackPawn4.indexJOnLogicArray - 1] > 0:
                                fourMoves[3] = AdjustPositionAfterMove(blackPawn4.indexIOnLogicArray + 1, blackPawn4.indexJOnLogicArray - 1)
                    
                    return fourMoves  
                else:
                    if blackPawn4.indexIOnLogicArray + 1 >= 0:
                            if rectLogicArray[blackPawn4.indexIOnLogicArray + 1][blackPawn4.indexJOnLogicArray] == 0:
                                fourMoves[0] =  AdjustPositionAfterMove(blackPawn4.indexIOnLogicArray + 1, blackPawn4.indexJOnLogicArray)
                    if blackPawn4.indexIOnLogicArray + 1 < 8 and blackPawn4.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[blackPawn4.indexIOnLogicArray + 1][blackPawn4.indexJOnLogicArray + 1] > 0:
                                fourMoves[2] = AdjustPositionAfterMove(blackPawn4.indexIOnLogicArray + 1, blackPawn4.indexJOnLogicArray + 1)
                    if blackPawn4.indexIOnLogicArray + 1 < 8 and blackPawn4.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[blackPawn4.indexIOnLogicArray + 1][blackPawn4.indexJOnLogicArray - 1] > 0:
                                fourMoves[3] = AdjustPositionAfterMove(blackPawn4.indexIOnLogicArray + 1, blackPawn4.indexJOnLogicArray - 1)   
                    return fourMoves
        
        if whichPawn == 5:
            if blackPawn5.onBoard:
                if blackPawn5.firstMove:
                    for x in range(1,3):
                        if x < 3:
                            if blackPawn5.indexIOnLogicArray + x >= 0:
                                if rectLogicArray[blackPawn5.indexIOnLogicArray + x][blackPawn5.indexJOnLogicArray] == 0:
                                    fourMoves[x-1] =  AdjustPositionAfterMove(blackPawn5.indexIOnLogicArray + x, blackPawn5.indexJOnLogicArray)
                                elif rectLogicArray[blackPawn5.indexIOnLogicArray + x][blackPawn5.indexJOnLogicArray] != 0:
                                    break
                        if blackPawn5.indexIOnLogicArray + 1 < 8 and blackPawn5.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[blackPawn5.indexIOnLogicArray + 1][blackPawn5.indexJOnLogicArray + 1] > 0:
                                fourMoves[2] = AdjustPositionAfterMove(blackPawn5.indexIOnLogicArray + 1, blackPawn5.indexJOnLogicArray + 1)
                        if blackPawn5.indexIOnLogicArray + 1 < 8 and blackPawn5.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[blackPawn5.indexIOnLogicArray + 1][blackPawn5.indexJOnLogicArray - 1] > 0:
                                fourMoves[3] = AdjustPositionAfterMove(blackPawn5.indexIOnLogicArray + 1, blackPawn5.indexJOnLogicArray - 1)
                    
                    return fourMoves  
                else:
                    if blackPawn5.indexIOnLogicArray + 1 >= 0:
                            if rectLogicArray[blackPawn5.indexIOnLogicArray + 1][blackPawn5.indexJOnLogicArray] == 0:
                                fourMoves[0] =  AdjustPositionAfterMove(blackPawn5.indexIOnLogicArray + 1, blackPawn5.indexJOnLogicArray)
                    if blackPawn5.indexIOnLogicArray + 1 < 8 and blackPawn5.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[blackPawn5.indexIOnLogicArray + 1][blackPawn5.indexJOnLogicArray + 1] > 0:
                                fourMoves[2] = AdjustPositionAfterMove(blackPawn5.indexIOnLogicArray + 1, blackPawn5.indexJOnLogicArray + 1)
                    if blackPawn5.indexIOnLogicArray + 1 < 8 and blackPawn5.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[blackPawn5.indexIOnLogicArray + 1][blackPawn5.indexJOnLogicArray - 1] > 0:
                                fourMoves[3] = AdjustPositionAfterMove(blackPawn5.indexIOnLogicArray + 1, blackPawn5.indexJOnLogicArray - 1)   
                    return fourMoves
        
        if whichPawn == 6:
            if blackPawn6.onBoard:
                if blackPawn6.firstMove:
                    for x in range(1,3):
                        if x < 3:
                            if blackPawn6.indexIOnLogicArray + x >= 0:
                                if rectLogicArray[blackPawn6.indexIOnLogicArray + x][blackPawn6.indexJOnLogicArray] == 0:
                                    fourMoves[x-1] =  AdjustPositionAfterMove(blackPawn6.indexIOnLogicArray + x, blackPawn6.indexJOnLogicArray)
                                elif rectLogicArray[blackPawn6.indexIOnLogicArray + x][blackPawn6.indexJOnLogicArray] != 0:
                                    break
                        if blackPawn6.indexIOnLogicArray + 1 < 8 and blackPawn6.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[blackPawn6.indexIOnLogicArray + 1][blackPawn6.indexJOnLogicArray + 1] > 0:
                                fourMoves[2] = AdjustPositionAfterMove(blackPawn6.indexIOnLogicArray + 1, blackPawn6.indexJOnLogicArray + 1)
                        if blackPawn6.indexIOnLogicArray + 1 < 8 and blackPawn6.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[blackPawn6.indexIOnLogicArray + 1][blackPawn6.indexJOnLogicArray - 1] > 0:
                                fourMoves[3] = AdjustPositionAfterMove(blackPawn6.indexIOnLogicArray + 1, blackPawn6.indexJOnLogicArray - 1)
                    
                    return fourMoves  
                else:
                    if blackPawn6.indexIOnLogicArray + 1 >= 0:
                            if rectLogicArray[blackPawn6.indexIOnLogicArray + 1][blackPawn6.indexJOnLogicArray] == 0:
                                fourMoves[0] =  AdjustPositionAfterMove(blackPawn6.indexIOnLogicArray + 1, blackPawn6.indexJOnLogicArray)
                    if blackPawn6.indexIOnLogicArray + 1 < 8 and blackPawn6.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[blackPawn6.indexIOnLogicArray + 1][blackPawn6.indexJOnLogicArray + 1] > 0:
                                fourMoves[2] = AdjustPositionAfterMove(blackPawn6.indexIOnLogicArray + 1, blackPawn6.indexJOnLogicArray + 1)
                    if blackPawn6.indexIOnLogicArray + 1 < 8 and blackPawn6.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[blackPawn6.indexIOnLogicArray + 1][blackPawn6.indexJOnLogicArray - 1] > 0:
                                fourMoves[3] = AdjustPositionAfterMove(blackPawn6.indexIOnLogicArray + 1, blackPawn6.indexJOnLogicArray - 1)   
                    return fourMoves
        
        if whichPawn == 7:
            if blackPawn7.onBoard:
                if blackPawn7.firstMove:
                    for x in range(1,3):
                        if x < 3:
                            if blackPawn7.indexIOnLogicArray + x >= 0:
                                if rectLogicArray[blackPawn7.indexIOnLogicArray + x][blackPawn7.indexJOnLogicArray] == 0:
                                    fourMoves[x-1] =  AdjustPositionAfterMove(blackPawn7.indexIOnLogicArray + x, blackPawn7.indexJOnLogicArray)
                                elif rectLogicArray[blackPawn7.indexIOnLogicArray + x][blackPawn7.indexJOnLogicArray] != 0:
                                    break
                        if blackPawn7.indexIOnLogicArray + 1 < 8 and blackPawn7.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[blackPawn7.indexIOnLogicArray + 1][blackPawn7.indexJOnLogicArray + 1] > 0:
                                fourMoves[2] = AdjustPositionAfterMove(blackPawn7.indexIOnLogicArray + 1, blackPawn7.indexJOnLogicArray + 1)
                        if blackPawn7.indexIOnLogicArray + 1 < 8 and blackPawn7.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[blackPawn7.indexIOnLogicArray + 1][blackPawn7.indexJOnLogicArray - 1] > 0:
                                fourMoves[3] = AdjustPositionAfterMove(blackPawn7.indexIOnLogicArray + 1, blackPawn7.indexJOnLogicArray - 1)
                    
                    return fourMoves  
                else:
                    if blackPawn7.indexIOnLogicArray + 1 >= 0:
                            if rectLogicArray[blackPawn7.indexIOnLogicArray + 1][blackPawn7.indexJOnLogicArray] == 0:
                                fourMoves[0] =  AdjustPositionAfterMove(blackPawn7.indexIOnLogicArray + 1, blackPawn7.indexJOnLogicArray)
                    if blackPawn7.indexIOnLogicArray + 1 < 8 and blackPawn7.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[blackPawn7.indexIOnLogicArray + 1][blackPawn7.indexJOnLogicArray + 1] > 0:
                                fourMoves[2] = AdjustPositionAfterMove(blackPawn7.indexIOnLogicArray + 1, blackPawn7.indexJOnLogicArray + 1)
                    if blackPawn7.indexIOnLogicArray + 1 < 8 and blackPawn7.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[blackPawn7.indexIOnLogicArray + 1][blackPawn7.indexJOnLogicArray - 1] > 0:
                                fourMoves[3] = AdjustPositionAfterMove(blackPawn7.indexIOnLogicArray + 1, blackPawn7.indexJOnLogicArray - 1)   
                    return fourMoves
            
        if whichPawn == 8:
            if blackPawn8.onBoard:
                if blackPawn8.firstMove:
                    for x in range(1,3):
                        if x < 3:
                            if blackPawn8.indexIOnLogicArray + x >= 0:
                                if rectLogicArray[blackPawn8.indexIOnLogicArray + x][blackPawn8.indexJOnLogicArray] == 0:
                                    fourMoves[x-1] =  AdjustPositionAfterMove(blackPawn8.indexIOnLogicArray + x, blackPawn8.indexJOnLogicArray)
                                elif rectLogicArray[blackPawn8.indexIOnLogicArray + x][blackPawn8.indexJOnLogicArray] != 0:
                                    break
                        if blackPawn8.indexIOnLogicArray + 1 < 8 and blackPawn8.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[blackPawn8.indexIOnLogicArray + 1][blackPawn8.indexJOnLogicArray + 1] > 0:
                                fourMoves[2] = AdjustPositionAfterMove(blackPawn8.indexIOnLogicArray + 1, blackPawn8.indexJOnLogicArray + 1)
                        if blackPawn8.indexIOnLogicArray + 1 < 8 and blackPawn8.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[blackPawn8.indexIOnLogicArray + 1][blackPawn8.indexJOnLogicArray - 1] > 0:
                                fourMoves[3] = AdjustPositionAfterMove(blackPawn8.indexIOnLogicArray + 1, blackPawn8.indexJOnLogicArray - 1)
                    
                    return fourMoves  
                else:
                    if blackPawn8.indexIOnLogicArray + 1 >= 0:
                            if rectLogicArray[blackPawn8.indexIOnLogicArray + 1][blackPawn8.indexJOnLogicArray] == 0:
                                fourMoves[0] =  AdjustPositionAfterMove(blackPawn8.indexIOnLogicArray + 1, blackPawn8.indexJOnLogicArray)
                    if blackPawn8.indexIOnLogicArray + 1 < 8 and blackPawn8.indexJOnLogicArray + 1 < 8:
                            if rectLogicArray[blackPawn8.indexIOnLogicArray + 1][blackPawn8.indexJOnLogicArray + 1] > 0:
                                fourMoves[2] = AdjustPositionAfterMove(blackPawn8.indexIOnLogicArray + 1, blackPawn8.indexJOnLogicArray + 1)
                    if blackPawn8.indexIOnLogicArray + 1 < 8 and blackPawn8.indexJOnLogicArray - 1 >= 0:
                            if rectLogicArray[blackPawn8.indexIOnLogicArray + 1][blackPawn8.indexJOnLogicArray - 1] > 0:
                                fourMoves[3] = AdjustPositionAfterMove(blackPawn8.indexIOnLogicArray + 1, blackPawn8.indexJOnLogicArray - 1)   
                    return fourMoves    
                        
def MovePositionOfPawn(turn, whichPawn, wherePawnCanMove, whereMouseIs):
    global switchTurn
    switchTurn = False
    # Movement of the pawn
    if turn == 'white':
        if whichPawn == 1:
            if wherePawnCanMove != [(0,0), (0,0), (0,0), (0,0)]: # If the movement list is not empty
                if whitePawn1.firstMove:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs): # If where the mouse is alligns with potential moves
                            whitePawn1.rect.x, whitePawn1.rect.y = whereMouseIs # movement of the pawn
                            CenterPawnInTile(turn, whichPawn) # ensures the pawn is centered in its new tile
                            PiecesCollide(turn) # If it collides with a piece of opposite colour it removes them from the board
                            
                            if whitePawn1.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)): # Ensures the movement of the pawn is on the right tile
                                rectLogicArray[whitePawn1.indexIOnLogicArray][whitePawn1.indexJOnLogicArray] = 0 # Starting here the position of the pawn is updated in the logic array
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                whitePawn1.indexIOnLogicArray, whitePawn1.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[whitePawn1.indexIOnLogicArray][whitePawn1.indexJOnLogicArray] = 1 # Ending here
                                switchTurn = True # Signals that whites turn is over
                                whitePawn1.pos = wherePawnCanMove[x] # Updates position in the object
                                whitePawn1.firstMove = False # Signals that the first move has been made to change the amount of potential moves next turn
                else:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            whitePawn1.rect.x, whitePawn1.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if whitePawn1.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[whitePawn1.indexIOnLogicArray][whitePawn1.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                whitePawn1.indexIOnLogicArray, whitePawn1.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[whitePawn1.indexIOnLogicArray][whitePawn1.indexJOnLogicArray] = 1
                                switchTurn = True
                                whitePawn1.pos = wherePawnCanMove[x]
                                whitePawn1.firstMove = False
        
        if whichPawn == 2:
            if wherePawnCanMove != [(0,0), (0,0), (0,0), (0,0)]:
                if whitePawn2.firstMove:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            whitePawn2.rect.x, whitePawn2.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if whitePawn2.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[whitePawn2.indexIOnLogicArray][whitePawn2.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                whitePawn2.indexIOnLogicArray, whitePawn2.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[whitePawn2.indexIOnLogicArray][whitePawn2.indexJOnLogicArray] = 1
                                switchTurn = True
                                whitePawn2.pos = wherePawnCanMove[x]
                                whitePawn2.firstMove = False
                else:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            whitePawn2.rect.x, whitePawn2.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if whitePawn2.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[whitePawn2.indexIOnLogicArray][whitePawn2.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                whitePawn2.indexIOnLogicArray, whitePawn2.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[whitePawn2.indexIOnLogicArray][whitePawn2.indexJOnLogicArray] = 1
                                switchTurn = True
                                whitePawn2.pos = wherePawnCanMove[x]
                                whitePawn2.firstMove = False
        
        if whichPawn == 3:
            if wherePawnCanMove != [(0,0), (0,0), (0,0), (0,0)]:
                if whitePawn3.firstMove:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            whitePawn3.rect.x, whitePawn3.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if whitePawn3.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[whitePawn3.indexIOnLogicArray][whitePawn3.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                whitePawn3.indexIOnLogicArray, whitePawn3.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[whitePawn3.indexIOnLogicArray][whitePawn3.indexJOnLogicArray] = 1
                                switchTurn = True
                                whitePawn3.pos = wherePawnCanMove[x]
                                whitePawn3.firstMove = False
                else:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            whitePawn3.rect.x, whitePawn3.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if whitePawn3.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[whitePawn3.indexIOnLogicArray][whitePawn3.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                whitePawn3.indexIOnLogicArray, whitePawn3.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[whitePawn3.indexIOnLogicArray][whitePawn3.indexJOnLogicArray] = 1
                                switchTurn = True
                                whitePawn3.pos = wherePawnCanMove[x]
                                whitePawn3.firstMove = False
        
        if whichPawn == 4:
            if wherePawnCanMove != [(0,0), (0,0), (0,0), (0,0)]:
                if whitePawn4.firstMove:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            whitePawn4.rect.x, whitePawn4.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if whitePawn4.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[whitePawn4.indexIOnLogicArray][whitePawn4.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                whitePawn4.indexIOnLogicArray, whitePawn4.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[whitePawn4.indexIOnLogicArray][whitePawn4.indexJOnLogicArray] = 1
                                switchTurn = True
                                whitePawn4.pos = wherePawnCanMove[x]
                                whitePawn4.firstMove = False
                else:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            whitePawn4.rect.x, whitePawn4.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if whitePawn4.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[whitePawn4.indexIOnLogicArray][whitePawn4.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                whitePawn4.indexIOnLogicArray, whitePawn4.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[whitePawn4.indexIOnLogicArray][whitePawn4.indexJOnLogicArray] = 1
                                switchTurn = True
                                whitePawn4.pos = wherePawnCanMove[x]
                                whitePawn4.firstMove = False
        
        if whichPawn == 5:
            if wherePawnCanMove != [(0,0), (0,0), (0,0), (0,0)]:
                if whitePawn5.firstMove:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            whitePawn5.rect.x, whitePawn5.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if whitePawn5.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[whitePawn5.indexIOnLogicArray][whitePawn5.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                whitePawn5.indexIOnLogicArray, whitePawn5.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[whitePawn5.indexIOnLogicArray][whitePawn5.indexJOnLogicArray] = 1
                                switchTurn = True
                                whitePawn5.pos = wherePawnCanMove[x]
                                whitePawn5.firstMove = False
                else:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            whitePawn5.rect.x, whitePawn5.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if whitePawn5.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[whitePawn5.indexIOnLogicArray][whitePawn5.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                whitePawn5.indexIOnLogicArray, whitePawn5.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[whitePawn5.indexIOnLogicArray][whitePawn5.indexJOnLogicArray] = 1
                                switchTurn = True
                                whitePawn5.pos = wherePawnCanMove[x]
                                whitePawn5.firstMove = False
        
        if whichPawn == 6:
            if wherePawnCanMove != [(0,0), (0,0), (0,0), (0,0)]:
                if whitePawn6.firstMove:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            whitePawn6.rect.x, whitePawn6.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if whitePawn6.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[whitePawn6.indexIOnLogicArray][whitePawn6.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                whitePawn6.indexIOnLogicArray, whitePawn6.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[whitePawn6.indexIOnLogicArray][whitePawn6.indexJOnLogicArray] = 1
                                switchTurn = True
                                whitePawn6.pos = wherePawnCanMove[x]
                                whitePawn6.firstMove = False
                else:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            whitePawn6.rect.x, whitePawn6.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if whitePawn6.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[whitePawn6.indexIOnLogicArray][whitePawn6.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                whitePawn6.indexIOnLogicArray, whitePawn6.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[whitePawn6.indexIOnLogicArray][whitePawn6.indexJOnLogicArray] = 1
                                switchTurn = True
                                whitePawn6.pos = wherePawnCanMove[x]
                                whitePawn6.firstMove = False
        
        if whichPawn == 7:
            if wherePawnCanMove != [(0,0), (0,0), (0,0), (0,0)]:
                if whitePawn7.firstMove:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            whitePawn7.rect.x, whitePawn7.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if whitePawn7.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[whitePawn7.indexIOnLogicArray][whitePawn7.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                whitePawn7.indexIOnLogicArray, whitePawn7.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[whitePawn7.indexIOnLogicArray][whitePawn7.indexJOnLogicArray] = 1
                                switchTurn = True
                                whitePawn7.pos = wherePawnCanMove[x]
                                whitePawn7.firstMove = False
                else:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            whitePawn7.rect.x, whitePawn7.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if whitePawn7.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[whitePawn7.indexIOnLogicArray][whitePawn7.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                whitePawn7.indexIOnLogicArray, whitePawn7.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[whitePawn7.indexIOnLogicArray][whitePawn7.indexJOnLogicArray] = 1
                                switchTurn = True
                                whitePawn7.pos = wherePawnCanMove[x]
                                whitePawn7.firstMove = False
        
        if whichPawn == 8:
            if wherePawnCanMove != [(0,0), (0,0), (0,0), (0,0)]:
                if whitePawn8.firstMove:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            whitePawn8.rect.x, whitePawn8.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if whitePawn8.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[whitePawn8.indexIOnLogicArray][whitePawn8.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                whitePawn8.indexIOnLogicArray, whitePawn8.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[whitePawn8.indexIOnLogicArray][whitePawn8.indexJOnLogicArray] = 1
                                switchTurn = True
                                whitePawn8.pos = wherePawnCanMove[x]
                                whitePawn8.firstMove = False
                else:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            whitePawn8.rect.x, whitePawn8.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if whitePawn8.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[whitePawn8.indexIOnLogicArray][whitePawn8.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                whitePawn8.indexIOnLogicArray, whitePawn8.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[whitePawn8.indexIOnLogicArray][whitePawn8.indexJOnLogicArray] = 1
                                switchTurn = True
                                whitePawn8.pos = wherePawnCanMove[x]
                                whitePawn8.firstMove = False
        
    
    elif turn == 'black':
        
        if whichPawn == 1:
            if wherePawnCanMove != [(0,0), (0,0), (0,0), (0,0)]:
                if blackPawn1.firstMove:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            blackPawn1.rect.x, blackPawn1.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if blackPawn1.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[blackPawn1.indexIOnLogicArray][blackPawn1.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                blackPawn1.indexIOnLogicArray, blackPawn1.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[blackPawn1.indexIOnLogicArray][blackPawn1.indexJOnLogicArray] = -1
                                switchTurn = True
                                blackPawn1.pos = wherePawnCanMove[x]
                                blackPawn1.firstMove = False
                else:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            blackPawn1.rect.x, blackPawn1.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if blackPawn1.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[blackPawn1.indexIOnLogicArray][blackPawn1.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                blackPawn1.indexIOnLogicArray, blackPawn1.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[blackPawn1.indexIOnLogicArray][blackPawn1.indexJOnLogicArray] = -1
                                switchTurn = True
                                blackPawn1.pos = wherePawnCanMove[x]
                                blackPawn1.firstMove = False
        
        if whichPawn == 2:
            if wherePawnCanMove != [(0,0), (0,0), (0,0), (0,0)]:
                if blackPawn2.firstMove:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            blackPawn2.rect.x, blackPawn2.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if blackPawn2.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[blackPawn2.indexIOnLogicArray][blackPawn2.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                blackPawn2.indexIOnLogicArray, blackPawn2.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[blackPawn2.indexIOnLogicArray][blackPawn2.indexJOnLogicArray] = -1
                                switchTurn = True
                                blackPawn2.pos = wherePawnCanMove[x]
                                blackPawn2.firstMove = False
                else:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            blackPawn2.rect.x, blackPawn2.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if blackPawn2.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[blackPawn2.indexIOnLogicArray][blackPawn2.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                blackPawn2.indexIOnLogicArray, blackPawn2.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[blackPawn2.indexIOnLogicArray][blackPawn2.indexJOnLogicArray] = -1
                                switchTurn = True
                                blackPawn2.pos = wherePawnCanMove[x]
                                blackPawn2.firstMove = False
        
        if whichPawn == 3:
            if wherePawnCanMove != [(0,0), (0,0), (0,0), (0,0)]:
                if blackPawn3.firstMove:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            blackPawn3.rect.x, blackPawn3.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if blackPawn3.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[blackPawn3.indexIOnLogicArray][blackPawn3.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                blackPawn3.indexIOnLogicArray, blackPawn3.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[blackPawn3.indexIOnLogicArray][blackPawn3.indexJOnLogicArray] = -1
                                switchTurn = True
                                blackPawn3.pos = wherePawnCanMove[x]
                                blackPawn3.firstMove = False
                else:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            blackPawn3.rect.x, blackPawn3.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if blackPawn3.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[blackPawn3.indexIOnLogicArray][blackPawn3.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                blackPawn3.indexIOnLogicArray, blackPawn3.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[blackPawn3.indexIOnLogicArray][blackPawn3.indexJOnLogicArray] = -1
                                switchTurn = True
                                blackPawn3.pos = wherePawnCanMove[x]
                                blackPawn3.firstMove = False
                                
        if whichPawn == 4:
            if wherePawnCanMove != [(0,0), (0,0), (0,0), (0,0)]:
                if blackPawn4.firstMove:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            blackPawn4.rect.x, blackPawn4.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if blackPawn4.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[blackPawn4.indexIOnLogicArray][blackPawn4.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                blackPawn4.indexIOnLogicArray, blackPawn4.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[blackPawn4.indexIOnLogicArray][blackPawn4.indexJOnLogicArray] = -1
                                switchTurn = True
                                blackPawn4.pos = wherePawnCanMove[x]
                                blackPawn4.firstMove = False
                else:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            blackPawn4.rect.x, blackPawn4.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if blackPawn4.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[blackPawn4.indexIOnLogicArray][blackPawn4.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                blackPawn4.indexIOnLogicArray, blackPawn4.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[blackPawn4.indexIOnLogicArray][blackPawn4.indexJOnLogicArray] = -1
                                switchTurn = True
                                blackPawn4.pos = wherePawnCanMove[x]
                                blackPawn4.firstMove = False
        
        if whichPawn == 5:
            if wherePawnCanMove != [(0,0), (0,0), (0,0), (0,0)]:
                if blackPawn5.firstMove:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            blackPawn5.rect.x, blackPawn5.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if blackPawn5.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[blackPawn5.indexIOnLogicArray][blackPawn5.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                blackPawn5.indexIOnLogicArray, blackPawn5.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[blackPawn5.indexIOnLogicArray][blackPawn5.indexJOnLogicArray] = -1
                                switchTurn = True
                                blackPawn5.pos = wherePawnCanMove[x]
                                blackPawn5.firstMove = False
                else:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            blackPawn5.rect.x, blackPawn5.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if blackPawn5.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[blackPawn5.indexIOnLogicArray][blackPawn5.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                blackPawn5.indexIOnLogicArray, blackPawn5.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[blackPawn5.indexIOnLogicArray][blackPawn5.indexJOnLogicArray] = -1
                                switchTurn = True
                                blackPawn5.pos = wherePawnCanMove[x]
                                blackPawn5.firstMove = False
        
        if whichPawn == 6:
            if wherePawnCanMove != [(0,0), (0,0), (0,0), (0,0)]:
                if blackPawn6.firstMove:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            blackPawn6.rect.x, blackPawn6.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if blackPawn6.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[blackPawn6.indexIOnLogicArray][blackPawn6.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                blackPawn6.indexIOnLogicArray, blackPawn6.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[blackPawn6.indexIOnLogicArray][blackPawn6.indexJOnLogicArray] = -1
                                switchTurn = True
                                blackPawn6.pos = wherePawnCanMove[x]
                                blackPawn6.firstMove = False
                else:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            blackPawn6.rect.x, blackPawn6.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if blackPawn6.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[blackPawn6.indexIOnLogicArray][blackPawn6.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                blackPawn6.indexIOnLogicArray, blackPawn6.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[blackPawn6.indexIOnLogicArray][blackPawn6.indexJOnLogicArray] = -1
                                switchTurn = True
                                blackPawn6.pos = wherePawnCanMove[x]
                                blackPawn6.firstMove = False
        
        if whichPawn == 7:
            if wherePawnCanMove != [(0,0), (0,0), (0,0), (0,0)]:
                if blackPawn7.firstMove:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            blackPawn7.rect.x, blackPawn7.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if blackPawn7.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[blackPawn7.indexIOnLogicArray][blackPawn7.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                blackPawn7.indexIOnLogicArray, blackPawn7.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[blackPawn7.indexIOnLogicArray][blackPawn7.indexJOnLogicArray] = -1
                                switchTurn = True
                                blackPawn7.pos = wherePawnCanMove[x]
                                blackPawn7.firstMove = False
                else:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            blackPawn7.rect.x, blackPawn7.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if blackPawn7.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[blackPawn7.indexIOnLogicArray][blackPawn7.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                blackPawn7.indexIOnLogicArray, blackPawn7.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[blackPawn7.indexIOnLogicArray][blackPawn7.indexJOnLogicArray] = -1
                                switchTurn = True
                                blackPawn7.pos = wherePawnCanMove[x]
                                blackPawn7.firstMove = False
        
        if whichPawn == 8:
            if wherePawnCanMove != [(0,0), (0,0), (0,0), (0,0)]:
                if blackPawn8.firstMove:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            blackPawn8.rect.x, blackPawn8.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if blackPawn8.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[blackPawn8.indexIOnLogicArray][blackPawn8.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                blackPawn8.indexIOnLogicArray, blackPawn8.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[blackPawn8.indexIOnLogicArray][blackPawn8.indexJOnLogicArray] = -1
                                switchTurn = True
                                blackPawn8.pos = wherePawnCanMove[x]
                                blackPawn8.firstMove = False
                else:
                    for x in range(0,4):
                        
                        tileLetter, tileNumber = wherePawnCanMove[x]
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            blackPawn8.rect.x, blackPawn8.rect.y = whereMouseIs
                            CenterPawnInTile(turn, whichPawn)
                            PiecesCollide(turn)
                            
                            if blackPawn8.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[blackPawn8.indexIOnLogicArray][blackPawn8.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                blackPawn8.indexIOnLogicArray, blackPawn8.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[blackPawn8.indexIOnLogicArray][blackPawn8.indexJOnLogicArray] = -1
                                switchTurn = True
                                blackPawn8.pos = wherePawnCanMove[x]
                                blackPawn8.firstMove = False

def CenterPawnInTile(turn, whichPawn):
    # Takes an offcentered pawn and centers it after movement to make the board look less clustered
    if turn == 'white':
        if whichPawn == 1:
            if whitePawn1.rect.collidelist(collisionList) == -1:
                return False
            else:
                whitePawn1.rect.center = collisionList[whitePawn1.rect.collidelist(collisionList)].center 
        elif whichPawn == 2:
            if whitePawn2.rect.collidelist(collisionList) == -1:
                return False
            else:
                whitePawn2.rect.center = collisionList[whitePawn2.rect.collidelist(collisionList)].center 
        elif whichPawn == 3:
            if whitePawn3.rect.collidelist(collisionList) == -1:
                return False
            else:
                whitePawn3.rect.center = collisionList[whitePawn3.rect.collidelist(collisionList)].center 
        elif whichPawn == 4:
            if whitePawn4.rect.collidelist(collisionList) == -1:
                return False
            else:
                whitePawn4.rect.center = collisionList[whitePawn4.rect.collidelist(collisionList)].center 
        elif whichPawn == 5:
            if whitePawn5.rect.collidelist(collisionList) == -1:
                return False
            else:
                whitePawn5.rect.center = collisionList[whitePawn5.rect.collidelist(collisionList)].center 
        elif whichPawn == 6:
            if whitePawn6.rect.collidelist(collisionList) == -1:
                return False
            else:
                whitePawn6.rect.center = collisionList[whitePawn6.rect.collidelist(collisionList)].center 
        elif whichPawn == 7:
            if whitePawn7.rect.collidelist(collisionList) == -1:
                return False
            else:
                whitePawn7.rect.center = collisionList[whitePawn7.rect.collidelist(collisionList)].center 
        elif whichPawn == 8:
            if whitePawn8.rect.collidelist(collisionList) == -1:
                return False
            else:
                whitePawn8.rect.center = collisionList[whitePawn8.rect.collidelist(collisionList)].center 
    elif turn == 'black':
        if whichPawn == 1:
            if blackPawn1.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackPawn1.rect.center = collisionList[blackPawn1.rect.collidelist(collisionList)].center 
        elif whichPawn == 2:
            if blackPawn2.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackPawn2.rect.center = collisionList[blackPawn2.rect.collidelist(collisionList)].center 
        elif whichPawn == 3:
            if blackPawn3.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackPawn3.rect.center = collisionList[blackPawn3.rect.collidelist(collisionList)].center 
        elif whichPawn == 4:
            if blackPawn4.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackPawn4.rect.center = collisionList[blackPawn4.rect.collidelist(collisionList)].center 
        elif whichPawn == 5:
            if blackPawn5.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackPawn5.rect.center = collisionList[blackPawn5.rect.collidelist(collisionList)].center 
        elif whichPawn == 6:
            if blackPawn6.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackPawn6.rect.center = collisionList[blackPawn6.rect.collidelist(collisionList)].center 
        elif whichPawn == 7:
            if blackPawn7.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackPawn7.rect.center = collisionList[blackPawn7.rect.collidelist(collisionList)].center 
        elif whichPawn == 8:
            if blackPawn8.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackPawn8.rect.center = collisionList[blackPawn8.rect.collidelist(collisionList)].center 
  
def PawnCollidesWithPromotionZone(turn, whichPawn):
    blackPromotionZone = [blackA1, whiteB1, blackC1, whiteD1, blackE1, whiteF1, blackG1, whiteH1]
    whitePromotionZone = [whiteA8, blackB8, whiteC8, blackD8, whiteE8, blackF8, whiteG8, blackH8]
    # If a pawn reaches it's promotion zone this method returns true so the promotion can begin
    if turn == 'white':
        if whichPawn == 1:
            if whitePawn1.rect.collidelist(whitePromotionZone) == -1:
                return False
            else:
                return True
        elif whichPawn == 2:
            if whitePawn2.rect.collidelist(whitePromotionZone) == -1:
                return False
            else:
                return True
        elif whichPawn == 3:
            if whitePawn3.rect.collidelist(whitePromotionZone) == -1:
                return False
            else:
                return True
        elif whichPawn == 4:
            if whitePawn4.rect.collidelist(whitePromotionZone) == -1:
                return False
            else:
                return True
        elif whichPawn == 5:
            if whitePawn5.rect.collidelist(whitePromotionZone) == -1:
                return False
            else:
                return True
        elif whichPawn == 6:
            if whitePawn6.rect.collidelist(whitePromotionZone) == -1:
                return False
            else:
                return True
        elif whichPawn == 7:
            if whitePawn7.rect.collidelist(whitePromotionZone) == -1:
                return False
            else:
                return True
        elif whichPawn == 8:
            if whitePawn8.rect.collidelist(whitePromotionZone) == -1:
                return False
            else:
                return True
    
    elif turn == 'black':
        if whichPawn == 1:
            if blackPawn1.rect.collidelist(blackPromotionZone) == -1:
                return False
            else:
                return True
        elif whichPawn == 2:
            if blackPawn2.rect.collidelist(blackPromotionZone) == -1:
                return False
            else:
                return True
        elif whichPawn == 3:
            if blackPawn3.rect.collidelist(blackPromotionZone) == -1:
                return False
            else:
                return True
        elif whichPawn == 4:
            if blackPawn4.rect.collidelist(blackPromotionZone) == -1:
                return False
            else:
                return True
        elif whichPawn == 5:
            if blackPawn5.rect.collidelist(blackPromotionZone) == -1:
                return False
            else:
                return True
        elif whichPawn == 6:
            if blackPawn6.rect.collidelist(blackPromotionZone) == -1:
                return False
            else:
                return True
        elif whichPawn == 7:
            if blackPawn7.rect.collidelist(blackPromotionZone) == -1:
                return False
            else:
                return True
        elif whichPawn == 8:
            if blackPawn8.rect.collidelist(blackPromotionZone) == -1:
                return False
            else:
                return True

def PawnPromotion(turn, whichPawn):
    # When a pawn is in the promotion zone it is promoted to a queen
    whitePromotionCounter = 0
    blackPromotionCounter = 0
    if turn == 'white':
        if whichPawn == 1:
            
            # Set position of queen
            whiteQueen1.pos = whitePawn1.pos 
            rectLogicArray[whitePawn1.indexIOnLogicArray][whitePawn1.indexJOnLogicArray] = 5 
            whiteQueen1.indexIOnLogicArray, whiteQueen1.indexJOnLogicArray = whitePawn1.indexIOnLogicArray, whitePawn1.indexJOnLogicArray
            whiteQueen1.rect.center = whitePawn1.rect.center
            whiteQueen1.onBoard = True
            
            whitePromotionCounter +=1
            
            # Get rid of the previous pawn's positions
            whitePawn1.rect.x, whitePawn1.rect.y = 500, 1500+(60*whitePromotionCounter)
            whitePawn1.pos =  (500,10+(60*whitePromotionCounter))
            whitePawn1.indexIOnLogicArray, whitePawn1.indexJOnLogicArray = 0,0
            
        if whichPawn == 2:
            
            whiteQueen2.pos = whitePawn2.pos
            rectLogicArray[whitePawn2.indexIOnLogicArray][whitePawn2.indexJOnLogicArray] = 5
            whiteQueen2.indexIOnLogicArray, whiteQueen2.indexJOnLogicArray = whitePawn2.indexIOnLogicArray, whitePawn2.indexJOnLogicArray
            
            
            whiteQueen2.rect.center = whitePawn2.rect.center
            whiteQueen2.onBoard = True
            
            
            whitePromotionCounter +=1
            
            whitePawn2.rect.x, whitePawn2.rect.y = 500, 1500+(60*whitePromotionCounter)
            whitePawn2.pos =  (500,10+(60*whitePromotionCounter))
            whitePawn2.indexIOnLogicArray, whitePawn2.indexJOnLogicArray = 0,0
        
        if whichPawn == 3:
            
            whiteQueen3.pos = whitePawn3.pos
            rectLogicArray[whitePawn3.indexIOnLogicArray][whitePawn3.indexJOnLogicArray] = 5
            whiteQueen3.indexIOnLogicArray, whiteQueen3.indexJOnLogicArray = whitePawn3.indexIOnLogicArray, whitePawn3.indexJOnLogicArray
            
            
            whiteQueen3.rect.center = whitePawn3.rect.center
            whiteQueen3.onBoard = True
            
            
            whitePromotionCounter +=1
            
            whitePawn3.rect.x, whitePawn3.rect.y = 500, 1500+(60*whitePromotionCounter)
            whitePawn3.pos =  (500,10+(60*whitePromotionCounter))
            whitePawn3.indexIOnLogicArray, whitePawn3.indexJOnLogicArray = 0,0
        
        if whichPawn == 4:
            
            whiteQueen4.pos = whitePawn4.pos
            rectLogicArray[whitePawn4.indexIOnLogicArray][whitePawn4.indexJOnLogicArray] = 5
            whiteQueen4.indexIOnLogicArray, whiteQueen4.indexJOnLogicArray = whitePawn4.indexIOnLogicArray, whitePawn4.indexJOnLogicArray
            
            
            whiteQueen4.rect.center = whitePawn4.rect.center
            whiteQueen4.onBoard = True
            
            
            whitePromotionCounter +=1
            
            whitePawn4.rect.x, whitePawn4.rect.y = 500, 1500+(60*whitePromotionCounter)
            whitePawn4.pos =  (500,10+(60*whitePromotionCounter))
            whitePawn4.indexIOnLogicArray, whitePawn4.indexJOnLogicArray = 0,0
        
        if whichPawn == 5:
            
            whiteQueen5.pos = whitePawn5.pos
            rectLogicArray[whitePawn5.indexIOnLogicArray][whitePawn5.indexJOnLogicArray] = 5
            whiteQueen5.indexIOnLogicArray, whiteQueen5.indexJOnLogicArray = whitePawn5.indexIOnLogicArray, whitePawn5.indexJOnLogicArray
            
            
            whiteQueen5.rect.center = whitePawn5.rect.center
            whiteQueen5.onBoard = True
            
            
            whitePromotionCounter +=1
            
            whitePawn5.rect.x, whitePawn5.rect.y = 500, 1500+(60*whitePromotionCounter)
            whitePawn5.pos =  (500,10+(60*whitePromotionCounter))
            whitePawn5.indexIOnLogicArray, whitePawn5.indexJOnLogicArray = 0,0
        
        if whichPawn == 6:
            
            whiteQueen6.pos = whitePawn6.pos
            rectLogicArray[whitePawn6.indexIOnLogicArray][whitePawn6.indexJOnLogicArray] = 5
            whiteQueen6.indexIOnLogicArray, whiteQueen6.indexJOnLogicArray = whitePawn6.indexIOnLogicArray, whitePawn6.indexJOnLogicArray
            
            
            whiteQueen6.rect.center = whitePawn6.rect.center
            whiteQueen6.onBoard = True
            
            
            whitePromotionCounter +=1
            
            whitePawn6.rect.x, whitePawn6.rect.y = 500, 1500+(60*whitePromotionCounter)
            whitePawn6.pos =  (500,10+(60*whitePromotionCounter))
            whitePawn6.indexIOnLogicArray, whitePawn6.indexJOnLogicArray = 0,0
        
        if whichPawn == 7:
            
            whiteQueen7.pos = whitePawn7.pos
            rectLogicArray[whitePawn7.indexIOnLogicArray][whitePawn7.indexJOnLogicArray] = 5
            whiteQueen7.indexIOnLogicArray, whiteQueen7.indexJOnLogicArray = whitePawn7.indexIOnLogicArray, whitePawn7.indexJOnLogicArray
            
            
            whiteQueen7.rect.center = whitePawn7.rect.center
            whiteQueen7.onBoard = True
            
            
            whitePromotionCounter +=1
            
            whitePawn7.rect.x, whitePawn7.rect.y = 500, 1500+(60*whitePromotionCounter)
            whitePawn7.pos =  (500,10+(60*whitePromotionCounter))
            whitePawn7.indexIOnLogicArray, whitePawn7.indexJOnLogicArray = 0,0
        
        if whichPawn == 8:
            
            whiteQueen8.pos = whitePawn8.pos
            rectLogicArray[whitePawn8.indexIOnLogicArray][whitePawn8.indexJOnLogicArray] = 5
            whiteQueen8.indexIOnLogicArray, whiteQueen8.indexJOnLogicArray = whitePawn8.indexIOnLogicArray, whitePawn8.indexJOnLogicArray
            
            
            whiteQueen8.rect.center = whitePawn8.rect.center
            whiteQueen8.onBoard = True
            
            
            whitePromotionCounter +=1
            
            whitePawn8.rect.x, whitePawn8.rect.y = 500, 1500+(60*whitePromotionCounter)
            whitePawn8.pos =  (500,10+(60*whitePromotionCounter))
            whitePawn8.indexIOnLogicArray, whitePawn8.indexJOnLogicArray = 0,0
    
    elif turn == 'black':
        if whichPawn == 1:
            
            # Set position of queen
            blackQueen1.pos = blackPawn1.pos 
            rectLogicArray[blackPawn1.indexIOnLogicArray][blackPawn1.indexJOnLogicArray] = 5 
            blackQueen1.indexIOnLogicArray, blackQueen1.indexJOnLogicArray = blackPawn1.indexIOnLogicArray, blackPawn1.indexJOnLogicArray
            blackQueen1.rect.center = blackPawn1.rect.center
            blackQueen1.onBoard = True
            
            blackPromotionCounter +=1
            
            # Get rid of all pawn positions
            blackPawn1.rect.x, blackPawn1.rect.y = 500, 1500+(60*blackPromotionCounter)
            blackPawn1.pos =  (500,10+(60*blackPromotionCounter))
            blackPawn1.indexIOnLogicArray, blackPawn1.indexJOnLogicArray = 0,0
            
        if whichPawn == 2:
            
            blackQueen2.pos = blackPawn2.pos
            rectLogicArray[blackPawn2.indexIOnLogicArray][blackPawn2.indexJOnLogicArray] = 5
            blackQueen2.indexIOnLogicArray, blackQueen2.indexJOnLogicArray = blackPawn2.indexIOnLogicArray, blackPawn2.indexJOnLogicArray
            
            
            blackQueen2.rect.center = blackPawn2.rect.center
            blackQueen2.onBoard = True
            
            
            blackPromotionCounter +=1
            
            blackPawn2.rect.x, blackPawn2.rect.y = 500, 1500+(60*blackPromotionCounter)
            blackPawn2.pos =  (500,10+(60*blackPromotionCounter))
            blackPawn2.indexIOnLogicArray, blackPawn2.indexJOnLogicArray = 0,0
        
        if whichPawn == 3:
            
            blackQueen3.pos = blackPawn3.pos
            rectLogicArray[blackPawn3.indexIOnLogicArray][blackPawn3.indexJOnLogicArray] = 5
            blackQueen3.indexIOnLogicArray, blackQueen3.indexJOnLogicArray = blackPawn3.indexIOnLogicArray, blackPawn3.indexJOnLogicArray
            
            
            blackQueen3.rect.center = blackPawn3.rect.center
            blackQueen3.onBoard = True
            
            
            blackPromotionCounter +=1
            
            blackPawn3.rect.x, blackPawn3.rect.y = 500, 1500+(60*blackPromotionCounter)
            blackPawn3.pos =  (500,10+(60*blackPromotionCounter))
            blackPawn3.indexIOnLogicArray, blackPawn3.indexJOnLogicArray = 0,0
        
        if whichPawn == 4:
            
            blackQueen4.pos = blackPawn4.pos
            rectLogicArray[blackPawn4.indexIOnLogicArray][blackPawn4.indexJOnLogicArray] = 5
            blackQueen4.indexIOnLogicArray, blackQueen4.indexJOnLogicArray = blackPawn4.indexIOnLogicArray, blackPawn4.indexJOnLogicArray
            
            
            blackQueen4.rect.center = blackPawn4.rect.center
            blackQueen4.onBoard = True
            
            
            blackPromotionCounter +=1
            
            blackPawn4.rect.x, blackPawn4.rect.y = 500, 1500+(60*blackPromotionCounter)
            blackPawn4.pos =  (500,10+(60*blackPromotionCounter))
            blackPawn4.indexIOnLogicArray, blackPawn4.indexJOnLogicArray = 0,0
        
        if whichPawn == 5:
            
            blackQueen5.pos = blackPawn5.pos
            rectLogicArray[blackPawn5.indexIOnLogicArray][blackPawn5.indexJOnLogicArray] = 5
            blackQueen5.indexIOnLogicArray, blackQueen5.indexJOnLogicArray = blackPawn5.indexIOnLogicArray, blackPawn5.indexJOnLogicArray
            
            
            blackQueen5.rect.center = blackPawn5.rect.center
            blackQueen5.onBoard = True
            
            
            blackPromotionCounter +=1
            
            blackPawn5.rect.x, blackPawn5.rect.y = 500, 1500+(60*blackPromotionCounter)
            blackPawn5.pos =  (500,10+(60*blackPromotionCounter))
            blackPawn5.indexIOnLogicArray, blackPawn5.indexJOnLogicArray = 0,0
        
        if whichPawn == 6:
            
            blackQueen6.pos = blackPawn6.pos
            rectLogicArray[blackPawn6.indexIOnLogicArray][blackPawn6.indexJOnLogicArray] = 5
            blackQueen6.indexIOnLogicArray, blackQueen6.indexJOnLogicArray = blackPawn6.indexIOnLogicArray, blackPawn6.indexJOnLogicArray
            
            
            blackQueen6.rect.center = blackPawn6.rect.center
            blackQueen6.onBoard = True
            
            
            blackPromotionCounter +=1
            
            blackPawn6.rect.x, blackPawn6.rect.y = 500, 1500+(60*blackPromotionCounter)
            blackPawn6.pos =  (500,10+(60*blackPromotionCounter))
            blackPawn6.indexIOnLogicArray, blackPawn6.indexJOnLogicArray = 0,0
        
        if whichPawn == 7:
            
            blackQueen7.pos = blackPawn7.pos
            rectLogicArray[blackPawn7.indexIOnLogicArray][blackPawn7.indexJOnLogicArray] = 5
            blackQueen7.indexIOnLogicArray, blackQueen7.indexJOnLogicArray = blackPawn7.indexIOnLogicArray, blackPawn7.indexJOnLogicArray
            
            
            blackQueen7.rect.center = blackPawn7.rect.center
            blackQueen7.onBoard = True
            
            
            blackPromotionCounter +=1
            
            blackPawn7.rect.x, blackPawn7.rect.y = 500, 1500+(60*blackPromotionCounter)
            blackPawn7.pos =  (500,10+(60*blackPromotionCounter))
            blackPawn7.indexIOnLogicArray, blackPawn7.indexJOnLogicArray = 0,0
        
        if whichPawn == 8:
            
            blackQueen8.pos = blackPawn8.pos
            rectLogicArray[blackPawn8.indexIOnLogicArray][blackPawn8.indexJOnLogicArray] = 5
            blackQueen8.indexIOnLogicArray, blackQueen8.indexJOnLogicArray = blackPawn8.indexIOnLogicArray, blackPawn8.indexJOnLogicArray
            
            
            blackQueen8.rect.center = blackPawn8.rect.center
            blackQueen8.onBoard = True
            
            
            blackPromotionCounter +=1
            
            blackPawn8.rect.x, blackPawn8.rect.y = 500, 1500+(60*blackPromotionCounter)
            blackPawn8.pos =  (500,10+(60*blackPromotionCounter))
            blackPawn8.indexIOnLogicArray, blackPawn8.indexJOnLogicArray = 0,0
        
def CreatePromotedQueens():
    global whiteQueen1, whiteQueen2, whiteQueen3, whiteQueen4, whiteQueen5, whiteQueen6, whiteQueen7, whiteQueen8, blackQueen1, blackQueen2, blackQueen3, blackQueen4, blackQueen5, blackQueen6, blackQueen7, blackQueen8
    
    # Setting all queens to the same pos and indexs for logic array whilst they are not on the board, to be changed when promotion occurs
    
    whiteQueen1 = chessPieces.Queen("white", (0,0), 10, 10, False)
    whiteQueen2 = chessPieces.Queen("white", (0,0), 10, 10, False)
    whiteQueen3 = chessPieces.Queen("white", (0,0), 10, 10, False)
    whiteQueen4 = chessPieces.Queen("white", (0,0), 10, 10, False)
    whiteQueen5 = chessPieces.Queen("white", (0,0), 10, 10, False)
    whiteQueen6 = chessPieces.Queen("white", (0,0), 10, 10, False)
    whiteQueen7 = chessPieces.Queen("white", (0,0), 10, 10, False)
    whiteQueen8 = chessPieces.Queen("white", (0,0), 10, 10, False)
    
    blackQueen1 = chessPieces.Queen("black", (0,0), 10, 10, False)
    blackQueen2 = chessPieces.Queen("black", (0,0), 10, 10, False)
    blackQueen3 = chessPieces.Queen("black", (0,0), 10, 10, False)
    blackQueen4 = chessPieces.Queen("black", (0,0), 10, 10, False)
    blackQueen5 = chessPieces.Queen("black", (0,0), 10, 10, False)
    blackQueen6 = chessPieces.Queen("black", (0,0), 10, 10, False)
    blackQueen7 = chessPieces.Queen("black", (0,0), 10, 10, False)
    blackQueen8 = chessPieces.Queen("black", (0,0), 10, 10, False)

def PutPromotedQueensOnTheBoard():
    
    screen.blit(whiteQueen1.surface, whiteQueen1.rect)
    screen.blit(whiteQueen2.surface, whiteQueen2.rect)
    screen.blit(whiteQueen3.surface, whiteQueen3.rect)
    screen.blit(whiteQueen4.surface, whiteQueen4.rect)
    screen.blit(whiteQueen5.surface, whiteQueen5.rect)
    screen.blit(whiteQueen6.surface, whiteQueen6.rect)
    screen.blit(whiteQueen7.surface, whiteQueen7.rect)
    screen.blit(whiteQueen8.surface, whiteQueen8.rect)
    
    screen.blit(blackQueen1.surface, blackQueen1.rect)
    screen.blit(blackQueen2.surface, blackQueen2.rect)
    screen.blit(blackQueen3.surface, blackQueen3.rect)
    screen.blit(blackQueen4.surface, blackQueen4.rect)
    screen.blit(blackQueen5.surface, blackQueen5.rect)
    screen.blit(blackQueen6.surface, blackQueen6.rect)
    screen.blit(blackQueen7.surface, blackQueen7.rect)
    screen.blit(blackQueen8.surface, blackQueen8.rect)

# Castle methods
            
def CreateWhiteCastles():
    global whiteCastle1, whiteCastle2
    
    # Creates 2 castle objects
    # Initialised with their starting position and their position on the logic array
    whiteCastle1 = chessPieces.Castle("white", ("a", 1), 7, 0, True)
    whiteCastle2 =  chessPieces.Castle("white", ("h", 1), 7, 7, True)
    
def CreateBlackCastles():
    global blackCastle1, blackCastle2
    
    # Creates 2 castle objects
    # Initialised with their starting position and their position on the logic array
    blackCastle1 = chessPieces.Castle("black", ("a", 8), 0, 0, True)
    blackCastle2 =  chessPieces.Castle("black", ("h", 8), 0, 7, True)
    
def PutAllCastlesOnTheBoard():
    
    # Ties the castles surfaces and rects together and then puts them on the screen
    screen.blit(blackCastle1.surface, blackCastle1.rect)
    screen.blit(blackCastle2.surface, blackCastle2.rect)
    
    screen.blit(whiteCastle1.surface, whiteCastle1.rect)
    screen.blit(whiteCastle2.surface, whiteCastle2.rect)
    
def CollidingWithACastle(turn, whereMouseIs):
    # Detects if a castle is colliding with where the mouse is so they can be selected to move 
    if turn == "white":
        if whiteCastle1.rect.collidepoint(whereMouseIs) or whiteCastle2.rect.collidepoint(whereMouseIs):
            return True
        else:
            return False
    elif turn == "black":
        if blackCastle1.rect.collidepoint(whereMouseIs) or blackCastle2.rect.collidepoint(whereMouseIs):     
            return True
        else:
            return False

def WhichCastleIsCollidedWith(turn, whereMouseIs):
    # Detects which castle is being clicked
    if turn == 'white':
        if whiteCastle1.rect.collidepoint(whereMouseIs):
            return 1
        elif whiteCastle2.rect.collidepoint(whereMouseIs):
            return 2
    elif turn == 'black':
        if blackCastle1.rect.collidepoint(whereMouseIs):
            return 1
        elif blackCastle2.rect.collidepoint(whereMouseIs):
            return 2

def CenterCastleInTile(turn, whichCastle):
    # Centers a piece in the tile they are currently on to reduce clustering
    if turn == 'white':
        if whichCastle == 1:
            if whiteCastle1.rect.collidelist(collisionList) == -1:
                return False
            else:
                whiteCastle1.rect.center = collisionList[whiteCastle1.rect.collidelist(collisionList)].center 
        elif whichCastle == 2:
            if whiteCastle2.rect.collidelist(collisionList) == -1:
                return False
            else:
                whiteCastle2.rect.center = collisionList[whiteCastle2.rect.collidelist(collisionList)].center
    elif turn == 'black':
        if whichCastle == 1:
            if blackCastle1.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackCastle1.rect.center = collisionList[blackCastle1.rect.collidelist(collisionList)].center 
        elif whichCastle == 2:
            if blackCastle2.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackCastle2.rect.center = collisionList[blackCastle2.rect.collidelist(collisionList)].center
    
def WhereCanCastleMove(turn, whichCastle, isACastle):
    # 7 is the most amount of moves a castle can move in one direction at any time, with 4 directional possibilites
    # Therefore a list with 28 spaces is made
    
    # Organised with North or up being the first direction and then going through in a clockwise fashion with last direction being West or left
    twentyEightMoves = [(0,0) for x in range(0,29)]
    
    if isACastle: # If it is a castle as opposed to queen
        if turn == 'white':
            
            if whichCastle == 1:
                if whiteCastle1.onBoard:
                    # Up direction
                    for x in range(1,8):
                        if whiteCastle1.indexIOnLogicArray - x  >= 0: # Ensures the index does not exceed the range of the logic array
                                # If there is nothing blocking the castles way then add it to potential moves
                            if rectLogicArray[whiteCastle1.indexIOnLogicArray - x][whiteCastle1.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteCastle1.indexIOnLogicArray - x, whiteCastle1.indexJOnLogicArray) 
                                # If it detects a piece of the opposite colour, add it to the potential moves and then stop
                                # So it does not add moves that are past the point of the opposite piece
                            elif rectLogicArray[whiteCastle1.indexIOnLogicArray - x][whiteCastle1.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteCastle1.indexIOnLogicArray - x, whiteCastle1.indexJOnLogicArray)
                                break
                                # If the position has a piece of the same colour stop as only knights can jump same coloured pieces
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if whiteCastle1.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteCastle1.indexIOnLogicArray][whiteCastle1.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteCastle1.indexIOnLogicArray, whiteCastle1.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteCastle1.indexIOnLogicArray][whiteCastle1.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteCastle1.indexIOnLogicArray, whiteCastle1.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if whiteCastle1.indexIOnLogicArray + x < 8:
                            if rectLogicArray[whiteCastle1.indexIOnLogicArray + x][whiteCastle1.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteCastle1.indexIOnLogicArray + x, whiteCastle1.indexJOnLogicArray)
                            elif rectLogicArray[whiteCastle1.indexIOnLogicArray + x][whiteCastle1.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteCastle1.indexIOnLogicArray + x, whiteCastle1.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if whiteCastle1.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteCastle1.indexIOnLogicArray][whiteCastle1.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteCastle1.indexIOnLogicArray, whiteCastle1.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteCastle1.indexIOnLogicArray][whiteCastle1.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteCastle1.indexIOnLogicArray, whiteCastle1.indexJOnLogicArray - x)
                                break
                            else:
                                break
                            
                    return twentyEightMoves
                
            elif whichCastle == 2:
                if whiteCastle2.onBoard:
                    # Up direction
                    for x in range(1,8):
                        if whiteCastle2.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[whiteCastle2.indexIOnLogicArray - x][whiteCastle2.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteCastle2.indexIOnLogicArray - x, whiteCastle2.indexJOnLogicArray)
                            elif rectLogicArray[whiteCastle2.indexIOnLogicArray - x][whiteCastle2.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteCastle2.indexIOnLogicArray - x, whiteCastle2.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if whiteCastle2.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteCastle2.indexIOnLogicArray][whiteCastle2.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteCastle2.indexIOnLogicArray, whiteCastle2.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteCastle2.indexIOnLogicArray][whiteCastle2.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteCastle2.indexIOnLogicArray, whiteCastle2.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if whiteCastle2.indexIOnLogicArray + x < 8:
                            if rectLogicArray[whiteCastle2.indexIOnLogicArray + x][whiteCastle2.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteCastle2.indexIOnLogicArray + x, whiteCastle2.indexJOnLogicArray)
                            elif rectLogicArray[whiteCastle2.indexIOnLogicArray + x][whiteCastle2.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteCastle2.indexIOnLogicArray + x, whiteCastle2.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if whiteCastle2.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteCastle2.indexIOnLogicArray][whiteCastle2.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteCastle2.indexIOnLogicArray, whiteCastle2.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteCastle2.indexIOnLogicArray][whiteCastle2.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteCastle2.indexIOnLogicArray, whiteCastle2.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
        elif turn == 'black':
            
            if whichCastle == 1:
                if blackCastle1.onBoard:
                    # Up direction
                    for x in range(1,8):
                        if blackCastle1.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[blackCastle1.indexIOnLogicArray - x][blackCastle1.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackCastle1.indexIOnLogicArray - x, blackCastle1.indexJOnLogicArray)
                            elif rectLogicArray[blackCastle1.indexIOnLogicArray - x][blackCastle1.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackCastle1.indexIOnLogicArray - x, blackCastle1.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if blackCastle1.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackCastle1.indexIOnLogicArray][blackCastle1.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackCastle1.indexIOnLogicArray, blackCastle1.indexJOnLogicArray + x)
                            elif rectLogicArray[blackCastle1.indexIOnLogicArray][blackCastle1.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackCastle1.indexIOnLogicArray, blackCastle1.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if blackCastle1.indexIOnLogicArray + x < 8:
                            if rectLogicArray[blackCastle1.indexIOnLogicArray + x][blackCastle1.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackCastle1.indexIOnLogicArray + x, blackCastle1.indexJOnLogicArray)
                            elif rectLogicArray[blackCastle1.indexIOnLogicArray + x][blackCastle1.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackCastle1.indexIOnLogicArray + x, blackCastle1.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if blackCastle1.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackCastle1.indexIOnLogicArray][blackCastle1.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackCastle1.indexIOnLogicArray, blackCastle1.indexJOnLogicArray - x)
                            elif rectLogicArray[blackCastle1.indexIOnLogicArray][blackCastle1.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackCastle1.indexIOnLogicArray, blackCastle1.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichCastle == 2:
                if blackCastle2.onBoard:
                    # Up direction
                    for x in range(1,8):
                        if blackCastle2.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[blackCastle2.indexIOnLogicArray - x][blackCastle2.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackCastle2.indexIOnLogicArray - x, blackCastle2.indexJOnLogicArray)
                            elif rectLogicArray[blackCastle2.indexIOnLogicArray - x][blackCastle2.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackCastle2.indexIOnLogicArray - x, blackCastle2.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if blackCastle2.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackCastle2.indexIOnLogicArray][blackCastle2.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackCastle2.indexIOnLogicArray, blackCastle2.indexJOnLogicArray + x)
                            elif rectLogicArray[blackCastle2.indexIOnLogicArray][blackCastle2.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackCastle2.indexIOnLogicArray, blackCastle2.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if blackCastle2.indexIOnLogicArray + x < 8:
                            if rectLogicArray[blackCastle2.indexIOnLogicArray + x][blackCastle2.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackCastle2.indexIOnLogicArray + x, blackCastle2.indexJOnLogicArray)
                            elif rectLogicArray[blackCastle2.indexIOnLogicArray + x][blackCastle2.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackCastle2.indexIOnLogicArray + x, blackCastle2.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if blackCastle2.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackCastle2.indexIOnLogicArray][blackCastle2.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackCastle2.indexIOnLogicArray, blackCastle2.indexJOnLogicArray - x)
                            elif rectLogicArray[blackCastle2.indexIOnLogicArray][blackCastle2.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackCastle2.indexIOnLogicArray, blackCastle2.indexJOnLogicArray - x)
                                break
                            else:
                                break
                            
                    return twentyEightMoves
    else: # In the case it is not a castle it is a queen, as the queen follows similiar linear movement logic
        if turn == 'white':
            if whichCastle == 1:
                if whiteQueen1.onBoard:
                
                    # Up direction
                    for x in range(1,8):
                        if whiteQueen1.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[whiteQueen1.indexIOnLogicArray - x][whiteQueen1.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen1.indexIOnLogicArray - x, whiteQueen1.indexJOnLogicArray)
                            elif rectLogicArray[whiteQueen1.indexIOnLogicArray - x][whiteQueen1.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen1.indexIOnLogicArray - x, whiteQueen1.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if whiteQueen1.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen1.indexIOnLogicArray][whiteQueen1.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen1.indexIOnLogicArray, whiteQueen1.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen1.indexIOnLogicArray][whiteQueen1.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen1.indexIOnLogicArray, whiteQueen1.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if whiteQueen1.indexIOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen1.indexIOnLogicArray + x][whiteQueen1.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen1.indexIOnLogicArray + x, whiteQueen1.indexJOnLogicArray)
                            elif rectLogicArray[whiteQueen1.indexIOnLogicArray + x][whiteQueen1.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen1.indexIOnLogicArray + x, whiteQueen1.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if whiteQueen1.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen1.indexIOnLogicArray][whiteQueen1.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen1.indexIOnLogicArray, whiteQueen1.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen1.indexIOnLogicArray][whiteQueen1.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen1.indexIOnLogicArray, whiteQueen1.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichCastle == 2:
                if whiteQueen2.onBoard:
                
                    # Up direction
                    for x in range(1,8):
                        if whiteQueen2.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[whiteQueen2.indexIOnLogicArray - x][whiteQueen2.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen2.indexIOnLogicArray - x, whiteQueen2.indexJOnLogicArray)
                            elif rectLogicArray[whiteQueen2.indexIOnLogicArray - x][whiteQueen2.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen2.indexIOnLogicArray - x, whiteQueen2.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if whiteQueen2.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen2.indexIOnLogicArray][whiteQueen2.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen2.indexIOnLogicArray, whiteQueen2.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen2.indexIOnLogicArray][whiteQueen2.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen2.indexIOnLogicArray, whiteQueen2.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if whiteQueen2.indexIOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen2.indexIOnLogicArray + x][whiteQueen2.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen2.indexIOnLogicArray + x, whiteQueen2.indexJOnLogicArray)
                            elif rectLogicArray[whiteQueen2.indexIOnLogicArray + x][whiteQueen2.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen2.indexIOnLogicArray + x, whiteQueen2.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if whiteQueen2.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen2.indexIOnLogicArray][whiteQueen2.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen2.indexIOnLogicArray, whiteQueen2.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen2.indexIOnLogicArray][whiteQueen2.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen2.indexIOnLogicArray, whiteQueen2.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichCastle == 3:
                if whiteQueen3.onBoard:
                
                    # Up direction
                    for x in range(1,8):
                        if whiteQueen3.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[whiteQueen3.indexIOnLogicArray - x][whiteQueen3.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen3.indexIOnLogicArray - x, whiteQueen3.indexJOnLogicArray)
                            elif rectLogicArray[whiteQueen3.indexIOnLogicArray - x][whiteQueen3.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen3.indexIOnLogicArray - x, whiteQueen3.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if whiteQueen3.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen3.indexIOnLogicArray][whiteQueen3.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen3.indexIOnLogicArray, whiteQueen3.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen3.indexIOnLogicArray][whiteQueen3.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen3.indexIOnLogicArray, whiteQueen3.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if whiteQueen3.indexIOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen3.indexIOnLogicArray + x][whiteQueen3.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen3.indexIOnLogicArray + x, whiteQueen3.indexJOnLogicArray)
                            elif rectLogicArray[whiteQueen3.indexIOnLogicArray + x][whiteQueen3.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen3.indexIOnLogicArray + x, whiteQueen3.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if whiteQueen3.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen3.indexIOnLogicArray][whiteQueen3.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen3.indexIOnLogicArray, whiteQueen3.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen3.indexIOnLogicArray][whiteQueen3.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen3.indexIOnLogicArray, whiteQueen3.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
                
            elif whichCastle == 4:
                if whiteQueen4.onBoard:
                
                    # Up direction
                    for x in range(1,8):
                        if whiteQueen4.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[whiteQueen4.indexIOnLogicArray - x][whiteQueen4.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen4.indexIOnLogicArray - x, whiteQueen4.indexJOnLogicArray)
                            elif rectLogicArray[whiteQueen4.indexIOnLogicArray - x][whiteQueen4.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen4.indexIOnLogicArray - x, whiteQueen4.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if whiteQueen4.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen4.indexIOnLogicArray][whiteQueen4.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen4.indexIOnLogicArray, whiteQueen4.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen4.indexIOnLogicArray][whiteQueen4.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen4.indexIOnLogicArray, whiteQueen4.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if whiteQueen4.indexIOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen4.indexIOnLogicArray + x][whiteQueen4.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen4.indexIOnLogicArray + x, whiteQueen4.indexJOnLogicArray)
                            elif rectLogicArray[whiteQueen4.indexIOnLogicArray + x][whiteQueen4.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen4.indexIOnLogicArray + x, whiteQueen4.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if whiteQueen4.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen4.indexIOnLogicArray][whiteQueen4.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen4.indexIOnLogicArray, whiteQueen4.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen4.indexIOnLogicArray][whiteQueen4.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen4.indexIOnLogicArray, whiteQueen4.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichCastle == 5:
                if whiteQueen5.onBoard:
                
                    # Up direction
                    for x in range(1,8):
                        if whiteQueen5.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[whiteQueen5.indexIOnLogicArray - x][whiteQueen5.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen5.indexIOnLogicArray - x, whiteQueen5.indexJOnLogicArray)
                            elif rectLogicArray[whiteQueen5.indexIOnLogicArray - x][whiteQueen5.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen5.indexIOnLogicArray - x, whiteQueen5.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if whiteQueen5.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen5.indexIOnLogicArray][whiteQueen5.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen5.indexIOnLogicArray, whiteQueen5.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen5.indexIOnLogicArray][whiteQueen5.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen5.indexIOnLogicArray, whiteQueen5.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if whiteQueen5.indexIOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen5.indexIOnLogicArray + x][whiteQueen5.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen5.indexIOnLogicArray + x, whiteQueen5.indexJOnLogicArray)
                            elif rectLogicArray[whiteQueen5.indexIOnLogicArray + x][whiteQueen5.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen5.indexIOnLogicArray + x, whiteQueen5.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if whiteQueen5.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen5.indexIOnLogicArray][whiteQueen5.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen5.indexIOnLogicArray, whiteQueen5.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen5.indexIOnLogicArray][whiteQueen5.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen5.indexIOnLogicArray, whiteQueen5.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichCastle == 6:
                if whiteQueen6.onBoard:
                
                    # Up direction
                    for x in range(1,8):
                        if whiteQueen6.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[whiteQueen6.indexIOnLogicArray - x][whiteQueen6.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen6.indexIOnLogicArray - x, whiteQueen6.indexJOnLogicArray)
                            elif rectLogicArray[whiteQueen6.indexIOnLogicArray - x][whiteQueen6.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen6.indexIOnLogicArray - x, whiteQueen6.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if whiteQueen6.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen6.indexIOnLogicArray][whiteQueen6.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen6.indexIOnLogicArray, whiteQueen6.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen6.indexIOnLogicArray][whiteQueen6.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen6.indexIOnLogicArray, whiteQueen6.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if whiteQueen6.indexIOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen6.indexIOnLogicArray + x][whiteQueen6.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen6.indexIOnLogicArray + x, whiteQueen6.indexJOnLogicArray)
                            elif rectLogicArray[whiteQueen6.indexIOnLogicArray + x][whiteQueen6.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen6.indexIOnLogicArray + x, whiteQueen6.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if whiteQueen6.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen6.indexIOnLogicArray][whiteQueen6.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen6.indexIOnLogicArray, whiteQueen6.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen6.indexIOnLogicArray][whiteQueen6.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen6.indexIOnLogicArray, whiteQueen6.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
                
            elif whichCastle == 7:
                if whiteQueen7.onBoard:
                
                    # Up direction
                    for x in range(1,8):
                        if whiteQueen7.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[whiteQueen7.indexIOnLogicArray - x][whiteQueen7.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen7.indexIOnLogicArray - x, whiteQueen7.indexJOnLogicArray)
                            elif rectLogicArray[whiteQueen7.indexIOnLogicArray - x][whiteQueen7.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen7.indexIOnLogicArray - x, whiteQueen7.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if whiteQueen7.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen7.indexIOnLogicArray][whiteQueen7.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen7.indexIOnLogicArray, whiteQueen7.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen7.indexIOnLogicArray][whiteQueen7.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen7.indexIOnLogicArray, whiteQueen7.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if whiteQueen7.indexIOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen7.indexIOnLogicArray + x][whiteQueen7.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen7.indexIOnLogicArray + x, whiteQueen7.indexJOnLogicArray)
                            elif rectLogicArray[whiteQueen7.indexIOnLogicArray + x][whiteQueen7.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen7.indexIOnLogicArray + x, whiteQueen7.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if whiteQueen7.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen7.indexIOnLogicArray][whiteQueen7.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen7.indexIOnLogicArray, whiteQueen7.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen7.indexIOnLogicArray][whiteQueen7.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen7.indexIOnLogicArray, whiteQueen7.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichCastle == 8:
                if whiteQueen8.onBoard:
                
                    # Up direction
                    for x in range(1,8):
                        if whiteQueen8.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[whiteQueen8.indexIOnLogicArray - x][whiteQueen8.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen8.indexIOnLogicArray - x, whiteQueen8.indexJOnLogicArray)
                            elif rectLogicArray[whiteQueen8.indexIOnLogicArray - x][whiteQueen8.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen8.indexIOnLogicArray - x, whiteQueen8.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if whiteQueen8.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen8.indexIOnLogicArray][whiteQueen8.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen8.indexIOnLogicArray, whiteQueen8.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen8.indexIOnLogicArray][whiteQueen8.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen8.indexIOnLogicArray, whiteQueen8.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if whiteQueen8.indexIOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen8.indexIOnLogicArray + x][whiteQueen8.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen8.indexIOnLogicArray + x, whiteQueen8.indexJOnLogicArray)
                            elif rectLogicArray[whiteQueen8.indexIOnLogicArray + x][whiteQueen8.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen8.indexIOnLogicArray + x, whiteQueen8.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if whiteQueen8.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen8.indexIOnLogicArray][whiteQueen8.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen8.indexIOnLogicArray, whiteQueen8.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen8.indexIOnLogicArray][whiteQueen8.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen8.indexIOnLogicArray, whiteQueen8.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichCastle == 9:
                if whiteQueen9.onBoard:
                
                    # Up direction
                    for x in range(1,8):
                        if whiteQueen9.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[whiteQueen9.indexIOnLogicArray - x][whiteQueen9.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen9.indexIOnLogicArray - x, whiteQueen9.indexJOnLogicArray)
                            elif rectLogicArray[whiteQueen9.indexIOnLogicArray - x][whiteQueen9.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen9.indexIOnLogicArray - x, whiteQueen9.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if whiteQueen9.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen9.indexIOnLogicArray][whiteQueen9.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen9.indexIOnLogicArray, whiteQueen9.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen9.indexIOnLogicArray][whiteQueen9.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen9.indexIOnLogicArray, whiteQueen9.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if whiteQueen9.indexIOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen9.indexIOnLogicArray + x][whiteQueen9.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen9.indexIOnLogicArray + x, whiteQueen9.indexJOnLogicArray)
                            elif rectLogicArray[whiteQueen9.indexIOnLogicArray + x][whiteQueen9.indexJOnLogicArray] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen9.indexIOnLogicArray + x, whiteQueen9.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if whiteQueen9.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen9.indexIOnLogicArray][whiteQueen9.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen9.indexIOnLogicArray, whiteQueen9.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen9.indexIOnLogicArray][whiteQueen9.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen9.indexIOnLogicArray, whiteQueen9.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
        
        elif turn == 'black':
            if whichCastle == 1:
                if blackQueen1.onBoard:
                
                    # Up direction
                    for x in range(1,8):
                        if blackQueen1.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[blackQueen1.indexIOnLogicArray - x][blackQueen1.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen1.indexIOnLogicArray - x, blackQueen1.indexJOnLogicArray)
                            elif rectLogicArray[blackQueen1.indexIOnLogicArray - x][blackQueen1.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen1.indexIOnLogicArray - x, blackQueen1.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if blackQueen1.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen1.indexIOnLogicArray][blackQueen1.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen1.indexIOnLogicArray, blackQueen1.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen1.indexIOnLogicArray][blackQueen1.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen1.indexIOnLogicArray, blackQueen1.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if blackQueen1.indexIOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen1.indexIOnLogicArray + x][blackQueen1.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen1.indexIOnLogicArray + x, blackQueen1.indexJOnLogicArray)
                            elif rectLogicArray[blackQueen1.indexIOnLogicArray + x][blackQueen1.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen1.indexIOnLogicArray + x, blackQueen1.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if blackQueen1.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen1.indexIOnLogicArray][blackQueen1.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen1.indexIOnLogicArray, blackQueen1.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen1.indexIOnLogicArray][blackQueen1.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen1.indexIOnLogicArray, blackQueen1.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichCastle == 2:
                if blackQueen2.onBoard:
                
                    # Up direction
                    for x in range(1,8):
                        if blackQueen2.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[blackQueen2.indexIOnLogicArray - x][blackQueen2.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen2.indexIOnLogicArray - x, blackQueen2.indexJOnLogicArray)
                            elif rectLogicArray[blackQueen2.indexIOnLogicArray - x][blackQueen2.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen2.indexIOnLogicArray - x, blackQueen2.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if blackQueen2.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen2.indexIOnLogicArray][blackQueen2.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen2.indexIOnLogicArray, blackQueen2.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen2.indexIOnLogicArray][blackQueen2.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen2.indexIOnLogicArray, blackQueen2.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if blackQueen2.indexIOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen2.indexIOnLogicArray + x][blackQueen2.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen2.indexIOnLogicArray + x, blackQueen2.indexJOnLogicArray)
                            elif rectLogicArray[blackQueen2.indexIOnLogicArray + x][blackQueen2.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen2.indexIOnLogicArray + x, blackQueen2.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if blackQueen2.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen2.indexIOnLogicArray][blackQueen2.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen2.indexIOnLogicArray, blackQueen2.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen2.indexIOnLogicArray][blackQueen2.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen2.indexIOnLogicArray, blackQueen2.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichCastle == 3:
                if blackQueen3.onBoard:
                
                    # Up direction
                    for x in range(1,8):
                        if blackQueen3.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[blackQueen3.indexIOnLogicArray - x][blackQueen3.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen3.indexIOnLogicArray - x, blackQueen3.indexJOnLogicArray)
                            elif rectLogicArray[blackQueen3.indexIOnLogicArray - x][blackQueen3.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen3.indexIOnLogicArray - x, blackQueen3.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if blackQueen3.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen3.indexIOnLogicArray][blackQueen3.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen3.indexIOnLogicArray, blackQueen3.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen3.indexIOnLogicArray][blackQueen3.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen3.indexIOnLogicArray, blackQueen3.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if blackQueen3.indexIOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen3.indexIOnLogicArray + x][blackQueen3.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen3.indexIOnLogicArray + x, blackQueen3.indexJOnLogicArray)
                            elif rectLogicArray[blackQueen3.indexIOnLogicArray + x][blackQueen3.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen3.indexIOnLogicArray + x, blackQueen3.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if blackQueen3.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen3.indexIOnLogicArray][blackQueen3.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen3.indexIOnLogicArray, blackQueen3.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen3.indexIOnLogicArray][blackQueen3.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen3.indexIOnLogicArray, blackQueen3.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichCastle == 4:
                if blackQueen4.onBoard:
                
                    # Up direction
                    for x in range(1,8):
                        if blackQueen4.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[blackQueen4.indexIOnLogicArray - x][blackQueen4.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen4.indexIOnLogicArray - x, blackQueen4.indexJOnLogicArray)
                            elif rectLogicArray[blackQueen4.indexIOnLogicArray - x][blackQueen4.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen4.indexIOnLogicArray - x, blackQueen4.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if blackQueen4.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen4.indexIOnLogicArray][blackQueen4.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen4.indexIOnLogicArray, blackQueen4.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen4.indexIOnLogicArray][blackQueen4.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen4.indexIOnLogicArray, blackQueen4.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if blackQueen4.indexIOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen4.indexIOnLogicArray + x][blackQueen4.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen4.indexIOnLogicArray + x, blackQueen4.indexJOnLogicArray)
                            elif rectLogicArray[blackQueen4.indexIOnLogicArray + x][blackQueen4.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen4.indexIOnLogicArray + x, blackQueen4.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if blackQueen4.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen4.indexIOnLogicArray][blackQueen4.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen4.indexIOnLogicArray, blackQueen4.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen4.indexIOnLogicArray][blackQueen4.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen4.indexIOnLogicArray, blackQueen4.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichCastle == 5:
                if blackQueen5.onBoard:
                
                    # Up direction
                    for x in range(1,8):
                        if blackQueen5.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[blackQueen5.indexIOnLogicArray - x][blackQueen5.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen5.indexIOnLogicArray - x, blackQueen5.indexJOnLogicArray)
                            elif rectLogicArray[blackQueen5.indexIOnLogicArray - x][blackQueen5.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen5.indexIOnLogicArray - x, blackQueen5.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if blackQueen5.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen5.indexIOnLogicArray][blackQueen5.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen5.indexIOnLogicArray, blackQueen5.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen5.indexIOnLogicArray][blackQueen5.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen5.indexIOnLogicArray, blackQueen5.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if blackQueen5.indexIOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen5.indexIOnLogicArray + x][blackQueen5.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen5.indexIOnLogicArray + x, blackQueen5.indexJOnLogicArray)
                            elif rectLogicArray[blackQueen5.indexIOnLogicArray + x][blackQueen5.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen5.indexIOnLogicArray + x, blackQueen5.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if blackQueen5.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen5.indexIOnLogicArray][blackQueen5.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen5.indexIOnLogicArray, blackQueen5.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen5.indexIOnLogicArray][blackQueen5.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen5.indexIOnLogicArray, blackQueen5.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichCastle == 6:
                if blackQueen6.onBoard:
                
                    # Up direction
                    for x in range(1,8):
                        if blackQueen6.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[blackQueen6.indexIOnLogicArray - x][blackQueen6.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen6.indexIOnLogicArray - x, blackQueen6.indexJOnLogicArray)
                            elif rectLogicArray[blackQueen6.indexIOnLogicArray - x][blackQueen6.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen6.indexIOnLogicArray - x, blackQueen6.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if blackQueen6.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen6.indexIOnLogicArray][blackQueen6.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen6.indexIOnLogicArray, blackQueen6.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen6.indexIOnLogicArray][blackQueen6.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen6.indexIOnLogicArray, blackQueen6.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if blackQueen6.indexIOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen6.indexIOnLogicArray + x][blackQueen6.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen6.indexIOnLogicArray + x, blackQueen6.indexJOnLogicArray)
                            elif rectLogicArray[blackQueen6.indexIOnLogicArray + x][blackQueen6.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen6.indexIOnLogicArray + x, blackQueen6.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if blackQueen6.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen6.indexIOnLogicArray][blackQueen6.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen6.indexIOnLogicArray, blackQueen6.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen6.indexIOnLogicArray][blackQueen6.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen6.indexIOnLogicArray, blackQueen6.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichCastle == 7:
                if blackQueen7.onBoard:
                
                    # Up direction
                    for x in range(1,8):
                        if blackQueen7.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[blackQueen7.indexIOnLogicArray - x][blackQueen7.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen7.indexIOnLogicArray - x, blackQueen7.indexJOnLogicArray)
                            elif rectLogicArray[blackQueen7.indexIOnLogicArray - x][blackQueen7.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen7.indexIOnLogicArray - x, blackQueen7.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if blackQueen7.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen7.indexIOnLogicArray][blackQueen7.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen7.indexIOnLogicArray, blackQueen7.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen7.indexIOnLogicArray][blackQueen7.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen7.indexIOnLogicArray, blackQueen7.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if blackQueen7.indexIOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen7.indexIOnLogicArray + x][blackQueen7.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen7.indexIOnLogicArray + x, blackQueen7.indexJOnLogicArray)
                            elif rectLogicArray[blackQueen7.indexIOnLogicArray + x][blackQueen7.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen7.indexIOnLogicArray + x, blackQueen7.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if blackQueen7.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen7.indexIOnLogicArray][blackQueen7.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen7.indexIOnLogicArray, blackQueen7.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen7.indexIOnLogicArray][blackQueen7.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen7.indexIOnLogicArray, blackQueen7.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichCastle == 8:
                if blackQueen8.onBoard:
                
                    # Up direction
                    for x in range(1,8):
                        if blackQueen8.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[blackQueen8.indexIOnLogicArray - x][blackQueen8.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen8.indexIOnLogicArray - x, blackQueen8.indexJOnLogicArray)
                            elif rectLogicArray[blackQueen8.indexIOnLogicArray - x][blackQueen8.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen8.indexIOnLogicArray - x, blackQueen8.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if blackQueen8.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen8.indexIOnLogicArray][blackQueen8.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen8.indexIOnLogicArray, blackQueen8.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen8.indexIOnLogicArray][blackQueen8.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen8.indexIOnLogicArray, blackQueen8.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if blackQueen8.indexIOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen8.indexIOnLogicArray + x][blackQueen8.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen8.indexIOnLogicArray + x, blackQueen8.indexJOnLogicArray)
                            elif rectLogicArray[blackQueen8.indexIOnLogicArray + x][blackQueen8.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen8.indexIOnLogicArray + x, blackQueen8.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if blackQueen8.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen8.indexIOnLogicArray][blackQueen8.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen8.indexIOnLogicArray, blackQueen8.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen8.indexIOnLogicArray][blackQueen8.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen8.indexIOnLogicArray, blackQueen8.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichCastle == 9:
                if blackQueen9.onBoard:
                
                    # Up direction
                    for x in range(1,8):
                        if blackQueen9.indexIOnLogicArray - x  >= 0:
                            if rectLogicArray[blackQueen9.indexIOnLogicArray - x][blackQueen9.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen9.indexIOnLogicArray - x, blackQueen9.indexJOnLogicArray)
                            elif rectLogicArray[blackQueen9.indexIOnLogicArray - x][blackQueen9.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen9.indexIOnLogicArray - x, blackQueen9.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Right direction
                    for x in range(1,8):
                        if blackQueen9.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen9.indexIOnLogicArray][blackQueen9.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen9.indexIOnLogicArray, blackQueen9.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen9.indexIOnLogicArray][blackQueen9.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen9.indexIOnLogicArray, blackQueen9.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # Down direction
                    for x in range(1,8):
                        if blackQueen9.indexIOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen9.indexIOnLogicArray + x][blackQueen9.indexJOnLogicArray] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen9.indexIOnLogicArray + x, blackQueen9.indexJOnLogicArray)
                            elif rectLogicArray[blackQueen9.indexIOnLogicArray + x][blackQueen9.indexJOnLogicArray] > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen9.indexIOnLogicArray + x, blackQueen9.indexJOnLogicArray)
                                break
                            else:
                                break
                    # Left direction
                    for x in range(1,8):
                        if blackQueen9.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen9.indexIOnLogicArray][blackQueen9.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen9.indexIOnLogicArray, blackQueen9.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen9.indexIOnLogicArray][blackQueen9.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen9.indexIOnLogicArray, blackQueen9.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
                        
def MovePositionOfCastle(turn, whichCastle, whereCastleCanMove, whereMouseIs):
    global switchTurn
    switchTurn = False
    
    if turn == 'white':
        if whichCastle == 1:
            if whereCastleCanMove != [(0,0) for x in range(0,len(whereCastleCanMove))]: # If the movement list is not empty
                for x in range(0,len(whereCastleCanMove)):
                    if whereCastleCanMove[x]:
                        tileLetter, tileNumber = whereCastleCanMove[x]           
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs): # If where the mouse is alligns with potential moves
                            whiteCastle1.rect.x, whiteCastle1.rect.y = whereMouseIs # movement of the castle
                            CenterCastleInTile(turn, whichCastle) # ensures the castle is centered in its new tile
                            PiecesCollide(turn) # If it collides with a piece of opposite colour it removes them from the board
                            
                            if whiteCastle1.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)): # Ensures the movement of the castle is on the right tile
                                rectLogicArray[whiteCastle1.indexIOnLogicArray][whiteCastle1.indexJOnLogicArray] = 0 # Starting here the position of the castle is updated in the logic array
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                whiteCastle1.indexIOnLogicArray, whiteCastle1.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[whiteCastle1.indexIOnLogicArray][whiteCastle1.indexJOnLogicArray] = 2 # Ends here
                                switchTurn = True # Signals to swith turns
                                whiteCastle1.pos = whereCastleCanMove[x] # Updates position in the object
        
        elif whichCastle == 2:
            
            if whereCastleCanMove != [(0,0) for x in range(0,len(whereCastleCanMove))]:
                for x in range(0,len(whereCastleCanMove)):
                    if whereCastleCanMove[x]:
                        tileLetter, tileNumber = whereCastleCanMove[x]           
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            whiteCastle2.rect.x, whiteCastle2.rect.y = whereMouseIs
                            CenterCastleInTile(turn, whichCastle)
                            PiecesCollide(turn)
                            if whiteCastle2.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[whiteCastle2.indexIOnLogicArray][whiteCastle2.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                whiteCastle2.indexIOnLogicArray, whiteCastle2.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[whiteCastle2.indexIOnLogicArray][whiteCastle2.indexJOnLogicArray] = 2
                                switchTurn = True
                                whiteCastle2.pos = whereCastleCanMove[x]
    elif turn == 'black':
        
        if whichCastle == 1:
            
            if whereCastleCanMove != [(0,0) for x in range(0,len(whereCastleCanMove))]:
                for x in range(0,len(whereCastleCanMove)):
                    if whereCastleCanMove[x]:
                        tileLetter, tileNumber = whereCastleCanMove[x]           
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            blackCastle1.rect.x, blackCastle1.rect.y = whereMouseIs
                            CenterCastleInTile(turn, whichCastle)
                            PiecesCollide(turn)
                            if blackCastle1.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[blackCastle1.indexIOnLogicArray][blackCastle1.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                blackCastle1.indexIOnLogicArray, blackCastle1.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[blackCastle1.indexIOnLogicArray][blackCastle1.indexJOnLogicArray] = -2
                                switchTurn = True
                                blackCastle1.pos = whereCastleCanMove[x]
        
        elif whichCastle == 2:
            
            if whereCastleCanMove != [(0,0) for x in range(0,len(whereCastleCanMove))]:
                for x in range(0,len(whereCastleCanMove)):
                    if whereCastleCanMove[x]:
                        tileLetter, tileNumber = whereCastleCanMove[x]           
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            blackCastle2.rect.x, blackCastle2.rect.y = whereMouseIs
                            CenterCastleInTile(turn, whichCastle)
                            PiecesCollide(turn)
                            if blackCastle2.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[blackCastle2.indexIOnLogicArray][blackCastle2.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                blackCastle2.indexIOnLogicArray, blackCastle2.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[blackCastle2.indexIOnLogicArray][blackCastle2.indexJOnLogicArray] = -2
                                switchTurn = True
                                blackCastle2.pos = whereCastleCanMove[x]  
    
# Knight methods

def CreateWhiteKnights():
    global whiteKnight1, whiteKnight2
    
    # Creates 2 knight objects
    # Initialised with their starting position and their position on the logic array
    whiteKnight1 = chessPieces.Knight("white", ("b", 1), 7, 1, True)
    whiteKnight2 = chessPieces.Knight("white", ("g", 1), 7, 6, True)

def CreateBlackKnights():
    global blackKnight1, blackKnight2
    
    # Creates 2 knight objects
    # Initialised with their starting position and their position on the logic array
    blackKnight1 =  chessPieces.Knight("black", ("b", 8), 0, 1, True)
    blackKnight2 =  chessPieces.Knight("black", ("g", 8), 0 , 6, True)
    
def PutAllKnightsOnTheBoard():
    
    # Ties the knights surfaces and rects together and then puts them on the screen
    screen.blit(blackKnight1.surface, blackKnight1.rect)
    screen.blit(blackKnight2.surface, blackKnight2.rect)
    
    screen.blit(whiteKnight1.surface, whiteKnight1.rect)
    screen.blit(whiteKnight2.surface, whiteKnight2.rect)

def CollidingWithAKnight(turn, whereMouseIs):
    # Detects if mouse is colliding with a piece
    if turn == 'white':
        if whiteKnight1.rect.collidepoint(whereMouseIs) or whiteKnight2.rect.collidepoint(whereMouseIs):
            return True
        else:
            return False
    elif turn == "black":
        if blackKnight1.rect.collidepoint(whereMouseIs) or blackKnight2.rect.collidepoint(whereMouseIs):     
            return True
        else:
            return False

def WhichKnightIsCollidedWith(turn, collidingWithKnight, whereMouseIs):
    # Detects which knight the mouse is colliding with
    if turn == 'white':
        if whiteKnight1.rect.collidepoint(whereMouseIs):
            return 1
        elif whiteKnight2.rect.collidepoint(whereMouseIs):
            return 2
    elif turn == 'black':
        if blackKnight1.rect.collidepoint(whereMouseIs):
            return 1
        elif blackKnight2.rect.collidepoint(whereMouseIs):
            return 2

def CenterKnightInTile(turn, whichKnight):
    # Centers a piece in the tile they are currently on to reduce clustering
    if turn == 'white':
        if whichKnight == 1:
            if whiteKnight1.rect.collidelist(collisionList) == -1:
                return False
            else:
                whiteKnight1.rect.center = collisionList[whiteKnight1.rect.collidelist(collisionList)].center 
        elif whichKnight == 2:
            if whiteKnight2.rect.collidelist(collisionList) == -1:
                return False
            else:
                whiteKnight2.rect.center = collisionList[whiteKnight2.rect.collidelist(collisionList)].center
    elif turn == 'black':
        if whichKnight == 1:
            if blackKnight1.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackKnight1.rect.center = collisionList[blackKnight1.rect.collidelist(collisionList)].center 
        elif whichKnight == 2:
            if blackKnight2.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackKnight2.rect.center = collisionList[blackKnight2.rect.collidelist(collisionList)].center

def WhereCanKnightMove(turn, whichKnight):
    # 8 potential moves a knight can make
    # Organised in a clockwise fashion, index 0 being the top right potential position and index 7 in the top left
    eightMoves = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    
    if turn == 'white':
        
        if whichKnight == 1:
            if whiteKnight1.onBoard:
                # Down - Changing index I by 2 
                
                    # Right - Changing index J by 1
                if whiteKnight1.indexIOnLogicArray + 2 < 8 and whiteKnight1.indexJOnLogicArray + 1 < 8:
                    if rectLogicArray[whiteKnight1.indexIOnLogicArray + 2][whiteKnight1.indexJOnLogicArray + 1] < 1:
                        eightMoves[3] = AdjustPositionAfterMove(whiteKnight1.indexIOnLogicArray + 2, whiteKnight1.indexJOnLogicArray + 1)
                else:
                        eightMoves[3] = (0,0)
                    # Left - Changing index J by 1
                if whiteKnight1.indexIOnLogicArray + 2 < 8 and whiteKnight1.indexJOnLogicArray - 1 >= 0:
                    if rectLogicArray[whiteKnight1.indexIOnLogicArray + 2][whiteKnight1.indexJOnLogicArray - 1] < 1:
                        eightMoves[4] = AdjustPositionAfterMove(whiteKnight1.indexIOnLogicArray + 2, whiteKnight1.indexJOnLogicArray - 1)   
                else:
                        eightMoves[4] = (0,0)
                # Up - Changing index I by 2 
                
                    # Right - Changing index J by 1
                if whiteKnight1.indexIOnLogicArray - 2 >= 0 and whiteKnight1.indexJOnLogicArray + 1 < 8:
                    if rectLogicArray[whiteKnight1.indexIOnLogicArray - 2][whiteKnight1.indexJOnLogicArray + 1] < 1:
                        eightMoves[0] = AdjustPositionAfterMove(whiteKnight1.indexIOnLogicArray - 2, whiteKnight1.indexJOnLogicArray + 1)
                else:
                        eightMoves[0] = (0,0)
                    # Left - Changing index J by 1
                if whiteKnight1.indexIOnLogicArray - 2 >= 0 and whiteKnight1.indexJOnLogicArray - 1 >= 0:
                    if rectLogicArray[whiteKnight1.indexIOnLogicArray - 2][whiteKnight1.indexJOnLogicArray - 1] < 1:
                        eightMoves[7] = AdjustPositionAfterMove(whiteKnight1.indexIOnLogicArray - 2, whiteKnight1.indexJOnLogicArray - 1)
                else:
                        eightMoves[7] = (0,0)
                # Right - Changing J index by 2
                
                    # Down - Changing I index by 1
                if whiteKnight1.indexIOnLogicArray + 1 < 8 and whiteKnight1.indexJOnLogicArray + 2 < 8:
                    if rectLogicArray[whiteKnight1.indexIOnLogicArray + 1][whiteKnight1.indexJOnLogicArray + 2] < 1:
                        eightMoves[2] = AdjustPositionAfterMove(whiteKnight1.indexIOnLogicArray + 1, whiteKnight1.indexJOnLogicArray + 2)
                else:
                        eightMoves[2] = (0,0)
                    # Up - Changing I index by 1
                if whiteKnight1.indexIOnLogicArray - 1 >= 0 and whiteKnight1.indexJOnLogicArray + 2 < 8:
                    if rectLogicArray[whiteKnight1.indexIOnLogicArray - 1][whiteKnight1.indexJOnLogicArray + 2] < 1:
                        eightMoves[1] = AdjustPositionAfterMove(whiteKnight1.indexIOnLogicArray - 1, whiteKnight1.indexJOnLogicArray + 2)
                else:
                        eightMoves[1] = (0,0)
                
                # Left - Changing J index by 2
                
                    # Down - Changing I index by 1
                if whiteKnight1.indexIOnLogicArray + 1 < 8 and whiteKnight1.indexJOnLogicArray - 2 >= 0:
                    if rectLogicArray[whiteKnight1.indexIOnLogicArray + 1][whiteKnight1.indexJOnLogicArray - 2] < 1:
                        eightMoves[5] = AdjustPositionAfterMove(whiteKnight1.indexIOnLogicArray + 1, whiteKnight1.indexJOnLogicArray - 2)
                else:
                        eightMoves[5] = (0,0)
                    # Up - Changing I index by 1
                if whiteKnight1.indexIOnLogicArray - 1 >= 0 and whiteKnight1.indexJOnLogicArray - 2 >= 0:
                    if rectLogicArray[whiteKnight1.indexIOnLogicArray - 1][whiteKnight1.indexJOnLogicArray - 2] < 1:
                        eightMoves[6] = AdjustPositionAfterMove(whiteKnight1.indexIOnLogicArray - 1, whiteKnight1.indexJOnLogicArray - 2)
                else:
                        eightMoves[6] = (0,0)
                        
                return eightMoves
        
        elif whichKnight == 2:
            if whiteKnight2.onBoard:
                # Down - Changing index I by 2 
                
                    # Right - Changing index J by 1
                if whiteKnight2.indexIOnLogicArray + 2 < 8 and whiteKnight2.indexJOnLogicArray + 1 < 8:
                    if rectLogicArray[whiteKnight2.indexIOnLogicArray + 2][whiteKnight2.indexJOnLogicArray + 1] < 1:
                        eightMoves[3] = AdjustPositionAfterMove(whiteKnight2.indexIOnLogicArray + 2, whiteKnight2.indexJOnLogicArray + 1)
                else:
                        eightMoves[3] = (0,0)
                    # Left - Changing index J by 1
                if whiteKnight2.indexIOnLogicArray + 2 < 8 and whiteKnight2.indexJOnLogicArray - 1 >= 0:
                    if rectLogicArray[whiteKnight2.indexIOnLogicArray + 2][whiteKnight2.indexJOnLogicArray - 1] < 1:
                        eightMoves[4] = AdjustPositionAfterMove(whiteKnight2.indexIOnLogicArray + 2, whiteKnight2.indexJOnLogicArray - 1)   
                else:
                        eightMoves[4] = (0,0)
                # Up - Changing index I by 2 
                
                    # Right - Changing index J by 1
                if whiteKnight2.indexIOnLogicArray - 2 >= 0 and whiteKnight2.indexJOnLogicArray + 1 < 8:
                    if rectLogicArray[whiteKnight2.indexIOnLogicArray - 2][whiteKnight2.indexJOnLogicArray + 1] < 1:
                        eightMoves[0] = AdjustPositionAfterMove(whiteKnight2.indexIOnLogicArray - 2, whiteKnight2.indexJOnLogicArray + 1)
                else:
                        eightMoves[0] = (0,0)
                    # Left - Changing index J by 1
                if whiteKnight2.indexIOnLogicArray - 2 >= 0 and whiteKnight2.indexJOnLogicArray - 1 >= 0:
                    if rectLogicArray[whiteKnight2.indexIOnLogicArray - 2][whiteKnight2.indexJOnLogicArray - 1] < 1:
                        eightMoves[7] = AdjustPositionAfterMove(whiteKnight2.indexIOnLogicArray - 2, whiteKnight2.indexJOnLogicArray - 1)
                else:
                        eightMoves[7] = (0,0)
                    
                # Right - Changing J index by 2
                
                    # Down - Changing I index by 1
                if whiteKnight2.indexIOnLogicArray + 1 < 8 and whiteKnight2.indexJOnLogicArray + 2 < 8:
                    if rectLogicArray[whiteKnight2.indexIOnLogicArray + 1][whiteKnight2.indexJOnLogicArray + 2] < 1:
                        eightMoves[2] = AdjustPositionAfterMove(whiteKnight2.indexIOnLogicArray + 1, whiteKnight2.indexJOnLogicArray + 2)
                else:
                        eightMoves[2] = (0,0)
                    # Up - Changing I index by 1
                if whiteKnight2.indexIOnLogicArray - 1 >= 0 and whiteKnight2.indexJOnLogicArray + 2 < 8:
                    if rectLogicArray[whiteKnight2.indexIOnLogicArray - 1][whiteKnight2.indexJOnLogicArray + 2] < 1:
                        eightMoves[1] = AdjustPositionAfterMove(whiteKnight2.indexIOnLogicArray - 1, whiteKnight2.indexJOnLogicArray + 2)
                else:
                        eightMoves[1] = (0,0)
                
                # Left - Changing J index by 2
                
                    # Down - Changing I index by 1
                if whiteKnight2.indexIOnLogicArray + 1 < 8 and whiteKnight2.indexJOnLogicArray - 2 >= 0:
                    if rectLogicArray[whiteKnight2.indexIOnLogicArray + 1][whiteKnight2.indexJOnLogicArray - 2] < 1:
                        eightMoves[5] = AdjustPositionAfterMove(whiteKnight2.indexIOnLogicArray + 1, whiteKnight2.indexJOnLogicArray - 2)
                else:
                        eightMoves[5] = (0,0)
                    # Up - Changing I index by 1
                if whiteKnight2.indexIOnLogicArray - 1 >= 0 and whiteKnight2.indexJOnLogicArray - 2 >= 0:
                    if rectLogicArray[whiteKnight2.indexIOnLogicArray - 1][whiteKnight2.indexJOnLogicArray - 2] < 1:
                        eightMoves[6] = AdjustPositionAfterMove(whiteKnight2.indexIOnLogicArray - 1, whiteKnight2.indexJOnLogicArray - 2)
                else:
                        eightMoves[6] = (0,0)
                        
                return eightMoves
        
    elif turn == 'black':
        
        if whichKnight == 1:
            if blackKnight1.onBoard:
                # Down - Changing index I by 2 
                
                    # Right - Changing index J by 1
                if blackKnight1.indexIOnLogicArray + 2 < 8 and blackKnight1.indexJOnLogicArray + 1 < 8:
                    if rectLogicArray[blackKnight1.indexIOnLogicArray + 2][blackKnight1.indexJOnLogicArray + 1] >= 0:
                        eightMoves[3] = AdjustPositionAfterMove(blackKnight1.indexIOnLogicArray + 2, blackKnight1.indexJOnLogicArray + 1)
                else:
                        eightMoves[3] = (0,0)
                    # Left - Changing index J by 1
                if blackKnight1.indexIOnLogicArray + 2 < 8 and blackKnight1.indexJOnLogicArray - 1 >= 0:
                    if rectLogicArray[blackKnight1.indexIOnLogicArray + 2][blackKnight1.indexJOnLogicArray - 1] >= 0:
                        eightMoves[4] = AdjustPositionAfterMove(blackKnight1.indexIOnLogicArray + 2, blackKnight1.indexJOnLogicArray - 1)  
                else:
                        eightMoves[4] = (0,0) 
                
                # Up - Changing index I by 2 
                
                    # Right - Changing index J by 1
                if blackKnight1.indexIOnLogicArray - 2 >= 0 and blackKnight1.indexJOnLogicArray + 1 < 8:
                    if rectLogicArray[blackKnight1.indexIOnLogicArray - 2][blackKnight1.indexJOnLogicArray + 1] >= 0:
                        eightMoves[0] = AdjustPositionAfterMove(blackKnight1.indexIOnLogicArray - 2, blackKnight1.indexJOnLogicArray + 1)
                else:
                        eightMoves[0] = (0,0)
                    # Left - Changing index J by 1
                if blackKnight1.indexIOnLogicArray - 2 >= 0 and blackKnight1.indexJOnLogicArray - 1 >= 0:
                    if rectLogicArray[blackKnight1.indexIOnLogicArray - 2][blackKnight1.indexJOnLogicArray - 1] >= 0:
                        eightMoves[7] = AdjustPositionAfterMove(blackKnight1.indexIOnLogicArray - 2, blackKnight1.indexJOnLogicArray - 1)
                else:
                        eightMoves[7] = (0,0)
                    
                # Right - Changing J index by 2
                
                    # Down - Changing I index by 1
                if blackKnight1.indexIOnLogicArray + 1 < 8 and blackKnight1.indexJOnLogicArray + 2 < 8:
                    if rectLogicArray[blackKnight1.indexIOnLogicArray + 1][blackKnight1.indexJOnLogicArray + 2] >= 0:
                        eightMoves[2] = AdjustPositionAfterMove(blackKnight1.indexIOnLogicArray + 1, blackKnight1.indexJOnLogicArray + 2)
                else:
                        eightMoves[2] = (0,0)
                    # Up - Changing I index by 1
                if blackKnight1.indexIOnLogicArray - 1 >= 0 and blackKnight1.indexJOnLogicArray + 2 < 8:
                    if rectLogicArray[blackKnight1.indexIOnLogicArray - 1][blackKnight1.indexJOnLogicArray + 2] >= 0:
                        eightMoves[1] = AdjustPositionAfterMove(blackKnight1.indexIOnLogicArray - 1, blackKnight1.indexJOnLogicArray + 2)
                else:
                        eightMoves[1] = (0,0)
                
                # Left - Changing J index by 2
                
                    # Down - Changing I index by 1
                if blackKnight1.indexIOnLogicArray + 1 < 8 and blackKnight1.indexJOnLogicArray - 2 >= 0:
                    if rectLogicArray[blackKnight1.indexIOnLogicArray + 1][blackKnight1.indexJOnLogicArray - 2] >= 0:
                        eightMoves[5] = AdjustPositionAfterMove(blackKnight1.indexIOnLogicArray + 1, blackKnight1.indexJOnLogicArray - 2)
                else:
                        eightMoves[5] = (0,0)
                    # Up - Changing I index by 1
                if blackKnight1.indexIOnLogicArray - 1 >= 0 and blackKnight1.indexJOnLogicArray - 2 >= 0:
                    if rectLogicArray[blackKnight1.indexIOnLogicArray - 1][blackKnight1.indexJOnLogicArray - 2] >= 0:
                        eightMoves[6] = AdjustPositionAfterMove(blackKnight1.indexIOnLogicArray - 1, blackKnight1.indexJOnLogicArray - 2)
                else:
                        eightMoves[6] = (0,0)
                        
                return eightMoves
        
        elif whichKnight == 2:
            if blackKnight2.onBoard:
                # Down - Changing index I by 2 
                
                    # Right - Changing index J by 1
                if blackKnight2.indexIOnLogicArray + 2 < 8 and blackKnight2.indexJOnLogicArray + 1 < 8:
                    if rectLogicArray[blackKnight2.indexIOnLogicArray + 2][blackKnight2.indexJOnLogicArray + 1] >= 0:
                        eightMoves[3] = AdjustPositionAfterMove(blackKnight2.indexIOnLogicArray + 2, blackKnight2.indexJOnLogicArray + 1)
                else:
                        eightMoves[3] = (0,0)
                    # Left - Changing index J by 1
                if blackKnight2.indexIOnLogicArray + 2 < 8 and blackKnight2.indexJOnLogicArray - 1 >= 0:
                    if rectLogicArray[blackKnight2.indexIOnLogicArray + 2][blackKnight2.indexJOnLogicArray - 1] >= 0:
                        eightMoves[4] = AdjustPositionAfterMove(blackKnight2.indexIOnLogicArray + 2, blackKnight2.indexJOnLogicArray - 1)   
                else:
                        eightMoves[4] = (0,0)
                
                # Up - Changing index I by 2 
                
                    # Right - Changing index J by 1
                if blackKnight2.indexIOnLogicArray - 2 >= 0 and blackKnight2.indexJOnLogicArray + 1 < 8:
                    if rectLogicArray[blackKnight2.indexIOnLogicArray - 2][blackKnight2.indexJOnLogicArray + 1] >= 0:
                        eightMoves[0] = AdjustPositionAfterMove(blackKnight2.indexIOnLogicArray - 2, blackKnight2.indexJOnLogicArray + 1)
                else:
                        eightMoves[0] = (0,0)
                    # Left - Changing index J by 1
                if blackKnight2.indexIOnLogicArray - 2 >= 0 and blackKnight2.indexJOnLogicArray - 1 >= 0:
                    if rectLogicArray[blackKnight2.indexIOnLogicArray - 2][blackKnight2.indexJOnLogicArray - 1] >= 0:
                        eightMoves[7] = AdjustPositionAfterMove(blackKnight2.indexIOnLogicArray - 2, blackKnight2.indexJOnLogicArray - 1)
                else:
                        eightMoves[7] = (0,0)
                    
                # Right - Changing J index by 2
                
                    # Down - Changing I index by 1
                if blackKnight2.indexIOnLogicArray + 1 < 8 and blackKnight2.indexJOnLogicArray + 2 < 8:
                    if rectLogicArray[blackKnight2.indexIOnLogicArray + 1][blackKnight2.indexJOnLogicArray + 2] >= 0:
                        eightMoves[2] = AdjustPositionAfterMove(blackKnight2.indexIOnLogicArray + 1, blackKnight2.indexJOnLogicArray + 2)
                else:
                        eightMoves[2] = (0,0)
                    # Up - Changing I index by 1
                if blackKnight2.indexIOnLogicArray - 1 >= 0 and blackKnight2.indexJOnLogicArray + 2 < 8:
                    if rectLogicArray[blackKnight2.indexIOnLogicArray - 1][blackKnight2.indexJOnLogicArray + 2] >= 0:
                        eightMoves[1] = AdjustPositionAfterMove(blackKnight2.indexIOnLogicArray - 1, blackKnight2.indexJOnLogicArray + 2)
                else:
                        eightMoves[1] = (0,0)
                
                # Left - Changing J index by 2
                
                    # Down - Changing I index by 1
                if blackKnight2.indexIOnLogicArray + 1 < 8 and blackKnight2.indexJOnLogicArray - 2 >= 0:
                    if rectLogicArray[blackKnight2.indexIOnLogicArray + 1][blackKnight2.indexJOnLogicArray - 2] >= 0:
                        eightMoves[5] = AdjustPositionAfterMove(blackKnight2.indexIOnLogicArray + 1, blackKnight2.indexJOnLogicArray - 2)
                else:
                        eightMoves[5] = (0,0)
                    # Up - Changing I index by 1
                if blackKnight2.indexIOnLogicArray - 1 >= 0 and blackKnight2.indexJOnLogicArray - 2 >= 0:
                    if rectLogicArray[blackKnight2.indexIOnLogicArray - 1][blackKnight2.indexJOnLogicArray - 2] >= 0:
                        eightMoves[6] = AdjustPositionAfterMove(blackKnight2.indexIOnLogicArray - 1, blackKnight2.indexJOnLogicArray - 2)
                else:
                    eightMoves[6] = (0,0)
                        
                return eightMoves
         
def MovePositionOfKnight(turn, whichKnight, whereKnightCanMove, whereMouseIs):
    global switchTurn
    switchTurn = False
    
    if turn == 'white':
        
        if whichKnight == 1:
            if whereKnightCanMove != [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]: # If the movement list is not empty
                
                for x in range(0,8):
                    tileLetter, tileNumber = whereKnightCanMove[x]
                    if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs): # If where the mouse is alligns with potential moves
                        whiteKnight1.rect.x, whiteKnight1.rect.y = whereMouseIs # movement of the knight
                        CenterKnightInTile(turn, whichKnight) # ensures the knight is centered in its new tile
                        PiecesCollide(turn) # If it collides with a piece of opposite colour it removes them from the board
                        
                        if whiteKnight1.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)): # Ensures the movement of the knight is on the right tile
                            rectLogicArray[whiteKnight1.indexIOnLogicArray][whiteKnight1.indexJOnLogicArray] = 0 # Starting here the position of the knight is updated in the logic array
                            indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                            whiteKnight1.indexIOnLogicArray, whiteKnight1.indexJOnLogicArray = indexI, indexJ 
                            rectLogicArray[whiteKnight1.indexIOnLogicArray][whiteKnight1.indexJOnLogicArray] = 3 # Ends here
                            switchTurn = True
                            whiteKnight1.pos = whereKnightCanMove[x] # Updates position in the object
        
        elif whichKnight == 2:
            if whereKnightCanMove != [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]:
                
                for x in range(0,8):
                    tileLetter, tileNumber = whereKnightCanMove[x]
                    if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                        whiteKnight2.rect.x, whiteKnight2.rect.y = whereMouseIs
                        CenterKnightInTile(turn, whichKnight)
                        PiecesCollide(turn)
                        if whiteKnight2.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                            rectLogicArray[whiteKnight2.indexIOnLogicArray][whiteKnight2.indexJOnLogicArray] = 0
                            indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                            whiteKnight2.indexIOnLogicArray, whiteKnight2.indexJOnLogicArray = indexI, indexJ
                            rectLogicArray[whiteKnight2.indexIOnLogicArray][whiteKnight2.indexJOnLogicArray] = 3
                            switchTurn = True
                            whiteKnight2.pos = whereKnightCanMove
        
    if turn == 'black':
        
        if whichKnight == 1:
            if whereKnightCanMove != [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]:
                
                for x in range(0,8):
                    tileLetter, tileNumber = whereKnightCanMove[x]
                    if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                        blackKnight1.rect.x, blackKnight1.rect.y = whereMouseIs
                        CenterKnightInTile(turn, whichKnight)
                        PiecesCollide(turn)
                        if blackKnight1.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                            rectLogicArray[blackKnight1.indexIOnLogicArray][blackKnight1.indexJOnLogicArray] = 0
                            indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                            blackKnight1.indexIOnLogicArray, blackKnight1.indexJOnLogicArray = indexI, indexJ
                            rectLogicArray[blackKnight1.indexIOnLogicArray][blackKnight1.indexJOnLogicArray] = -3
                            switchTurn = True
                            blackKnight1.pos = whereKnightCanMove[x]
        
        elif whichKnight == 2:
            if whereKnightCanMove != [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]:
                
                for x in range(0,8):
                    tileLetter, tileNumber = whereKnightCanMove[x]
                    if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                        blackKnight2.rect.x, blackKnight2.rect.y = whereMouseIs
                        CenterKnightInTile(turn, whichKnight)
                        PiecesCollide(turn)
                        if blackKnight2.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                            rectLogicArray[blackKnight2.indexIOnLogicArray][blackKnight2.indexJOnLogicArray] = 0
                            indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                            blackKnight2.indexIOnLogicArray, blackKnight2.indexJOnLogicArray = indexI, indexJ
                            rectLogicArray[blackKnight2.indexIOnLogicArray][blackKnight2.indexJOnLogicArray] = -3
                            switchTurn = True
                            blackKnight2.pos = whereKnightCanMove
                  
# Bishop methods

def CreateWhiteBishops():
    global whiteBishop1, whiteBishop2
    
    # Creates 2 bishop objects
    # Initialised with their starting position and their position on the logic array
    whiteBishop1 =  chessPieces.Bishop("white", ("c", 1), 7, 2, True)
    whiteBishop2 = chessPieces.Bishop("white", ("f", 1), 7, 5, True)
    
def CreateBlackBishops():
    global blackBishop1, blackBishop2
    
    # Creates 2 bishop objects
    # Initialised with their starting position and their position on the logic array
    blackBishop1 =  chessPieces.Bishop("black", ("c", 8), 0, 2, True)
    blackBishop2 = chessPieces.Bishop("black", ("f", 8), 0, 5, True)
    
def PutAllBishipsOnTheBoard():
    
    # Ties the bishops surfaces and rects together and then puts them on the screen
    screen.blit(blackBishop1.surface, blackBishop1.rect)
    screen.blit(blackBishop2.surface, blackBishop2.rect)
    
    screen.blit(whiteBishop1.surface, whiteBishop1.rect)
    screen.blit(whiteBishop2.surface, whiteBishop2.rect)

def CollidingWithABishop(turn, whereMouseIs):
    # Detects if mouse is colliding with a piece
    if turn == 'white':
        if whiteBishop1.rect.collidepoint(whereMouseIs) or whiteBishop2.rect.collidepoint(whereMouseIs):
            return True
        else:
            return False
    elif turn == "black":
        if blackBishop1.rect.collidepoint(whereMouseIs) or blackBishop2.rect.collidepoint(whereMouseIs):     
            return True
        else:
            return False

def WhichBishopIsCollidedWith(turn, collidingWithBishop, whereMouseIs):
    # Detects which bishop the mouse is colliding with
    if turn == 'white':
        if whiteBishop1.rect.collidepoint(whereMouseIs):
            return 1
        elif whiteBishop2.rect.collidepoint(whereMouseIs):
            return 2
    elif turn == 'black':
        if blackBishop1.rect.collidepoint(whereMouseIs):
            return 1
        elif blackBishop2.rect.collidepoint(whereMouseIs):
            return 2

def CenterBishopInTile(turn, whichBishop):
    # Centers a piece in the tile they are currently on to reduce clustering
    if turn == 'white':
        if whichBishop == 1:
            if whiteBishop1.rect.collidelist(collisionList) == -1:
                return False
            else:
                whiteBishop1.rect.center = collisionList[whiteBishop1.rect.collidelist(collisionList)].center 
        elif whichBishop == 2:
            if whiteBishop2.rect.collidelist(collisionList) == -1:
                return False
            else:
                whiteBishop2.rect.center = collisionList[whiteBishop2.rect.collidelist(collisionList)].center
    elif turn == 'black':
        if whichBishop == 1:
            if blackBishop1.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackBishop1.rect.center = collisionList[blackBishop1.rect.collidelist(collisionList)].center 
        elif whichBishop == 2:
            if blackBishop2.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackBishop2.rect.center = collisionList[blackBishop2.rect.collidelist(collisionList)].center

def WhereCanBishopMove(turn, whichBishop, isABishop):
    # 7 is the most amount of moves a bishop can move in one direction at any time, with 4 directional possibilites
    # Therefore a list with 28 spaces is made
    
    # Organised in clockwise fashion with the first direction being topleft and last topright
    twentyEightMoves = [(0,0) for x in range(0,29)]
    
    if isABishop: # If it is a bishop as opposed to queen
        if turn == 'white':
            
            if whichBishop == 1:
                if whiteBishop1.onBoard:
                    # top-right direction
                    for x in range(1,8):
                        if whiteBishop1.indexIOnLogicArray - x  >= 0 and whiteBishop1.indexJOnLogicArray + x < 8: # Ensures the index does not exceed the range of the logic array
                            # If there is nothing blocking the bishops way then add it to potential moves
                            if rectLogicArray[whiteBishop1.indexIOnLogicArray - x][whiteBishop1.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteBishop1.indexIOnLogicArray - x, whiteBishop1.indexJOnLogicArray + x)
                            # If there is a piece of opposite colour in the space then add to potential moves and then stop adding moves in that direction
                            elif rectLogicArray[whiteBishop1.indexIOnLogicArray - x][whiteBishop1.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteBishop1.indexIOnLogicArray - x, whiteBishop1.indexJOnLogicArray + x)
                                break
                            else:
                                # If there is a piece of same colour in the space then stop adding moves in that direction
                                break
                    # bottom-right direction
                    for x in range(1,8):
                        if whiteBishop1.indexIOnLogicArray + x < 8 and whiteBishop1.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteBishop1.indexIOnLogicArray + x][whiteBishop1.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteBishop1.indexIOnLogicArray + x, whiteBishop1.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteBishop1.indexIOnLogicArray + x][whiteBishop1.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteBishop1.indexIOnLogicArray + x, whiteBishop1.indexJOnLogicArray + x)
                                break
                            else:
                                    break
                    # bottom-left direction
                    for x in range(1,8):
                        if whiteBishop1.indexIOnLogicArray + x < 8 and whiteBishop1.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteBishop1.indexIOnLogicArray + x][whiteBishop1.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteBishop1.indexIOnLogicArray + x, whiteBishop1.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteBishop1.indexIOnLogicArray + x][whiteBishop1.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteBishop1.indexIOnLogicArray + x, whiteBishop1.indexJOnLogicArray - x)
                                break
                            else:
                                    break
                    #top-left direction
                    for x in range(1,8):
                        if whiteBishop1.indexIOnLogicArray - x < 8 and whiteBishop1.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteBishop1.indexIOnLogicArray - x][whiteBishop1.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteBishop1.indexIOnLogicArray - x, whiteBishop1.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteBishop1.indexIOnLogicArray - x][whiteBishop1.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteBishop1.indexIOnLogicArray - x, whiteBishop1.indexJOnLogicArray - x)
                                break
                            else:
                                    break
                    
                    return twentyEightMoves

            elif whichBishop == 2:
                if whiteBishop2.onBoard:
                    # top-right direction
                    for x in range(1,8):
                        if whiteBishop2.indexIOnLogicArray - x  >= 0 and whiteBishop2.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteBishop2.indexIOnLogicArray - x][whiteBishop2.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteBishop2.indexIOnLogicArray - x, whiteBishop2.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteBishop2.indexIOnLogicArray - x][whiteBishop2.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteBishop2.indexIOnLogicArray - x, whiteBishop2.indexJOnLogicArray + x)
                                break
                            else:
                                    break
                    # bottom-right direction
                    for x in range(1,8):
                        if whiteBishop2.indexIOnLogicArray + x < 8 and whiteBishop2.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteBishop2.indexIOnLogicArray + x][whiteBishop2.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteBishop2.indexIOnLogicArray + x, whiteBishop2.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteBishop2.indexIOnLogicArray + x][whiteBishop2.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteBishop2.indexIOnLogicArray + x, whiteBishop2.indexJOnLogicArray + x)
                                break
                            else:
                                    break
                    # bottom-left direction
                    for x in range(1,8):
                        if whiteBishop2.indexIOnLogicArray + x < 8 and whiteBishop2.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteBishop2.indexIOnLogicArray + x][whiteBishop2.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteBishop2.indexIOnLogicArray + x, whiteBishop2.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteBishop2.indexIOnLogicArray + x][whiteBishop2.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteBishop2.indexIOnLogicArray + x, whiteBishop2.indexJOnLogicArray - x)
                                break
                            else:
                                    break
                    #top-left direction
                    for x in range(1,8):
                        if whiteBishop2.indexIOnLogicArray - x < 8 and whiteBishop2.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteBishop2.indexIOnLogicArray - x][whiteBishop2.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteBishop2.indexIOnLogicArray - x, whiteBishop2.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteBishop2.indexIOnLogicArray - x][whiteBishop2.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteBishop2.indexIOnLogicArray - x, whiteBishop2.indexJOnLogicArray - x)
                                break
                            else:
                                    break
                    return twentyEightMoves
        
        elif turn == 'black':
            
            if whichBishop == 1:
                if blackBishop1.onBoard:
                    # top-right direction
                    for x in range(1,8):
                        if blackBishop1.indexIOnLogicArray - x  >= 0 and blackBishop1.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackBishop1.indexIOnLogicArray - x][blackBishop1.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackBishop1.indexIOnLogicArray - x, blackBishop1.indexJOnLogicArray + x)
                            elif rectLogicArray[blackBishop1.indexIOnLogicArray - x][blackBishop1.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackBishop1.indexIOnLogicArray - x, blackBishop1.indexJOnLogicArray + x)
                                break
                            else:
                                    break
                    # bottom-right direction
                    for x in range(1,8):
                        if blackBishop1.indexIOnLogicArray + x < 8 and blackBishop1.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackBishop1.indexIOnLogicArray + x][blackBishop1.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackBishop1.indexIOnLogicArray + x, blackBishop1.indexJOnLogicArray + x)
                            elif rectLogicArray[blackBishop1.indexIOnLogicArray + x][blackBishop1.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackBishop1.indexIOnLogicArray + x, blackBishop1.indexJOnLogicArray + x)
                                break
                            else:
                                    break
                    # bottom-left direction
                    for x in range(1,8):
                        if blackBishop1.indexIOnLogicArray + x < 8 and blackBishop1.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackBishop1.indexIOnLogicArray + x][blackBishop1.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackBishop1.indexIOnLogicArray + x, blackBishop1.indexJOnLogicArray - x)
                            elif rectLogicArray[blackBishop1.indexIOnLogicArray + x][blackBishop1.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackBishop1.indexIOnLogicArray + x, blackBishop1.indexJOnLogicArray - x)
                                break
                            else:
                                    break
                    #top-left direction
                    for x in range(1,8):
                        if blackBishop1.indexIOnLogicArray - x < 8 and blackBishop1.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackBishop1.indexIOnLogicArray - x][blackBishop1.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackBishop1.indexIOnLogicArray - x, blackBishop1.indexJOnLogicArray - x)
                            elif rectLogicArray[blackBishop1.indexIOnLogicArray - x][blackBishop1.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackBishop1.indexIOnLogicArray - x, blackBishop1.indexJOnLogicArray - x)
                                break
                            else:
                                    break
                    
                    return twentyEightMoves

            elif whichBishop == 2:
                if blackBishop2.onBoard:
                    # top-right direction
                    for x in range(1,8):
                        if blackBishop2.indexIOnLogicArray - x  >= 0 and blackBishop2.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackBishop2.indexIOnLogicArray - x][blackBishop2.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackBishop2.indexIOnLogicArray - x, blackBishop2.indexJOnLogicArray + x)
                            elif rectLogicArray[blackBishop2.indexIOnLogicArray - x][blackBishop2.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackBishop2.indexIOnLogicArray - x, blackBishop2.indexJOnLogicArray + x)
                                break
                            else:
                                    break
                    # bottom-right direction
                    for x in range(1,8):
                        if blackBishop2.indexIOnLogicArray + x < 8 and blackBishop2.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackBishop2.indexIOnLogicArray + x][blackBishop2.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackBishop2.indexIOnLogicArray + x, blackBishop2.indexJOnLogicArray + x)
                            elif rectLogicArray[blackBishop2.indexIOnLogicArray + x][blackBishop2.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackBishop2.indexIOnLogicArray + x, blackBishop2.indexJOnLogicArray + x)
                                break
                            else:
                                    break
                    # bottom-left direction
                    for x in range(1,8):
                        if blackBishop2.indexIOnLogicArray + x < 8 and blackBishop2.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackBishop2.indexIOnLogicArray + x][blackBishop2.indexJOnLogicArray - x]  == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackBishop2.indexIOnLogicArray + x, blackBishop2.indexJOnLogicArray - x)
                            elif rectLogicArray[blackBishop2.indexIOnLogicArray + x][blackBishop2.indexJOnLogicArray - x]  > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackBishop2.indexIOnLogicArray + x, blackBishop2.indexJOnLogicArray - x)
                                break
                            else:
                                    break
                    #top-left direction
                    for x in range(1,8):
                        if blackBishop2.indexIOnLogicArray - x < 8 and blackBishop2.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackBishop2.indexIOnLogicArray - x][blackBishop2.indexJOnLogicArray - x]  == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackBishop2.indexIOnLogicArray - x, blackBishop2.indexJOnLogicArray - x)
                            elif rectLogicArray[blackBishop2.indexIOnLogicArray - x][blackBishop2.indexJOnLogicArray - x]  > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackBishop2.indexIOnLogicArray - x, blackBishop2.indexJOnLogicArray - x)
                                break
                            else:
                                    break
                    
                    return twentyEightMoves
    
    else: # In the scenario a queens moves are being determined
        # As it uses the same diagonal movement that a bishop does
        if turn == 'white':
            if whichBishop == 1:
                if whiteQueen1.onBoard:
                    # top-right direction
                    for x in range(1,8):
                        if whiteQueen1.indexIOnLogicArray - x  >= 0 and whiteQueen1.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen1.indexIOnLogicArray - x][whiteQueen1.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen1.indexIOnLogicArray - x, whiteQueen1.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen1.indexIOnLogicArray - x][whiteQueen1.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen1.indexIOnLogicArray - x, whiteQueen1.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-right direction
                    for x in range(1,8):
                        if whiteQueen1.indexIOnLogicArray + x < 8 and whiteQueen1.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen1.indexIOnLogicArray + x][whiteQueen1.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen1.indexIOnLogicArray + x, whiteQueen1.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen1.indexIOnLogicArray + x][whiteQueen1.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen1.indexIOnLogicArray + x, whiteQueen1.indexJOnLogicArray + x)
                            else:
                                break
                    # bottom-left direction
                    for x in range(1,8):
                        if whiteQueen1.indexIOnLogicArray + x < 8 and whiteQueen1.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen1.indexIOnLogicArray + x][whiteQueen1.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen1.indexIOnLogicArray + x, whiteQueen1.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen1.indexIOnLogicArray + x][whiteQueen1.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen1.indexIOnLogicArray + x, whiteQueen1.indexJOnLogicArray - x)
                            else:
                                break
                    #top-left direction
                    for x in range(1,8):
                        if whiteQueen1.indexIOnLogicArray - x < 8 and whiteQueen1.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen1.indexIOnLogicArray - x][whiteQueen1.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen1.indexIOnLogicArray - x, whiteQueen1.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen1.indexIOnLogicArray - x][whiteQueen1.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen1.indexIOnLogicArray - x, whiteQueen1.indexJOnLogicArray - x)
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichBishop == 2:
                if whiteQueen2.onBoard:
                
                    # top-right direction
                    for x in range(1,8):
                        if whiteQueen2.indexIOnLogicArray - x  >= 0 and whiteQueen2.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen2.indexIOnLogicArray - x][whiteQueen2.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen2.indexIOnLogicArray - x, whiteQueen2.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen2.indexIOnLogicArray - x][whiteQueen2.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen2.indexIOnLogicArray - x, whiteQueen2.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-right direction
                    for x in range(1,8):
                        if whiteQueen2.indexIOnLogicArray + x < 8 and whiteQueen2.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen2.indexIOnLogicArray + x][whiteQueen2.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen2.indexIOnLogicArray + x, whiteQueen2.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen2.indexIOnLogicArray + x][whiteQueen2.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen2.indexIOnLogicArray + x, whiteQueen2.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-left direction
                    for x in range(1,8):
                        if whiteQueen2.indexIOnLogicArray + x < 8 and whiteQueen2.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen2.indexIOnLogicArray + x][whiteQueen2.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen2.indexIOnLogicArray + x, whiteQueen2.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen2.indexIOnLogicArray + x][whiteQueen2.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen2.indexIOnLogicArray + x, whiteQueen2.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    #top-left direction
                    for x in range(1,8):
                        if whiteQueen2.indexIOnLogicArray - x < 8 and whiteQueen2.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen2.indexIOnLogicArray - x][whiteQueen2.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen2.indexIOnLogicArray - x, whiteQueen2.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen2.indexIOnLogicArray - x][whiteQueen2.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen2.indexIOnLogicArray - x, whiteQueen2.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichBishop == 3:
                if whiteQueen3.onBoard:
                
                    # top-right direction
                    for x in range(1,8):
                        if whiteQueen3.indexIOnLogicArray - x  >= 0 and whiteQueen3.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen3.indexIOnLogicArray - x][whiteQueen3.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen3.indexIOnLogicArray - x, whiteQueen3.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen3.indexIOnLogicArray - x][whiteQueen3.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen3.indexIOnLogicArray - x, whiteQueen3.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-right direction
                    for x in range(1,8):
                        if whiteQueen3.indexIOnLogicArray + x < 8 and whiteQueen3.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen3.indexIOnLogicArray + x][whiteQueen3.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen3.indexIOnLogicArray + x, whiteQueen3.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen3.indexIOnLogicArray + x][whiteQueen3.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen3.indexIOnLogicArray + x, whiteQueen3.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-left direction
                    for x in range(1,8):
                        if whiteQueen3.indexIOnLogicArray + x < 8 and whiteQueen3.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen3.indexIOnLogicArray + x][whiteQueen3.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen3.indexIOnLogicArray + x, whiteQueen3.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen3.indexIOnLogicArray + x][whiteQueen3.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen3.indexIOnLogicArray + x, whiteQueen3.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    #top-left direction
                    for x in range(1,8):
                        if whiteQueen3.indexIOnLogicArray - x < 8 and whiteQueen3.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen3.indexIOnLogicArray - x][whiteQueen3.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen3.indexIOnLogicArray - x, whiteQueen3.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen3.indexIOnLogicArray - x][whiteQueen3.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen3.indexIOnLogicArray - x, whiteQueen3.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichBishop == 4:
                if whiteQueen4.onBoard:
                
                    # top-right direction
                    for x in range(1,8):
                        if whiteQueen4.indexIOnLogicArray - x  >= 0 and whiteQueen4.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen4.indexIOnLogicArray - x][whiteQueen4.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen4.indexIOnLogicArray - x, whiteQueen4.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen4.indexIOnLogicArray - x][whiteQueen4.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen4.indexIOnLogicArray - x, whiteQueen4.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-right direction
                    for x in range(1,8):
                        if whiteQueen4.indexIOnLogicArray + x < 8 and whiteQueen4.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen4.indexIOnLogicArray + x][whiteQueen4.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen4.indexIOnLogicArray + x, whiteQueen4.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen4.indexIOnLogicArray + x][whiteQueen4.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen4.indexIOnLogicArray + x, whiteQueen4.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-left direction
                    for x in range(1,8):
                        if whiteQueen4.indexIOnLogicArray + x < 8 and whiteQueen4.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen4.indexIOnLogicArray + x][whiteQueen4.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen4.indexIOnLogicArray + x, whiteQueen4.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen4.indexIOnLogicArray + x][whiteQueen4.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen4.indexIOnLogicArray + x, whiteQueen4.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    #top-left direction
                    for x in range(1,8):
                        if whiteQueen4.indexIOnLogicArray - x < 8 and whiteQueen4.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen4.indexIOnLogicArray - x][whiteQueen4.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen4.indexIOnLogicArray - x, whiteQueen4.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen4.indexIOnLogicArray - x][whiteQueen4.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen4.indexIOnLogicArray - x, whiteQueen4.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichBishop == 5:
                if whiteQueen5.onBoard:
                
                    # top-right direction
                    for x in range(1,8):
                        if whiteQueen5.indexIOnLogicArray - x  >= 0 and whiteQueen5.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen5.indexIOnLogicArray - x][whiteQueen5.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen5.indexIOnLogicArray - x, whiteQueen5.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen5.indexIOnLogicArray - x][whiteQueen5.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen5.indexIOnLogicArray - x, whiteQueen5.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-right direction
                    for x in range(1,8):
                        if whiteQueen5.indexIOnLogicArray + x < 8 and whiteQueen5.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen5.indexIOnLogicArray + x][whiteQueen5.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen5.indexIOnLogicArray + x, whiteQueen5.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen5.indexIOnLogicArray + x][whiteQueen5.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen5.indexIOnLogicArray + x, whiteQueen5.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-left direction
                    for x in range(1,8):
                        if whiteQueen5.indexIOnLogicArray + x < 8 and whiteQueen5.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen5.indexIOnLogicArray + x][whiteQueen5.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen5.indexIOnLogicArray + x, whiteQueen5.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen5.indexIOnLogicArray + x][whiteQueen5.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen5.indexIOnLogicArray + x, whiteQueen5.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    #top-left direction
                    for x in range(1,8):
                        if whiteQueen5.indexIOnLogicArray - x < 8 and whiteQueen5.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen5.indexIOnLogicArray - x][whiteQueen5.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen5.indexIOnLogicArray - x, whiteQueen5.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen5.indexIOnLogicArray - x][whiteQueen5.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen5.indexIOnLogicArray - x, whiteQueen5.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichBishop == 6:
                if whiteQueen6.onBoard:
                
                    # top-right direction
                    for x in range(1,8):
                        if whiteQueen6.indexIOnLogicArray - x  >= 0 and whiteQueen6.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen6.indexIOnLogicArray - x][whiteQueen6.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen6.indexIOnLogicArray - x, whiteQueen6.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen6.indexIOnLogicArray - x][whiteQueen6.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen6.indexIOnLogicArray - x, whiteQueen6.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-right direction
                    for x in range(1,8):
                        if whiteQueen6.indexIOnLogicArray + x < 8 and whiteQueen6.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen6.indexIOnLogicArray + x][whiteQueen6.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen6.indexIOnLogicArray + x, whiteQueen6.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen6.indexIOnLogicArray + x][whiteQueen6.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen6.indexIOnLogicArray + x, whiteQueen6.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-left direction
                    for x in range(1,8):
                        if whiteQueen6.indexIOnLogicArray + x < 8 and whiteQueen6.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen6.indexIOnLogicArray + x][whiteQueen6.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen6.indexIOnLogicArray + x, whiteQueen6.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen6.indexIOnLogicArray + x][whiteQueen6.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen6.indexIOnLogicArray + x, whiteQueen6.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    #top-left direction
                    for x in range(1,8):
                        if whiteQueen6.indexIOnLogicArray - x < 8 and whiteQueen6.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen6.indexIOnLogicArray - x][whiteQueen6.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen6.indexIOnLogicArray - x, whiteQueen6.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen6.indexIOnLogicArray - x][whiteQueen6.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen6.indexIOnLogicArray - x, whiteQueen6.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichBishop == 7:
                if whiteQueen7.onBoard:
                
                    # top-right direction
                    for x in range(1,8):
                        if whiteQueen7.indexIOnLogicArray - x  >= 0 and whiteQueen7.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen7.indexIOnLogicArray - x][whiteQueen7.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen7.indexIOnLogicArray - x, whiteQueen7.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen7.indexIOnLogicArray - x][whiteQueen7.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen7.indexIOnLogicArray - x, whiteQueen7.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-right direction
                    for x in range(1,8):
                        if whiteQueen7.indexIOnLogicArray + x < 8 and whiteQueen7.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen7.indexIOnLogicArray + x][whiteQueen7.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen7.indexIOnLogicArray + x, whiteQueen7.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen7.indexIOnLogicArray + x][whiteQueen7.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen7.indexIOnLogicArray + x, whiteQueen7.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-left direction
                    for x in range(1,8):
                        if whiteQueen7.indexIOnLogicArray + x < 8 and whiteQueen7.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen7.indexIOnLogicArray + x][whiteQueen7.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen7.indexIOnLogicArray + x, whiteQueen7.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen7.indexIOnLogicArray + x][whiteQueen7.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen7.indexIOnLogicArray + x, whiteQueen7.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    #top-left direction
                    for x in range(1,8):
                        if whiteQueen7.indexIOnLogicArray - x < 8 and whiteQueen7.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen7.indexIOnLogicArray - x][whiteQueen7.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen7.indexIOnLogicArray - x, whiteQueen7.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen7.indexIOnLogicArray - x][whiteQueen7.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen7.indexIOnLogicArray - x, whiteQueen7.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichBishop == 8:
                if whiteQueen8.onBoard:
                
                    # top-right direction
                    for x in range(1,8):
                        if whiteQueen8.indexIOnLogicArray - x  >= 0 and whiteQueen8.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen8.indexIOnLogicArray - x][whiteQueen8.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen8.indexIOnLogicArray - x, whiteQueen8.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen8.indexIOnLogicArray - x][whiteQueen8.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen8.indexIOnLogicArray - x, whiteQueen8.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-right direction
                    for x in range(1,8):
                        if whiteQueen8.indexIOnLogicArray + x < 8 and whiteQueen8.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen8.indexIOnLogicArray + x][whiteQueen8.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen8.indexIOnLogicArray + x, whiteQueen8.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen8.indexIOnLogicArray + x][whiteQueen8.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen8.indexIOnLogicArray + x, whiteQueen8.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-left direction
                    for x in range(1,8):
                        if whiteQueen8.indexIOnLogicArray + x < 8 and whiteQueen8.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen8.indexIOnLogicArray + x][whiteQueen8.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen8.indexIOnLogicArray + x, whiteQueen8.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen8.indexIOnLogicArray + x][whiteQueen8.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen8.indexIOnLogicArray + x, whiteQueen8.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    #top-left direction
                    for x in range(1,8):
                        if whiteQueen8.indexIOnLogicArray - x < 8 and whiteQueen8.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen8.indexIOnLogicArray - x][whiteQueen8.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen8.indexIOnLogicArray - x, whiteQueen8.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen8.indexIOnLogicArray - x][whiteQueen8.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen8.indexIOnLogicArray - x, whiteQueen8.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichBishop == 9:
                if whiteQueen9.onBoard:
                
                    # top-right direction
                    for x in range(1,8):
                        if whiteQueen9.indexIOnLogicArray - x  >= 0 and whiteQueen9.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen9.indexIOnLogicArray - x][whiteQueen9.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen9.indexIOnLogicArray - x, whiteQueen9.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen9.indexIOnLogicArray - x][whiteQueen9.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(whiteQueen9.indexIOnLogicArray - x, whiteQueen9.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-right direction
                    for x in range(1,8):
                        if whiteQueen9.indexIOnLogicArray + x < 8 and whiteQueen9.indexJOnLogicArray + x < 8:
                            if rectLogicArray[whiteQueen9.indexIOnLogicArray + x][whiteQueen9.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen9.indexIOnLogicArray + x, whiteQueen9.indexJOnLogicArray + x)
                            elif rectLogicArray[whiteQueen9.indexIOnLogicArray + x][whiteQueen9.indexJOnLogicArray + x] < 1:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(whiteQueen9.indexIOnLogicArray + x, whiteQueen9.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-left direction
                    for x in range(1,8):
                        if whiteQueen9.indexIOnLogicArray + x < 8 and whiteQueen9.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen9.indexIOnLogicArray + x][whiteQueen9.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen9.indexIOnLogicArray + x, whiteQueen9.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen9.indexIOnLogicArray + x][whiteQueen9.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(whiteQueen9.indexIOnLogicArray + x, whiteQueen9.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    #top-left direction
                    for x in range(1,8):
                        if whiteQueen9.indexIOnLogicArray - x < 8 and whiteQueen9.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[whiteQueen9.indexIOnLogicArray - x][whiteQueen9.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen9.indexIOnLogicArray - x, whiteQueen9.indexJOnLogicArray - x)
                            elif rectLogicArray[whiteQueen9.indexIOnLogicArray - x][whiteQueen9.indexJOnLogicArray - x] < 1:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(whiteQueen9.indexIOnLogicArray - x, whiteQueen9.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
        
        elif turn == 'black':
            if whichBishop == 1:
                if blackQueen1.onBoard:
                
                    # top-right direction
                    for x in range(1,8):
                        if blackQueen1.indexIOnLogicArray - x  >= 0 and blackQueen1.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen1.indexIOnLogicArray - x][blackQueen1.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen1.indexIOnLogicArray - x, blackQueen1.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen1.indexIOnLogicArray - x][blackQueen1.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen1.indexIOnLogicArray - x, blackQueen1.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-right direction
                    for x in range(1,8):
                        if blackQueen1.indexIOnLogicArray + x < 8 and blackQueen1.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen1.indexIOnLogicArray + x][blackQueen1.indexJOnLogicArray + x]  == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen1.indexIOnLogicArray + x, blackQueen1.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen1.indexIOnLogicArray + x][blackQueen1.indexJOnLogicArray + x]  > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen1.indexIOnLogicArray + x, blackQueen1.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-left direction
                    for x in range(1,8):
                        if blackQueen1.indexIOnLogicArray + x < 8 and blackQueen1.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen1.indexIOnLogicArray + x][blackQueen1.indexJOnLogicArray - x]  == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen1.indexIOnLogicArray + x, blackQueen1.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen1.indexIOnLogicArray + x][blackQueen1.indexJOnLogicArray - x]  > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen1.indexIOnLogicArray + x, blackQueen1.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    #top-left direction
                    for x in range(1,8):
                        if blackQueen1.indexIOnLogicArray - x < 8 and blackQueen1.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen1.indexIOnLogicArray - x][blackQueen1.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen1.indexIOnLogicArray - x, blackQueen1.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen1.indexIOnLogicArray - x][blackQueen1.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen1.indexIOnLogicArray - x, blackQueen1.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichBishop == 2:
                if blackQueen2.onBoard:
                
                    # top-right direction
                    for x in range(1,8):
                        if blackQueen2.indexIOnLogicArray - x  >= 0 and blackQueen2.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen2.indexIOnLogicArray - x][blackQueen2.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen2.indexIOnLogicArray - x, blackQueen2.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen2.indexIOnLogicArray - x][blackQueen2.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen2.indexIOnLogicArray - x, blackQueen2.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-right direction
                    for x in range(1,8):
                        if blackQueen2.indexIOnLogicArray + x < 8 and blackQueen2.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen2.indexIOnLogicArray + x][blackQueen2.indexJOnLogicArray + x]  == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen2.indexIOnLogicArray + x, blackQueen2.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen2.indexIOnLogicArray + x][blackQueen2.indexJOnLogicArray + x]  > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen2.indexIOnLogicArray + x, blackQueen2.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-left direction
                    for x in range(1,8):
                        if blackQueen2.indexIOnLogicArray + x < 8 and blackQueen2.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen2.indexIOnLogicArray + x][blackQueen2.indexJOnLogicArray - x]  == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen2.indexIOnLogicArray + x, blackQueen2.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen2.indexIOnLogicArray + x][blackQueen2.indexJOnLogicArray - x]  > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen2.indexIOnLogicArray + x, blackQueen2.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    #top-left direction
                    for x in range(1,8):
                        if blackQueen2.indexIOnLogicArray - x < 8 and blackQueen2.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen2.indexIOnLogicArray - x][blackQueen2.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen2.indexIOnLogicArray - x, blackQueen2.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen2.indexIOnLogicArray - x][blackQueen2.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen2.indexIOnLogicArray - x, blackQueen2.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichBishop == 3:
                if blackQueen3.onBoard:
                
                    # top-right direction
                    for x in range(1,8):
                        if blackQueen3.indexIOnLogicArray - x  >= 0 and blackQueen3.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen3.indexIOnLogicArray - x][blackQueen3.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen3.indexIOnLogicArray - x, blackQueen3.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen3.indexIOnLogicArray - x][blackQueen3.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen3.indexIOnLogicArray - x, blackQueen3.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-right direction
                    for x in range(1,8):
                        if blackQueen3.indexIOnLogicArray + x < 8 and blackQueen3.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen3.indexIOnLogicArray + x][blackQueen3.indexJOnLogicArray + x]  == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen3.indexIOnLogicArray + x, blackQueen3.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen3.indexIOnLogicArray + x][blackQueen3.indexJOnLogicArray + x]  > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen3.indexIOnLogicArray + x, blackQueen3.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-left direction
                    for x in range(1,8):
                        if blackQueen3.indexIOnLogicArray + x < 8 and blackQueen3.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen3.indexIOnLogicArray + x][blackQueen3.indexJOnLogicArray - x]  == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen3.indexIOnLogicArray + x, blackQueen3.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen3.indexIOnLogicArray + x][blackQueen3.indexJOnLogicArray - x]  > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen3.indexIOnLogicArray + x, blackQueen3.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    #top-left direction
                    for x in range(1,8):
                        if blackQueen3.indexIOnLogicArray - x < 8 and blackQueen3.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen3.indexIOnLogicArray - x][blackQueen3.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen3.indexIOnLogicArray - x, blackQueen3.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen3.indexIOnLogicArray - x][blackQueen3.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen3.indexIOnLogicArray - x, blackQueen3.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichBishop == 4:
                if blackQueen4.onBoard:
                
                    # top-right direction
                    for x in range(1,8):
                        if blackQueen4.indexIOnLogicArray - x  >= 0 and blackQueen4.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen4.indexIOnLogicArray - x][blackQueen4.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen4.indexIOnLogicArray - x, blackQueen4.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen4.indexIOnLogicArray - x][blackQueen4.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen4.indexIOnLogicArray - x, blackQueen4.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-right direction
                    for x in range(1,8):
                        if blackQueen4.indexIOnLogicArray + x < 8 and blackQueen4.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen4.indexIOnLogicArray + x][blackQueen4.indexJOnLogicArray + x]  == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen4.indexIOnLogicArray + x, blackQueen4.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen4.indexIOnLogicArray + x][blackQueen4.indexJOnLogicArray + x]  > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen4.indexIOnLogicArray + x, blackQueen4.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-left direction
                    for x in range(1,8):
                        if blackQueen4.indexIOnLogicArray + x < 8 and blackQueen4.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen4.indexIOnLogicArray + x][blackQueen4.indexJOnLogicArray - x]  == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen4.indexIOnLogicArray + x, blackQueen4.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen4.indexIOnLogicArray + x][blackQueen4.indexJOnLogicArray - x]  > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen4.indexIOnLogicArray + x, blackQueen4.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    #top-left direction
                    for x in range(1,8):
                        if blackQueen4.indexIOnLogicArray - x < 8 and blackQueen4.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen4.indexIOnLogicArray - x][blackQueen4.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen4.indexIOnLogicArray - x, blackQueen4.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen4.indexIOnLogicArray - x][blackQueen4.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen4.indexIOnLogicArray - x, blackQueen4.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichBishop == 5:
                if blackQueen5.onBoard:
                
                    # top-right direction
                    for x in range(1,8):
                        if blackQueen5.indexIOnLogicArray - x  >= 0 and blackQueen5.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen5.indexIOnLogicArray - x][blackQueen5.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen5.indexIOnLogicArray - x, blackQueen5.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen5.indexIOnLogicArray - x][blackQueen5.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen5.indexIOnLogicArray - x, blackQueen5.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-right direction
                    for x in range(1,8):
                        if blackQueen5.indexIOnLogicArray + x < 8 and blackQueen5.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen5.indexIOnLogicArray + x][blackQueen5.indexJOnLogicArray + x]  == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen5.indexIOnLogicArray + x, blackQueen5.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen5.indexIOnLogicArray + x][blackQueen5.indexJOnLogicArray + x]  > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen5.indexIOnLogicArray + x, blackQueen5.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-left direction
                    for x in range(1,8):
                        if blackQueen5.indexIOnLogicArray + x < 8 and blackQueen5.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen5.indexIOnLogicArray + x][blackQueen5.indexJOnLogicArray - x]  == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen5.indexIOnLogicArray + x, blackQueen5.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen5.indexIOnLogicArray + x][blackQueen5.indexJOnLogicArray - x]  > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen5.indexIOnLogicArray + x, blackQueen5.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    #top-left direction
                    for x in range(1,8):
                        if blackQueen5.indexIOnLogicArray - x < 8 and blackQueen5.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen5.indexIOnLogicArray - x][blackQueen5.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen5.indexIOnLogicArray - x, blackQueen5.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen5.indexIOnLogicArray - x][blackQueen5.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen5.indexIOnLogicArray - x, blackQueen5.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichBishop == 6:
                if blackQueen6.onBoard:
                
                    # top-right direction
                    for x in range(1,8):
                        if blackQueen6.indexIOnLogicArray - x  >= 0 and blackQueen6.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen6.indexIOnLogicArray - x][blackQueen6.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen6.indexIOnLogicArray - x, blackQueen6.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen6.indexIOnLogicArray - x][blackQueen6.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen6.indexIOnLogicArray - x, blackQueen6.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-right direction
                    for x in range(1,8):
                        if blackQueen6.indexIOnLogicArray + x < 8 and blackQueen6.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen6.indexIOnLogicArray + x][blackQueen6.indexJOnLogicArray + x]  == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen6.indexIOnLogicArray + x, blackQueen6.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen6.indexIOnLogicArray + x][blackQueen6.indexJOnLogicArray + x]  > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen6.indexIOnLogicArray + x, blackQueen6.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-left direction
                    for x in range(1,8):
                        if blackQueen6.indexIOnLogicArray + x < 8 and blackQueen6.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen6.indexIOnLogicArray + x][blackQueen6.indexJOnLogicArray - x]  == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen6.indexIOnLogicArray + x, blackQueen6.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen6.indexIOnLogicArray + x][blackQueen6.indexJOnLogicArray - x]  > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen6.indexIOnLogicArray + x, blackQueen6.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    #top-left direction
                    for x in range(1,8):
                        if blackQueen6.indexIOnLogicArray - x < 8 and blackQueen6.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen6.indexIOnLogicArray - x][blackQueen6.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen6.indexIOnLogicArray - x, blackQueen6.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen6.indexIOnLogicArray - x][blackQueen6.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen6.indexIOnLogicArray - x, blackQueen6.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
                
            elif whichBishop == 7:
                if blackQueen7.onBoard:
                
                    # top-right direction
                    for x in range(1,8):
                        if blackQueen7.indexIOnLogicArray - x  >= 0 and blackQueen7.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen7.indexIOnLogicArray - x][blackQueen7.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen7.indexIOnLogicArray - x, blackQueen7.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen7.indexIOnLogicArray - x][blackQueen7.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen7.indexIOnLogicArray - x, blackQueen7.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-right direction
                    for x in range(1,8):
                        if blackQueen7.indexIOnLogicArray + x < 8 and blackQueen7.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen7.indexIOnLogicArray + x][blackQueen7.indexJOnLogicArray + x]  == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen7.indexIOnLogicArray + x, blackQueen7.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen7.indexIOnLogicArray + x][blackQueen7.indexJOnLogicArray + x]  > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen7.indexIOnLogicArray + x, blackQueen7.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-left direction
                    for x in range(1,8):
                        if blackQueen7.indexIOnLogicArray + x < 8 and blackQueen7.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen7.indexIOnLogicArray + x][blackQueen7.indexJOnLogicArray - x]  == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen7.indexIOnLogicArray + x, blackQueen7.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen7.indexIOnLogicArray + x][blackQueen7.indexJOnLogicArray - x]  > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen7.indexIOnLogicArray + x, blackQueen7.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    #top-left direction
                    for x in range(1,8):
                        if blackQueen7.indexIOnLogicArray - x < 8 and blackQueen7.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen7.indexIOnLogicArray - x][blackQueen7.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen7.indexIOnLogicArray - x, blackQueen7.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen7.indexIOnLogicArray - x][blackQueen7.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen7.indexIOnLogicArray - x, blackQueen7.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
            
            elif whichBishop == 8:
                if blackQueen8.onBoard:
                
                    # top-right direction
                    for x in range(1,8):
                        if blackQueen8.indexIOnLogicArray - x  >= 0 and blackQueen8.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen8.indexIOnLogicArray - x][blackQueen8.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen8.indexIOnLogicArray - x, blackQueen8.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen8.indexIOnLogicArray - x][blackQueen8.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen8.indexIOnLogicArray - x, blackQueen8.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-right direction
                    for x in range(1,8):
                        if blackQueen8.indexIOnLogicArray + x < 8 and blackQueen8.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen8.indexIOnLogicArray + x][blackQueen8.indexJOnLogicArray + x]  == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen8.indexIOnLogicArray + x, blackQueen8.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen8.indexIOnLogicArray + x][blackQueen8.indexJOnLogicArray + x]  > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen8.indexIOnLogicArray + x, blackQueen8.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-left direction
                    for x in range(1,8):
                        if blackQueen8.indexIOnLogicArray + x < 8 and blackQueen8.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen8.indexIOnLogicArray + x][blackQueen8.indexJOnLogicArray - x]  == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen8.indexIOnLogicArray + x, blackQueen8.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen8.indexIOnLogicArray + x][blackQueen8.indexJOnLogicArray - x]  > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen8.indexIOnLogicArray + x, blackQueen8.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    #top-left direction
                    for x in range(1,8):
                        if blackQueen8.indexIOnLogicArray - x < 8 and blackQueen8.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen8.indexIOnLogicArray - x][blackQueen8.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen8.indexIOnLogicArray - x, blackQueen8.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen8.indexIOnLogicArray - x][blackQueen8.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen8.indexIOnLogicArray - x, blackQueen8.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    return twentyEightMoves
            
            elif whichBishop == 9:
                if blackQueen9.onBoard:
                
                    # top-right direction
                    for x in range(1,8):
                        if blackQueen9.indexIOnLogicArray - x  >= 0 and blackQueen9.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen9.indexIOnLogicArray - x][blackQueen9.indexJOnLogicArray + x] == 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen9.indexIOnLogicArray - x, blackQueen9.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen9.indexIOnLogicArray - x][blackQueen9.indexJOnLogicArray + x] > 0:
                                twentyEightMoves[x-1] = AdjustPositionAfterMove(blackQueen9.indexIOnLogicArray - x, blackQueen9.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-right direction
                    for x in range(1,8):
                        if blackQueen9.indexIOnLogicArray + x < 8 and blackQueen9.indexJOnLogicArray + x < 8:
                            if rectLogicArray[blackQueen9.indexIOnLogicArray + x][blackQueen9.indexJOnLogicArray + x]  == 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen9.indexIOnLogicArray + x, blackQueen9.indexJOnLogicArray + x)
                            elif rectLogicArray[blackQueen9.indexIOnLogicArray + x][blackQueen9.indexJOnLogicArray + x]  > 0:
                                twentyEightMoves[x-1+7] = AdjustPositionAfterMove(blackQueen9.indexIOnLogicArray + x, blackQueen9.indexJOnLogicArray + x)
                                break
                            else:
                                break
                    # bottom-left direction
                    for x in range(1,8):
                        if blackQueen9.indexIOnLogicArray + x < 8 and blackQueen9.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen9.indexIOnLogicArray + x][blackQueen9.indexJOnLogicArray - x]  == 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen9.indexIOnLogicArray + x, blackQueen9.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen9.indexIOnLogicArray + x][blackQueen9.indexJOnLogicArray - x]  > 0:
                                twentyEightMoves[x-1+14] = AdjustPositionAfterMove(blackQueen9.indexIOnLogicArray + x, blackQueen9.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    #top-left direction
                    for x in range(1,8):
                        if blackQueen9.indexIOnLogicArray - x < 8 and blackQueen9.indexJOnLogicArray - x >= 0:
                            if rectLogicArray[blackQueen9.indexIOnLogicArray - x][blackQueen9.indexJOnLogicArray - x] == 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen9.indexIOnLogicArray - x, blackQueen9.indexJOnLogicArray - x)
                            elif rectLogicArray[blackQueen9.indexIOnLogicArray - x][blackQueen9.indexJOnLogicArray - x] > 0:
                                twentyEightMoves[x-1+21] = AdjustPositionAfterMove(blackQueen9.indexIOnLogicArray - x, blackQueen9.indexJOnLogicArray - x)
                                break
                            else:
                                break
                    
                    return twentyEightMoves
                       
def MovePositionOfBishop(turn, whichBishop, whereBishopCanMove, whereMouseIs):
    global switchTurn
    switchTurn = False
    if turn == 'white':
        
        if whichBishop == 1:
            
            if whereBishopCanMove != [(0,0) for x in range(0, len(whereBishopCanMove))]: # If the movement list is not empty
                for x in range(0,len(whereBishopCanMove)):
                    if whereBishopCanMove[x]:
                        tileLetter, tileNumber = whereBishopCanMove[x]           
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs): # If where the mouse is alligns with potential moves
                            whiteBishop1.rect.x, whiteBishop1.rect.y = whereMouseIs # movement of the bishop
                            CenterBishopInTile(turn, whichBishop) # ensures the bishop is centered in its new tile
                            PiecesCollide(turn) # If it collides with a piece of opposite colour it removes them from the board
                            
                            if whiteBishop1.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)): # Ensures the movement of the bishop is on the right tile
                                rectLogicArray[whiteBishop1.indexIOnLogicArray][whiteBishop1.indexJOnLogicArray] = 0 # Starting here the position of the bishop is updated in the logic array
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                whiteBishop1.indexIOnLogicArray, whiteBishop1.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[whiteBishop1.indexIOnLogicArray][whiteBishop1.indexJOnLogicArray] = 4 # Ends here
                                switchTurn = True
                                whiteBishop1.pos = whereBishopCanMove # Updates position in the object
        
        elif whichBishop == 2:
            
            if whereBishopCanMove != [(0,0) for x in range(0,len(whereBishopCanMove))]:
                for x in range(0,len(whereBishopCanMove)):
                    if whereBishopCanMove[x]:
                        tileLetter, tileNumber = whereBishopCanMove[x]           
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            whiteBishop2.rect.x, whiteBishop2.rect.y = whereMouseIs
                            CenterBishopInTile(turn, whichBishop)
                            PiecesCollide(turn)
                            if whiteBishop2.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[whiteBishop2.indexIOnLogicArray][whiteBishop2.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                whiteBishop2.indexIOnLogicArray, whiteBishop2.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[whiteBishop2.indexIOnLogicArray][whiteBishop2.indexJOnLogicArray] = 4
                                switchTurn = True
                                whiteBishop2.pos = whereBishopCanMove
    elif turn == 'black':
        
        if whichBishop == 1:
            
            if whereBishopCanMove != [(0,0) for x in range(0,len(whereBishopCanMove))]:
                for x in range(0,len(whereBishopCanMove)):
                    if whereBishopCanMove[x]:
                        tileLetter, tileNumber = whereBishopCanMove[x]           
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            blackBishop1.rect.x, blackBishop1.rect.y = whereMouseIs
                            CenterBishopInTile(turn, whichBishop)
                            PiecesCollide(turn)
                            if blackBishop1.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[blackBishop1.indexIOnLogicArray][blackBishop1.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                blackBishop1.indexIOnLogicArray, blackBishop1.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[blackBishop1.indexIOnLogicArray][blackBishop1.indexJOnLogicArray] = -4
                                switchTurn = True
                                blackBishop1.pos = whereBishopCanMove
        
        elif whichBishop == 2:
            
            if whereBishopCanMove != [(0,0) for x in range(0,len(whereBishopCanMove))]:
                for x in range(0,len(whereBishopCanMove)):
                    if whereBishopCanMove[x]:
                        tileLetter, tileNumber = whereBishopCanMove[x]           
                        if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                            blackBishop2.rect.x, blackBishop2.rect.y = whereMouseIs
                            CenterBishopInTile(turn, whichBishop)
                            PiecesCollide(turn)
                            if blackBishop2.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                rectLogicArray[blackBishop2.indexIOnLogicArray][blackBishop2.indexJOnLogicArray] = 0
                                indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                blackBishop2.indexIOnLogicArray, blackBishop2.indexJOnLogicArray = indexI, indexJ
                                rectLogicArray[blackBishop2.indexIOnLogicArray][blackBishop2.indexJOnLogicArray] = -4
                                switchTurn = True
                                blackBishop2.pos = whereBishopCanMove
    
# King methods
               
def CreateWhiteKing():
    global whiteKing
    
    # Creates a king object
    # Initialised with it's starting position and it's position on the logic array
    whiteKing = chessPieces.King("white", ("e", 1), 7, 4, True)
    
def CreateBlackKing():
    global blackKing
    
    # Creates a king object
    # Initialised with it's starting position and it's position on the logic array
    blackKing = chessPieces.King("black", ("e", 8), 0, 4, True)
    
def PutAllTheKingsOnTheBoard():
    
    # Ties the kings surfaces to their rects and puts them on screen
    screen.blit(blackKing.surface, blackKing.rect)
    
    screen.blit(whiteKing.surface, whiteKing.rect)

def CollidingWithAKing(turn, whereMouseIs):
    # Detects if mouse is colliding with a piece
    if turn == 'white':
        if whiteKing.rect.collidepoint(whereMouseIs):
            return True
        else:
            return False
    elif turn == "black":
        if blackKing.rect.collidepoint(whereMouseIs):
            return True
        else:
            return False

def CenterKingInTile(turn):
    # Centers a piece in the tile they are currently on to reduce clustering
    if turn == 'white':
        if whiteKing.rect.collidelist(collisionList) == -1:
                return False
        else:
            whiteKing.rect.center = collisionList[whiteKing.rect.collidelist(collisionList)].center
    elif turn == 'black':
        if blackKing.rect.collidelist(collisionList) == -1:
                return False
        else:
            blackKing.rect.center = collisionList[blackKing.rect.collidelist(collisionList)].center

def WhereCanKingMove(turn):
    # Kings can move 1 space in all directions, there are 8 directions
    # Organised in clockwise fashion from top to topleft
    oneMoveInEachDirection = [(0,0)for x in range(0,8)]
    
    if turn == 'white':
        # top
            if whiteKing.indexIOnLogicArray - 1 >= 0:
                if rectLogicArray[whiteKing.indexIOnLogicArray - 1][whiteKing.indexJOnLogicArray] < 1:
                    oneMoveInEachDirection[0] = AdjustPositionAfterMove(whiteKing.indexIOnLogicArray - 1, whiteKing.indexJOnLogicArray )
        # top-right
            if whiteKing.indexIOnLogicArray - 1 >= 0 and whiteKing.indexJOnLogicArray + 1 < 8:
                if rectLogicArray[whiteKing.indexIOnLogicArray - 1][whiteKing.indexJOnLogicArray + 1] < 1:
                    oneMoveInEachDirection[1] = AdjustPositionAfterMove(whiteKing.indexIOnLogicArray - 1, whiteKing.indexJOnLogicArray + 1)
        # right
            if whiteKing.indexJOnLogicArray + 1 < 8:
                if rectLogicArray[whiteKing.indexIOnLogicArray][whiteKing.indexJOnLogicArray + 1] < 1:
                    oneMoveInEachDirection[2] = AdjustPositionAfterMove(whiteKing.indexIOnLogicArray, whiteKing.indexJOnLogicArray + 1)
        # bottom-right
            if whiteKing.indexIOnLogicArray + 1 < 8 and whiteKing.indexJOnLogicArray + 1 < 8:
                if rectLogicArray[whiteKing.indexIOnLogicArray + 1][whiteKing.indexJOnLogicArray + 1] < 1:
                    oneMoveInEachDirection[3] = AdjustPositionAfterMove(whiteKing.indexIOnLogicArray + 1, whiteKing.indexJOnLogicArray + 1)
        # bottom
            if whiteKing.indexIOnLogicArray + 1 < 8:
                if rectLogicArray[whiteKing.indexIOnLogicArray + 1][whiteKing.indexJOnLogicArray] < 1:
                    oneMoveInEachDirection[4] = AdjustPositionAfterMove(whiteKing.indexIOnLogicArray + 1, whiteKing.indexJOnLogicArray )
        # bottom-left
            if whiteKing.indexIOnLogicArray + 1 < 8 and whiteKing.indexJOnLogicArray - 1 >= 0:
                if rectLogicArray[whiteKing.indexIOnLogicArray + 1][whiteKing.indexJOnLogicArray - 1] < 1:
                    oneMoveInEachDirection[5] = AdjustPositionAfterMove(whiteKing.indexIOnLogicArray + 1, whiteKing.indexJOnLogicArray - 1)
        # left
            if whiteKing.indexJOnLogicArray - 1 >= 0:
                if rectLogicArray[whiteKing.indexIOnLogicArray][whiteKing.indexJOnLogicArray - 1] < 1:
                    oneMoveInEachDirection[6] = AdjustPositionAfterMove(whiteKing.indexIOnLogicArray, whiteKing.indexJOnLogicArray - 1)
        # top-left
            if whiteKing.indexIOnLogicArray - 1 >= 0 and whiteKing.indexJOnLogicArray - 1 >= 0:
                if rectLogicArray[whiteKing.indexIOnLogicArray - 1][whiteKing.indexJOnLogicArray - 1] < 1:
                    oneMoveInEachDirection[7] = AdjustPositionAfterMove(whiteKing.indexIOnLogicArray - 1, whiteKing.indexJOnLogicArray - 1)

            return oneMoveInEachDirection
    
    elif turn == 'black':
        # top
            if blackKing.indexIOnLogicArray - 1 >= 0:
                if rectLogicArray[blackKing.indexIOnLogicArray - 1][blackKing.indexJOnLogicArray] >= 0:
                    oneMoveInEachDirection[0] = AdjustPositionAfterMove(blackKing.indexIOnLogicArray - 1, blackKing.indexJOnLogicArray )
        # top-right
            if blackKing.indexIOnLogicArray - 1 >= 0 and blackKing.indexJOnLogicArray + 1 < 8:
                if rectLogicArray[blackKing.indexIOnLogicArray - 1][blackKing.indexJOnLogicArray + 1] >= 0:
                    oneMoveInEachDirection[1] = AdjustPositionAfterMove(blackKing.indexIOnLogicArray - 1, blackKing.indexJOnLogicArray + 1)
        # right
            if blackKing.indexJOnLogicArray + 1 < 8:
                if rectLogicArray[blackKing.indexIOnLogicArray][blackKing.indexJOnLogicArray + 1] >= 0:
                    oneMoveInEachDirection[2] = AdjustPositionAfterMove(blackKing.indexIOnLogicArray, blackKing.indexJOnLogicArray + 1)
        # bottom-right
            if blackKing.indexIOnLogicArray + 1 < 8 and blackKing.indexJOnLogicArray + 1 < 8:
                if rectLogicArray[blackKing.indexIOnLogicArray + 1][blackKing.indexJOnLogicArray + 1] >= 0:
                    oneMoveInEachDirection[3] = AdjustPositionAfterMove(blackKing.indexIOnLogicArray + 1, blackKing.indexJOnLogicArray + 1)
        # bottom
            if blackKing.indexIOnLogicArray + 1 < 8:
                if rectLogicArray[blackKing.indexIOnLogicArray + 1][blackKing.indexJOnLogicArray] >= 0:
                    oneMoveInEachDirection[4] = AdjustPositionAfterMove(blackKing.indexIOnLogicArray + 1, blackKing.indexJOnLogicArray )
        # bottom-left
            if blackKing.indexIOnLogicArray + 1 < 8 and blackKing.indexJOnLogicArray - 1 >= 0:
                if rectLogicArray[blackKing.indexIOnLogicArray + 1][blackKing.indexJOnLogicArray - 1] >= 0:
                    oneMoveInEachDirection[5] = AdjustPositionAfterMove(blackKing.indexIOnLogicArray + 1, blackKing.indexJOnLogicArray - 1)
        # left
            if blackKing.indexJOnLogicArray - 1 >= 0:
                if rectLogicArray[blackKing.indexIOnLogicArray][blackKing.indexJOnLogicArray - 1] >= 0:
                    oneMoveInEachDirection[6] = AdjustPositionAfterMove(blackKing.indexIOnLogicArray, blackKing.indexJOnLogicArray - 1)
        # top-left
            if blackKing.indexIOnLogicArray - 1 >= 0 and blackKing.indexJOnLogicArray - 1 >= 0:
                if rectLogicArray[blackKing.indexIOnLogicArray - 1][blackKing.indexJOnLogicArray - 1] >= 0:
                    oneMoveInEachDirection[7] = AdjustPositionAfterMove(blackKing.indexIOnLogicArray - 1, blackKing.indexJOnLogicArray - 1)

            return oneMoveInEachDirection

def MovePositionOfKing(turn, whereKingCanMove, whereMouseIs):
    global switchTurn
    switchTurn = False
    
    if turn == 'white':
        if whereKingCanMove != [(0,0) for x in range(0,8)]: # If the movement list is not empty
            
            for x in range(0,8):
                tileLetter, tileNumber = whereKingCanMove[x]
                if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs): # If where the mouse is alligns with potential moves
                    whiteKing.rect.x, whiteKing.rect.y = whereMouseIs # movement of the bishop
                    CenterKingInTile(turn) # ensures the bishop is centered in its new tile
                    PiecesCollide(turn) # If it collides with a piece of opposite colour it removes them from the board
                    
                    if whiteKing.rect.colliderect(LocatingTheTileRects(tileLetter, tileNumber)):  # Ensures the movement of the bishop is on the right tile
                        rectLogicArray[whiteKing.indexIOnLogicArray][whiteKing.indexJOnLogicArray] = 0 # Starting here the position of the bishop is updated in the logic array
                        indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                        whiteKing.indexIOnLogicArray, whiteKing.indexJOnLogicArray =  indexI, indexJ
                        rectLogicArray[whiteKing.indexIOnLogicArray][whiteKing.indexJOnLogicArray] = 6 # Ends here
                        switchTurn = True
                        whiteKing.pos = whereKingCanMove[x] # Updates position in the object
    
    elif turn == 'black':
        if whereKingCanMove != [(0,0) for x in range(0,8)]:
            
            for x in range(0,8):
                tileLetter, tileNumber = whereKingCanMove[x]
                if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                    blackKing.rect.x, blackKing.rect.y = whereMouseIs
                    CenterKingInTile(turn)
                    PiecesCollide(turn)
                    if blackKing.rect.colliderect(LocatingTheTileRects(tileLetter, tileNumber)):
                        rectLogicArray[blackKing.indexIOnLogicArray][blackKing.indexJOnLogicArray] = 0
                        indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                        blackKing.indexIOnLogicArray, blackKing.indexJOnLogicArray =  indexI, indexJ
                        rectLogicArray[blackKing.indexIOnLogicArray][blackKing.indexJOnLogicArray] = 6
                        switchTurn = True
                        blackKing.pos = whereKingCanMove[x]

# Queen methods

def CreateWhiteQueen():
    global whiteQueen9
     # 9 used for the main queen
     
    whiteQueen9 = chessPieces.Queen("white", ("d", 1), 7, 3, True)
    
def CreateBlackQueen():
    global blackQueen9
    # 9 used for the main queen
    
    blackQueen9 = chessPieces.Queen("black", ("d", 8), 0, 3, True)
    
def PutAllTheQueensOnTheBoard():
    
    screen.blit(blackQueen9.surface, blackQueen9.rect)
    screen.blit(whiteQueen9.surface, whiteQueen9.rect)

def CollidingWithAQueen(turn, whereMouseIs):
    if turn == 'white':
        if whiteQueen9.rect.collidepoint(whereMouseIs) or whiteQueen1.rect.collidepoint(whereMouseIs) or whiteQueen2.rect.collidepoint(whereMouseIs) or whiteQueen3.rect.collidepoint(whereMouseIs) or whiteQueen4.rect.collidepoint(whereMouseIs) or whiteQueen5.rect.collidepoint(whereMouseIs) or whiteQueen6.rect.collidepoint(whereMouseIs) or whiteQueen7.rect.collidepoint(whereMouseIs) or whiteQueen8.rect.collidepoint(whereMouseIs):
            return True
        else:
            return False
        
    elif turn == "black":
        if blackQueen9.rect.collidepoint(whereMouseIs) or blackQueen1.rect.collidepoint(whereMouseIs) or blackQueen2.rect.collidepoint(whereMouseIs) or blackQueen3.rect.collidepoint(whereMouseIs) or blackQueen4.rect.collidepoint(whereMouseIs) or blackQueen5.rect.collidepoint(whereMouseIs) or blackQueen6.rect.collidepoint(whereMouseIs) or blackQueen7.rect.collidepoint(whereMouseIs) or blackQueen8.rect.collidepoint(whereMouseIs):
            return True
        else:
            return False

def WhichQueenIsCollidedWith(turn, whereMouseIs):
     # If all pawns promote there can be a total of 9 queens on each side 
     # This method locates which one the mouse is on
        if turn == "white":
            if whiteQueen1.rect.collidepoint(whereMouseIs):
                return 1
            if whiteQueen2.rect.collidepoint(whereMouseIs):
                return 2
            if whiteQueen3.rect.collidepoint(whereMouseIs):
                return 3
            if whiteQueen4.rect.collidepoint(whereMouseIs):
                return 4
            if whiteQueen5.rect.collidepoint(whereMouseIs):
                return 5
            if whiteQueen6.rect.collidepoint(whereMouseIs):
                return 6
            if whiteQueen7.rect.collidepoint(whereMouseIs):
                return 7
            if whiteQueen8.rect.collidepoint(whereMouseIs):
                return 8
            if whiteQueen9.rect.collidepoint(whereMouseIs):
                return 9
        elif turn == "black":
            if blackQueen1.rect.collidepoint(whereMouseIs):
                return 1
            if blackQueen2.rect.collidepoint(whereMouseIs):
                return 2
            if blackQueen3.rect.collidepoint(whereMouseIs):
                return 3
            if blackQueen4.rect.collidepoint(whereMouseIs):
                return 4
            if blackQueen5.rect.collidepoint(whereMouseIs):
                return 5
            if blackQueen6.rect.collidepoint(whereMouseIs):
                return 6
            if blackQueen7.rect.collidepoint(whereMouseIs):
                return 7
            if blackQueen8.rect.collidepoint(whereMouseIs):
                return 8
            if blackQueen9.rect.collidepoint(whereMouseIs):
                return 9
    
def CenterQueenInTile(turn, whichQueen):
    # Centers a piece in the tile they are currently on to reduce clustering
    if turn == 'white':
        if whichQueen == 1:
            if whiteQueen1.rect.collidelist(collisionList) == -1:
                return False
            else:
                whiteQueen1.rect.center = collisionList[whiteQueen1.rect.collidelist(collisionList)].center 
        elif whichQueen == 2:
            if whiteQueen2.rect.collidelist(collisionList) == -1:
                return False
            else:
                whiteQueen2.rect.center = collisionList[whiteQueen2.rect.collidelist(collisionList)].center 
        elif whichQueen == 3:
            if whiteQueen3.rect.collidelist(collisionList) == -1:
                return False
            else:
                whiteQueen3.rect.center = collisionList[whiteQueen3.rect.collidelist(collisionList)].center 
        elif whichQueen == 4:
            if whiteQueen4.rect.collidelist(collisionList) == -1:
                return False
            else:
                whiteQueen4.rect.center = collisionList[whiteQueen4.rect.collidelist(collisionList)].center 
        elif whichQueen == 5:
            if whiteQueen5.rect.collidelist(collisionList) == -1:
                return False
            else:
                whiteQueen5.rect.center = collisionList[whiteQueen5.rect.collidelist(collisionList)].center 
        elif whichQueen == 6:
            if whiteQueen6.rect.collidelist(collisionList) == -1:
                return False
            else:
                whiteQueen6.rect.center = collisionList[whiteQueen6.rect.collidelist(collisionList)].center 
        elif whichQueen == 7:
            if whiteQueen7.rect.collidelist(collisionList) == -1:
                return False
            else:
                whiteQueen7.rect.center = collisionList[whiteQueen7.rect.collidelist(collisionList)].center 
        elif whichQueen == 8:
            if whiteQueen8.rect.collidelist(collisionList) == -1:
                return False
            else:
                whiteQueen8.rect.center = collisionList[whiteQueen8.rect.collidelist(collisionList)].center 
        elif whichQueen == 9:
            if whiteQueen9.rect.collidelist(collisionList) == -1:
                return False
            else:
                whiteQueen9.rect.center = collisionList[whiteQueen9.rect.collidelist(collisionList)].center 
    elif turn == 'black':
        if whichQueen == 1:
            if blackQueen1.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackQueen1.rect.center = collisionList[blackQueen1.rect.collidelist(collisionList)].center 
        elif whichQueen == 2:
            if blackQueen2.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackQueen2.rect.center = collisionList[blackQueen2.rect.collidelist(collisionList)].center 
        elif whichQueen == 3:
            if blackQueen3.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackQueen3.rect.center = collisionList[blackQueen3.rect.collidelist(collisionList)].center 
        elif whichQueen == 4:
            if blackQueen4.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackQueen4.rect.center = collisionList[blackQueen4.rect.collidelist(collisionList)].center 
        elif whichQueen == 5:
            if blackQueen5.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackQueen5.rect.center = collisionList[blackQueen5.rect.collidelist(collisionList)].center 
        elif whichQueen == 6:
            if blackQueen6.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackQueen6.rect.center = collisionList[blackQueen6.rect.collidelist(collisionList)].center 
        elif whichQueen == 7:
            if blackQueen7.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackQueen7.rect.center = collisionList[blackQueen7.rect.collidelist(collisionList)].center 
        elif whichQueen == 8:
            if blackQueen8.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackQueen8.rect.center = collisionList[blackQueen8.rect.collidelist(collisionList)].center 
        elif whichQueen == 9:
            if blackQueen9.rect.collidelist(collisionList) == -1:
                return False
            else:
                blackQueen9.rect.center = collisionList[blackQueen9.rect.collidelist(collisionList)].center 

def WhereCanQueenMove(turn, whichQueen):
    # This method combines the possible moves of a queen diagonally and linearly
    # Diagonal moves come from the bishop move method and linear from the castle method
    if turn == 'white':
        queenDiagonalMoves = WhereCanBishopMove(turn, whichQueen, False)
        queenLinearMoves =  WhereCanCastleMove(turn, whichQueen, False)
        if queenDiagonalMoves !=  None and queenLinearMoves != None: # Ensuring that None cannot be returned
            allQueenMoves = queenDiagonalMoves + queenLinearMoves
            return allQueenMoves
    
        elif queenDiagonalMoves == None and queenLinearMoves != None:
            allQueenMoves = queenLinearMoves 
            return allQueenMoves
            
        elif queenDiagonalMoves != None and queenLinearMoves == None:
            allQueenMoves = queenDiagonalMoves 
            return allQueenMoves
    
    elif turn == 'black':
        queenDiagonalMoves =  WhereCanBishopMove(turn, whichQueen, False)
        queenLinearMoves =  WhereCanCastleMove(turn, whichQueen, False)
        if queenDiagonalMoves !=  None and queenLinearMoves != None:
            allQueenMoves = queenDiagonalMoves + queenLinearMoves
            return allQueenMoves
    
        elif queenDiagonalMoves == None and queenLinearMoves != None:
            allQueenMoves = queenLinearMoves
            return allQueenMoves
            
        elif queenDiagonalMoves != None and queenLinearMoves == None:
            allQueenMoves = queenDiagonalMoves
            return allQueenMoves

def MovePositionOfQueen(turn, whereQueenCanMove, whichQueen, whereMouseIs):
    global switchTurn
    switchTurn = False
    
    if turn == 'white':
        if whichQueen == 1:
            if whereQueenCanMove != [(0,0) for l in range(0,len(whereQueenCanMove))]: 
                # Loops through all the potential moves of a queen, using the len method to get the amount of moves
                # Len is necessary as there are alot of possible moves and it fluctuates alot so set integers is not as efficient
                for x in range(0,len(whereQueenCanMove)):
                    if whereQueenCanMove[x]:
                            tileLetter, tileNumber = whereQueenCanMove[x]           
                            if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs): # If where the mouse is alligns with potential moves
                                whiteQueen1.rect.x, whiteQueen1.rect.y = whereMouseIs # movement of the queen
                                CenterQueenInTile(turn, whichQueen) # ensures the queen is centered in its new tile
                                PiecesCollide(turn) # If it collides with a piece of opposite colour it removes them from the board, put into the movement method so the moved,
                                # piece is not taken as well as the stationary one
                                
                                if whiteQueen1.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)): # Ensures the movement of the pawn is on the right tile
                                    rectLogicArray[whiteQueen1.indexIOnLogicArray][whiteQueen1.indexJOnLogicArray] = 0  # Starting here the position of the pawn is updated in the logic array
                                    indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                    whiteQueen1.indexIOnLogicArray, whiteQueen1.indexJOnLogicArray = indexI, indexJ
                                    rectLogicArray[whiteQueen1.indexIOnLogicArray][whiteQueen1.indexJOnLogicArray] = 5 # Ending here
                                    switchTurn = True # Signals to switch turn
                                    whiteQueen1.pos = whereQueenCanMove[x] # Updates the pos of the object
                    
        elif whichQueen == 2:
            if whereQueenCanMove != [(0,0) for l in range(0,len(whereQueenCanMove))]:
                
                for x in range(0,len(whereQueenCanMove)):
                    if whereQueenCanMove[x]:
                            tileLetter, tileNumber = whereQueenCanMove[x]           
                            if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                                whiteQueen2.rect.x, whiteQueen2.rect.y = whereMouseIs
                                CenterQueenInTile(turn, whichQueen)
                                PiecesCollide(turn)
                                if whiteQueen2.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                    rectLogicArray[whiteQueen2.indexIOnLogicArray][whiteQueen2.indexJOnLogicArray] = 0
                                    indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                    whiteQueen2.indexIOnLogicArray, whiteQueen2.indexJOnLogicArray = indexI, indexJ
                                    rectLogicArray[whiteQueen2.indexIOnLogicArray][whiteQueen2.indexJOnLogicArray] = 5
                                    switchTurn = True
                                    whiteQueen2.pos = whereQueenCanMove[x]
        
        elif whichQueen == 3:
            if whereQueenCanMove != [(0,0) for l in range(0,len(whereQueenCanMove))]:
                
                for x in range(0,len(whereQueenCanMove)):
                    if whereQueenCanMove[x]:
                            tileLetter, tileNumber = whereQueenCanMove[x]           
                            if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                                whiteQueen3.rect.x, whiteQueen3.rect.y = whereMouseIs
                                CenterQueenInTile(turn, whichQueen)
                                PiecesCollide(turn)
                                if whiteQueen3.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                    rectLogicArray[whiteQueen3.indexIOnLogicArray][whiteQueen3.indexJOnLogicArray] = 0
                                    indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                    whiteQueen3.indexIOnLogicArray, whiteQueen3.indexJOnLogicArray = indexI, indexJ
                                    rectLogicArray[whiteQueen3.indexIOnLogicArray][whiteQueen3.indexJOnLogicArray] = 5
                                    switchTurn = True
                                    whiteQueen3.pos = whereQueenCanMove[x]
        
        elif whichQueen == 4:
            if whereQueenCanMove != [(0,0) for l in range(0,len(whereQueenCanMove))]:
                
                for x in range(0,len(whereQueenCanMove)):
                    if whereQueenCanMove[x]:
                            tileLetter, tileNumber = whereQueenCanMove[x]           
                            if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                                whiteQueen4.rect.x, whiteQueen4.rect.y = whereMouseIs
                                CenterQueenInTile(turn, whichQueen)
                                PiecesCollide(turn)
                                if whiteQueen4.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                    rectLogicArray[whiteQueen4.indexIOnLogicArray][whiteQueen4.indexJOnLogicArray] = 0
                                    indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                    whiteQueen4.indexIOnLogicArray, whiteQueen4.indexJOnLogicArray = indexI, indexJ
                                    rectLogicArray[whiteQueen4.indexIOnLogicArray][whiteQueen4.indexJOnLogicArray] = 5
                                    switchTurn = True
                                    whiteQueen4.pos = whereQueenCanMove[x]
        
        elif whichQueen == 5:
            if whereQueenCanMove != [(0,0) for l in range(0,len(whereQueenCanMove))]:
                
                for x in range(0,len(whereQueenCanMove)):
                    if whereQueenCanMove[x]:
                            tileLetter, tileNumber = whereQueenCanMove[x]           
                            if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                                whiteQueen5.rect.x, whiteQueen5.rect.y = whereMouseIs
                                CenterQueenInTile(turn, whichQueen)
                                PiecesCollide(turn)
                                if whiteQueen5.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                    rectLogicArray[whiteQueen5.indexIOnLogicArray][whiteQueen5.indexJOnLogicArray] = 0
                                    indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                    whiteQueen5.indexIOnLogicArray, whiteQueen5.indexJOnLogicArray = indexI, indexJ
                                    rectLogicArray[whiteQueen5.indexIOnLogicArray][whiteQueen5.indexJOnLogicArray] = 5
                                    switchTurn = True
                                    whiteQueen5.pos = whereQueenCanMove[x]
        
        elif whichQueen == 6:
            if whereQueenCanMove != [(0,0) for l in range(0,len(whereQueenCanMove))]:
                
                for x in range(0,len(whereQueenCanMove)):
                    if whereQueenCanMove[x]:
                            tileLetter, tileNumber = whereQueenCanMove[x]           
                            if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                                whiteQueen6.rect.x, whiteQueen6.rect.y = whereMouseIs
                                CenterQueenInTile(turn, whichQueen)
                                PiecesCollide(turn)
                                if whiteQueen6.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                    rectLogicArray[whiteQueen6.indexIOnLogicArray][whiteQueen6.indexJOnLogicArray] = 0
                                    indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                    whiteQueen6.indexIOnLogicArray, whiteQueen6.indexJOnLogicArray = indexI, indexJ
                                    rectLogicArray[whiteQueen6.indexIOnLogicArray][whiteQueen6.indexJOnLogicArray] = 5
                                    switchTurn = True
                                    whiteQueen6.pos = whereQueenCanMove[x]
        
        elif whichQueen == 7:
            if whereQueenCanMove != [(0,0) for l in range(0,len(whereQueenCanMove))]:
                
                for x in range(0,len(whereQueenCanMove)):
                    if whereQueenCanMove[x]:
                            tileLetter, tileNumber = whereQueenCanMove[x]           
                            if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                                whiteQueen7.rect.x, whiteQueen7.rect.y = whereMouseIs
                                CenterQueenInTile(turn, whichQueen)
                                PiecesCollide(turn)
                                if whiteQueen7.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                    rectLogicArray[whiteQueen7.indexIOnLogicArray][whiteQueen7.indexJOnLogicArray] = 0
                                    indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                    whiteQueen7.indexIOnLogicArray, whiteQueen7.indexJOnLogicArray = indexI, indexJ
                                    rectLogicArray[whiteQueen7.indexIOnLogicArray][whiteQueen7.indexJOnLogicArray] = 5
                                    switchTurn = True
                                    whiteQueen7.pos = whereQueenCanMove[x]
        
        elif whichQueen == 8:
            if whereQueenCanMove != [[(0,0) for l in range(0,len(whereQueenCanMove))]]:
                
                for x in range(0,len(whereQueenCanMove)):
                    if whereQueenCanMove[x]:
                            tileLetter, tileNumber = whereQueenCanMove[x]           
                            if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                                whiteQueen8.rect.x, whiteQueen8.rect.y = whereMouseIs
                                CenterQueenInTile(turn, whichQueen)
                                PiecesCollide(turn)
                                if whiteQueen8.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                    rectLogicArray[whiteQueen8.indexIOnLogicArray][whiteQueen8.indexJOnLogicArray] = 0
                                    indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                    whiteQueen8.indexIOnLogicArray, whiteQueen8.indexJOnLogicArray = indexI, indexJ
                                    rectLogicArray[whiteQueen8.indexIOnLogicArray][whiteQueen8.indexJOnLogicArray] = 5
                                    switchTurn = True
                                    whiteQueen8.pos = whereQueenCanMove[x]
                                  
        elif whichQueen == 9:
            if whereQueenCanMove != [(0,0) for l in range(0,len(whereQueenCanMove))]:
                
                for x in range(0,len(whereQueenCanMove)):
                    if whereQueenCanMove[x]:
                            tileLetter, tileNumber = whereQueenCanMove[x]           
                            if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                                whiteQueen9.rect.x, whiteQueen9.rect.y = whereMouseIs
                                CenterQueenInTile(turn, whichQueen)
                                PiecesCollide(turn)
                                if whiteQueen9.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                    rectLogicArray[whiteQueen9.indexIOnLogicArray][whiteQueen9.indexJOnLogicArray] = 0
                                    indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                    whiteQueen9.indexIOnLogicArray, whiteQueen9.indexJOnLogicArray = indexI, indexJ
                                    rectLogicArray[whiteQueen9.indexIOnLogicArray][whiteQueen9.indexJOnLogicArray] = 5
                                    switchTurn = True
                                    whiteQueen9.pos = whereQueenCanMove[x]                  
                
                    
    elif turn == 'black':
        if whichQueen == 1:
            if whereQueenCanMove != [(0,0) for l in range(0,len(whereQueenCanMove))]:
                
                for x in range(0,len(whereQueenCanMove)):
                    if whereQueenCanMove[x]:
                            tileLetter, tileNumber = whereQueenCanMove[x]           
                            if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                                blackQueen1.rect.x, blackQueen1.rect.y = whereMouseIs
                                CenterQueenInTile(turn, whichQueen)
                                PiecesCollide(turn)
                                if blackQueen1.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                    rectLogicArray[blackQueen1.indexIOnLogicArray][blackQueen1.indexJOnLogicArray] = 0
                                    indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                    blackQueen1.indexIOnLogicArray, blackQueen1.indexJOnLogicArray = indexI, indexJ
                                    rectLogicArray[blackQueen1.indexIOnLogicArray][blackQueen1.indexJOnLogicArray] = -5
                                    switchTurn = True
                                    blackQueen1.pos = whereQueenCanMove[x]
        
        elif whichQueen == 2:
            if whereQueenCanMove != [(0,0) for l in range(0,len(whereQueenCanMove))]:
                
                for x in range(0,len(whereQueenCanMove)):
                    if whereQueenCanMove[x]:
                            tileLetter, tileNumber = whereQueenCanMove[x]           
                            if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                                blackQueen2.rect.x, blackQueen2.rect.y = whereMouseIs
                                CenterQueenInTile(turn, whichQueen)
                                PiecesCollide(turn)
                                if blackQueen2.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                    rectLogicArray[blackQueen2.indexIOnLogicArray][blackQueen2.indexJOnLogicArray] = 0
                                    indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                    blackQueen2.indexIOnLogicArray, blackQueen2.indexJOnLogicArray = indexI, indexJ
                                    rectLogicArray[blackQueen2.indexIOnLogicArray][blackQueen2.indexJOnLogicArray] = -5
                                    switchTurn = True
                                    blackQueen2.pos = whereQueenCanMove[x]
        
        elif whichQueen == 3:
            if whereQueenCanMove != [(0,0) for l in range(0,len(whereQueenCanMove))]:
                
                for x in range(0,len(whereQueenCanMove)):
                    if whereQueenCanMove[x]:
                            tileLetter, tileNumber = whereQueenCanMove[x]           
                            if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                                blackQueen3.rect.x, blackQueen3.rect.y = whereMouseIs
                                CenterQueenInTile(turn, whichQueen)
                                PiecesCollide(turn)
                                if blackQueen3.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                    rectLogicArray[blackQueen3.indexIOnLogicArray][blackQueen3.indexJOnLogicArray] = 0
                                    indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                    blackQueen3.indexIOnLogicArray, blackQueen3.indexJOnLogicArray = indexI, indexJ
                                    rectLogicArray[blackQueen3.indexIOnLogicArray][blackQueen3.indexJOnLogicArray] = -5
                                    switchTurn = True
                                    blackQueen3.pos = whereQueenCanMove[x]
        
        elif whichQueen == 4:
            if whereQueenCanMove != [(0,0) for l in range(0,len(whereQueenCanMove))]:
                
                for x in range(0,len(whereQueenCanMove)):
                    if whereQueenCanMove[x]:
                            tileLetter, tileNumber = whereQueenCanMove[x]           
                            if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                                blackQueen4.rect.x, blackQueen4.rect.y = whereMouseIs
                                CenterQueenInTile(turn, whichQueen)
                                PiecesCollide(turn)
                                if blackQueen4.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                    rectLogicArray[blackQueen4.indexIOnLogicArray][blackQueen4.indexJOnLogicArray] = 0
                                    indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                    blackQueen4.indexIOnLogicArray, blackQueen4.indexJOnLogicArray = indexI, indexJ
                                    rectLogicArray[blackQueen4.indexIOnLogicArray][blackQueen4.indexJOnLogicArray] = -5
                                    switchTurn = True
                                    blackQueen4.pos = whereQueenCanMove[x]
        
        elif whichQueen == 5:
            if whereQueenCanMove != [(0,0) for l in range(0,len(whereQueenCanMove))]:
                
                for x in range(0,len(whereQueenCanMove)):
                    if whereQueenCanMove[x]:
                            tileLetter, tileNumber = whereQueenCanMove[x]           
                            if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                                blackQueen5.rect.x, blackQueen5.rect.y = whereMouseIs
                                CenterQueenInTile(turn, whichQueen)
                                PiecesCollide(turn)
                                if blackQueen5.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                    rectLogicArray[blackQueen5.indexIOnLogicArray][blackQueen5.indexJOnLogicArray] = 0
                                    indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                    blackQueen5.indexIOnLogicArray, blackQueen5.indexJOnLogicArray = indexI, indexJ
                                    rectLogicArray[blackQueen5.indexIOnLogicArray][blackQueen5.indexJOnLogicArray] = -5
                                    switchTurn = True
                                    blackQueen5.pos = whereQueenCanMove[x]
        
        elif whichQueen == 6:
            if whereQueenCanMove != [(0,0) for l in range(0,len(whereQueenCanMove))]:
                
                for x in range(0,len(whereQueenCanMove)):
                    if whereQueenCanMove[x]:
                            tileLetter, tileNumber = whereQueenCanMove[x]           
                            if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                                blackQueen6.rect.x, blackQueen6.rect.y = whereMouseIs
                                CenterQueenInTile(turn, whichQueen)
                                PiecesCollide(turn)
                                if blackQueen6.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                    rectLogicArray[blackQueen6.indexIOnLogicArray][blackQueen6.indexJOnLogicArray] = 0
                                    indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                    blackQueen6.indexIOnLogicArray, blackQueen6.indexJOnLogicArray = indexI, indexJ
                                    rectLogicArray[blackQueen6.indexIOnLogicArray][blackQueen6.indexJOnLogicArray] = -5
                                    switchTurn = True
                                    blackQueen6.pos = whereQueenCanMove[x]
        
        elif whichQueen == 7:
            if whereQueenCanMove != [(0,0) for l in range(0,len(whereQueenCanMove))]:
                
                for x in range(0,len(whereQueenCanMove)):
                    if whereQueenCanMove[x]:
                            tileLetter, tileNumber = whereQueenCanMove[x]           
                            if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                                blackQueen7.rect.x, blackQueen7.rect.y = whereMouseIs
                                CenterQueenInTile(turn, whichQueen)
                                PiecesCollide(turn)
                                if blackQueen7.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                    rectLogicArray[blackQueen7.indexIOnLogicArray][blackQueen7.indexJOnLogicArray] = 0
                                    indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                    blackQueen7.indexIOnLogicArray, blackQueen7.indexJOnLogicArray = indexI, indexJ
                                    rectLogicArray[blackQueen7.indexIOnLogicArray][blackQueen7.indexJOnLogicArray] = -5
                                    switchTurn = True
                                    blackQueen7.pos = whereQueenCanMove[x]
        
        elif whichQueen == 8:
            if whereQueenCanMove != [(0,0) for l in range(0,len(whereQueenCanMove))]:
                
                for x in range(0,len(whereQueenCanMove)):
                    if whereQueenCanMove[x]:
                            tileLetter, tileNumber = whereQueenCanMove[x]           
                            if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                                blackQueen8.rect.x, blackQueen8.rect.y = whereMouseIs
                                CenterQueenInTile(turn, whichQueen)
                                PiecesCollide(turn)
                                if blackQueen8.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                    rectLogicArray[blackQueen8.indexIOnLogicArray][blackQueen8.indexJOnLogicArray] = 0
                                    indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                    blackQueen8.indexIOnLogicArray, blackQueen8.indexJOnLogicArray = indexI, indexJ
                                    rectLogicArray[blackQueen8.indexIOnLogicArray][blackQueen8.indexJOnLogicArray] = -5
                                    switchTurn = True
                                    blackQueen8.pos = whereQueenCanMove[x]
        
        elif whichQueen == 9:
            if whereQueenCanMove != [(0,0) for l in range(0,len(whereQueenCanMove))]:
                
                for x in range(0,len(whereQueenCanMove)):
                    if whereQueenCanMove[x]:
                            tileLetter, tileNumber = whereQueenCanMove[x]           
                            if LocatingTheTileRects(tileLetter,tileNumber).collidepoint(whereMouseIs):
                                blackQueen9.rect.x, blackQueen9.rect.y = whereMouseIs
                                CenterQueenInTile(turn, whichQueen)
                                PiecesCollide(turn)
                                if blackQueen9.rect.colliderect(LocatingTheTileRects(tileLetter,tileNumber)):
                                    rectLogicArray[blackQueen9.indexIOnLogicArray][blackQueen9.indexJOnLogicArray] = 0
                                    indexI, indexJ = FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber)
                                    blackQueen9.indexIOnLogicArray, blackQueen9.indexJOnLogicArray = indexI, indexJ
                                    rectLogicArray[blackQueen9.indexIOnLogicArray][blackQueen9.indexJOnLogicArray] = -5
                                    switchTurn = True
                                    blackQueen9.pos = whereQueenCanMove[x]
    

def PutPiecesOnTheBoard():
    # Combines putting the pieces on the board to one method
    PutAllPawnsOnTheBoard()
    PutAllCastlesOnTheBoard()
    PutAllKnightsOnTheBoard()
    PutAllBishipsOnTheBoard()
    PutAllTheKingsOnTheBoard()
    PutAllTheQueensOnTheBoard()
    PutPromotedQueensOnTheBoard()
    
#  End of Piece methods

def DrawBoardBorder():
    # Draws a rect border around the board to prevent the pieces from leaving the board
    pygame.draw.rect(screen, (0,0,0), board.rect, width = 2)
    
def DrawTilePositions():
    # Draws the numbers and letters that sit beside the board
    gamefont = pygame.font.Font("freesansbold.ttf", 32)
    
    tilePositionA = gamefont.render("a", False, (0,0,0))
    tilePositionB = gamefont.render("b", False, (0,0,0))
    tilePositionC = gamefont.render("c", False, (0,0,0))
    tilePositionD = gamefont.render("d", False, (0,0,0))
    tilePositionE = gamefont.render("e", False, (0,0,0))
    tilePositionF = gamefont.render("f", False, (0,0,0))
    tilePositionG = gamefont.render("g", False, (0,0,0))
    tilePositionH = gamefont.render("h", False, (0,0,0))
    
    screen.blit(tilePositionA, (140,50))
    screen.blit(tilePositionB, (240,50))
    screen.blit(tilePositionC, (340,50))
    screen.blit(tilePositionD, (440,50))
    screen.blit(tilePositionE, (540,50))
    screen.blit(tilePositionF, (640,50))
    screen.blit(tilePositionG, (740,50))
    screen.blit(tilePositionH, (840,50))
    
    tilePosition1 = gamefont.render("1", False, (0,0,0))
    tilePosition2 = gamefont.render("2", False, (0,0,0))
    tilePosition3 = gamefont.render("3", False, (0,0,0))
    tilePosition4 = gamefont.render("4", False, (0,0,0))
    tilePosition5 = gamefont.render("5", False, (0,0,0))
    tilePosition6 = gamefont.render("6", False, (0,0,0))
    tilePosition7 = gamefont.render("7", False, (0,0,0))
    tilePosition8 = gamefont.render("8", False, (0,0,0))
    
    screen.blit(tilePosition1, (50,840))
    screen.blit(tilePosition2, (50,740))
    screen.blit(tilePosition3, (50,640))
    screen.blit(tilePosition4, (50,540))
    screen.blit(tilePosition5, (50,440))
    screen.blit(tilePosition6, (50,340))
    screen.blit(tilePosition7, (50,240))
    screen.blit(tilePosition8, (50,140))

def CheckIfMouseIsWithinBoardBorder(whereMouseIs):
    if board.rect.collidepoint(whereMouseIs):
        return True
    else:
        return False

# Declaring of rectangles that are used to detect pieces on tiles
whiteA8 = pygame.Rect(100,100,100,100)
blackB8 = pygame.Rect(200,100,100,100)
whiteC8 = pygame.Rect(300,100,100,100)
blackD8 = pygame.Rect(400,100,100,100)
whiteE8 = pygame.Rect(500,100,100,100)
blackF8 = pygame.Rect(600,100,100,100)
whiteG8 = pygame.Rect(700,100,100,100)
blackH8 = pygame.Rect(800,100,100,100)
    
blackA7 = pygame.Rect(100,200,100,100)
whiteB7 = pygame.Rect(200,200,100,100)
blackC7 = pygame.Rect(300,200,100,100)
whiteD7 = pygame.Rect(400,200,100,100)
blackE7 = pygame.Rect(500,200,100,100)
whiteF7 = pygame.Rect(600,200,100,100)
blackG7 = pygame.Rect(700,200,100,100)
whiteH7 = pygame.Rect(800,200,100,100)
    
whiteA6 = pygame.Rect(100,300,100,100)
blackB6 = pygame.Rect(200,300,100,100)
whiteC6 = pygame.Rect(300,300,100,100)
blackD6 = pygame.Rect(400,300,100,100)
whiteE6 = pygame.Rect(500,300,100,100)
blackF6 = pygame.Rect(600,300,100,100)
whiteG6 = pygame.Rect(700,300,100,100)
blackH6 = pygame.Rect(800,300,100,100)
    
blackA5 = pygame.Rect(100,400,100,100)
whiteB5 = pygame.Rect(200,400,100,100)
blackC5 = pygame.Rect(300,400,100,100)
whiteD5 = pygame.Rect(400,400,100,100)
blackE5 = pygame.Rect(500,400,100,100)
whiteF5 = pygame.Rect(600,400,100,100)
blackG5 = pygame.Rect(700,400,100,100)
whiteH5 = pygame.Rect(800,400,100,100)
    
whiteA4= pygame.Rect(100,500,100,100)
blackB4 = pygame.Rect(200,500,100,100)
whiteC4 = pygame.Rect(300,500,100,100)
blackD4 = pygame.Rect(400,500,100,100)
whiteE4 = pygame.Rect(500,500,100,100)
blackF4 = pygame.Rect(600,500,100,100)
whiteG4 = pygame.Rect(700,500,100,100)
blackH4 = pygame.Rect(800,500,100,100)
    
blackA3 = pygame.Rect(100,600,100,100)
whiteB3 = pygame.Rect(200,600,100,100)
blackC3 = pygame.Rect(300,600,100,100)
whiteD3 = pygame.Rect(400,600,100,100)
blackE3 = pygame.Rect(500,600,100,100)
whiteF3 = pygame.Rect(600,600,100,100)
blackG3 = pygame.Rect(700,600,100,100)
whiteH3 = pygame.Rect(800,600,100,100)
    
whiteA2 = pygame.Rect(100,700,100,100)
blackB2 = pygame.Rect(200,700,100,100)
whiteC2 = pygame.Rect(300,700,100,100)
blackD2 = pygame.Rect(400,700,100,100)
whiteE2 = pygame.Rect(500,700,100,100)
blackF2 = pygame.Rect(600,700,100,100)
whiteG2 = pygame.Rect(700,700,100,100)
blackH2 = pygame.Rect(800,700,100,100)
    
blackA1 = pygame.Rect(100,800,100,100)
whiteB1 = pygame.Rect(200,800,100,100)
blackC1 = pygame.Rect(300,800,100,100)
whiteD1 = pygame.Rect(400,800,100,100)
blackE1 = pygame.Rect(500,800,100,100)
whiteF1 = pygame.Rect(600,800,100,100)
blackG1 = pygame.Rect(700,800,100,100)
whiteH1 = pygame.Rect(800,800,100,100)
    
collisionList = [ 

whiteA8, blackB8, whiteC8, blackD8, whiteE8, blackF8, whiteG8, blackH8,
    
blackA7,whiteB7,blackC7,whiteD7,blackE7,whiteF7,blackG7,whiteH7,
    
whiteA6,blackB6,whiteC6,blackD6,whiteE6,blackF6,whiteG6,blackH6,
    
blackA5,whiteB5,blackC5,whiteD5,blackE5,whiteF5,blackG5,whiteH5,
    
whiteA4,blackB4,whiteC4,blackD4,whiteE4,blackF4,whiteG4,blackH4,
    
blackA3,whiteB3,blackC3,whiteD3,blackE3,whiteF3,blackG3,whiteH3,
    
whiteA2,blackB2,whiteC2,blackD2,whiteE2,blackF2,whiteG2,blackH2,
    
blackA1,whiteB1,blackC1,whiteD1,blackE1,whiteF1,blackG1,whiteH1

]

        
# Methods and variables for the board

# 0 = Empty space
# 1 = pawn -1 if black
# 2 = castle -2 if black
# 3 = knight -3 if black    
# 4 = bishop -4 if black
# 5 = queen -5 if black
# 6 = king -6 if black

rectLogicArray = [[-2,-3,-4,-5,-6,-4,-3,-2],
                  [-1,-1,-1,-1,-1,-1,-1,-1],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [1,1,1,1,1,1,1,1],
                  [2,3,4,5,6,4,3,2]]

row8 = row  
row7 = row
row6 = row
row5 = row 
row4 = row
row3 = row
row2 = row
row1 = row

         
def LocatingTheTileRects(tileLetter, tileNumber):
    # Takes the tileLetter and tileNumber and outputs the rect of the tile 
    if tileLetter == 'a':
        if tileNumber == 1:
            return blackA1
        if tileNumber == 2:
            return whiteA2
        if tileNumber == 3:
            return blackA3
        if tileNumber == 4:
            return whiteA4
        if tileNumber == 5:
            return blackA5
        if tileNumber == 6:
            return whiteA6
        if tileNumber == 7:
            return blackA7
        if tileNumber == 8:
            return whiteA8
        
    if tileLetter == 'b':
        if tileNumber == 1:
            return whiteB1
        if tileNumber == 2:
            return blackB2
        if tileNumber == 3:
            return whiteB3
        if tileNumber == 4:
            return blackB4
        if tileNumber == 5:
            return whiteB5
        if tileNumber == 6:
            return blackB6
        if tileNumber == 7:
            return whiteB7
        if tileNumber == 8:
            return blackB8
    
    if tileLetter == 'c':
        if tileNumber == 1:
            return blackC1
        if tileNumber == 2:
            return whiteC2
        if tileNumber == 3:
            return blackC3
        if tileNumber == 4:
            return whiteC4
        if tileNumber == 5:
            return blackC5
        if tileNumber == 6:
            return whiteC6
        if tileNumber == 7:
            return blackC7
        if tileNumber == 8:
            return whiteC8
    
    if tileLetter == 'd':
        if tileNumber == 1:
            return whiteD1
        if tileNumber == 2:
            return blackD2
        if tileNumber == 3:
            return whiteD3
        if tileNumber == 4:
            return blackD4
        if tileNumber == 5:
            return whiteD5
        if tileNumber == 6:
            return blackD6
        if tileNumber == 7:
            return whiteD7
        if tileNumber == 8:
            return blackD8
        
    if tileLetter == 'e':
        if tileNumber == 1:
            return blackE1
        if tileNumber == 2:
            return whiteE2
        if tileNumber == 3:
            return blackE3
        if tileNumber == 4:
            return whiteE4
        if tileNumber == 5:
            return blackE5
        if tileNumber == 6:
            return whiteE6
        if tileNumber == 7:
            return blackE7
        if tileNumber == 8:
            return whiteE8
         
    if tileLetter == 'f':
        if tileNumber == 1:
            return whiteF1
        if tileNumber == 2:
            return blackF2
        if tileNumber == 3:
            return whiteF3
        if tileNumber == 4:
            return blackF4
        if tileNumber == 5:
            return whiteF5
        if tileNumber == 6:
            return blackF6
        if tileNumber == 7:
            return whiteF7
        if tileNumber == 8:
            return blackF8
        
    if tileLetter == 'g':
        if tileNumber == 1:
            return blackG1
        if tileNumber == 2:
            return whiteG2
        if tileNumber == 3:
            return blackG3
        if tileNumber == 4:
            return whiteG4
        if tileNumber == 5:
            return blackG5
        if tileNumber == 6:
            return whiteG6
        if tileNumber == 7:
            return blackG7
        if tileNumber == 8:
            return whiteG8
    
    if tileLetter == 'h':
        if tileNumber == 1:
            return whiteH1
        if tileNumber == 2:
            return blackH2
        if tileNumber == 3:
            return whiteH3
        if tileNumber == 4:
            return blackH4
        if tileNumber == 5:
            return whiteH5
        if tileNumber == 6:
            return blackH6
        if tileNumber == 7:
            return whiteH7
        if tileNumber == 8:
            return blackH8
    else:
        return whiteA2

def AdjustPositionAfterMove(iIndex, jIndex):
    # Takes two indexs and outputs the tile position
    if iIndex == 0:
        if jIndex == 0:
            return ('a', 8)
        elif jIndex == 1:
            return ('b', 8)
        elif jIndex == 2:
            return ('c', 8)
        elif jIndex == 3:
            return ('d', 8)
        elif jIndex == 4:
            return ('e', 8)
        elif jIndex == 5:
            return ('f', 8)
        elif jIndex == 6:
            return ('g', 8)
        elif jIndex == 7:
            return ('h', 8)
    elif iIndex == 1:
        if jIndex == 0:
            return ('a', 7)
        elif jIndex == 1:
            return ('b', 7)
        elif jIndex == 2:
            return ('c', 7)
        elif jIndex == 3:
            return ('d', 7)
        elif jIndex == 4:
            return ('e', 7)
        elif jIndex == 5:
            return ('f', 7)
        elif jIndex == 6:
            return ('g', 7)
        elif jIndex == 7:
            return ('h', 7)
    elif iIndex == 2:
        if jIndex == 0:
            return ('a', 6)
        elif jIndex == 1:
            return ('b', 6)
        elif jIndex == 2:
            return ('c', 6)
        elif jIndex == 3:
            return ('d', 6)
        elif jIndex == 4:
            return ('e', 6)
        elif jIndex == 5:
            return ('f', 6)
        elif jIndex == 6:
            return ('g', 6)
        elif jIndex == 7:
            return ('h', 6)
    elif iIndex == 3:
        if jIndex == 0:
            return ('a', 5)
        elif jIndex == 1:
            return ('b', 5)
        elif jIndex == 2:
            return ('c', 5)
        elif jIndex == 3:
            return ('d', 5)
        elif jIndex == 4:
            return ('e', 5)
        elif jIndex == 5:
            return ('f', 5)
        elif jIndex == 6:
            return ('g', 5)
        elif jIndex == 7:
            return ('h', 5)
    elif iIndex == 4:
        if jIndex == 0:
            return ('a', 4)
        elif jIndex == 1:
            return ('b', 4)
        elif jIndex == 2:
            return ('c', 4)
        elif jIndex == 3:
            return ('d', 4)
        elif jIndex == 4:
            return ('e', 4)
        elif jIndex == 5:
            return ('f', 4)
        elif jIndex == 6:
            return ('g', 4)
        elif jIndex == 7:
            return ('h', 4)
    elif iIndex == 5:
        if jIndex == 0:
            return ('a', 3)
        elif jIndex == 1:
            return ('b', 3)
        elif jIndex == 2:
            return ('c', 3)
        elif jIndex == 3:
            return ('d', 3)
        elif jIndex == 4:
            return ('e', 3)
        elif jIndex == 5:
            return ('f', 3)
        elif jIndex == 6:
            return ('g', 3)
        elif jIndex == 7:
            return ('h', 3)
    elif iIndex == 6:
        if jIndex == 0:
            return ('a', 2)
        elif jIndex == 1:
            return ('b', 2)
        elif jIndex == 2:
            return ('c', 2)
        elif jIndex == 3:
            return ('d', 2)
        elif jIndex == 4:
            return ('e', 2)
        elif jIndex == 5:
            return ('f', 2)
        elif jIndex == 6:
            return ('g', 2)
        elif jIndex == 7:
            return ('h', 2)
    elif iIndex == 7:
        if jIndex == 0:
            return ('a', 1)
        elif jIndex == 1:
            return ('b', 1)
        elif jIndex == 2:
            return ('c', 1)
        elif jIndex == 3:
            return ('d', 1)
        elif jIndex == 4:
            return ('e', 1)
        elif jIndex == 5:
            return ('f', 1)
        elif jIndex == 6:
            return ('g', 1)
        elif jIndex == 7:
            return ('h', 1)

def FindingTheLogicArrayIndexOfATile(tileLetter, tileNumber):
    # Takes the tile tileLetter and tileNumber and returns the indexs of the position
    if tileLetter == 'a':
        if tileNumber == 1:
            return 7,0
        if tileNumber == 2:
            return 6,0
        if tileNumber == 3:
            return 5,0
        if tileNumber == 4:
            return 4,0
        if tileNumber == 5:
            return 3,0
        if tileNumber == 6:
            return 2,0
        if tileNumber == 7:
            return 1,0
        if tileNumber == 8:
            return 0,0
        
    if tileLetter == 'b':
        if tileNumber == 1:
            return 7,1
        if tileNumber == 2:
            return 6,1
        if tileNumber == 3:
            return 5,1
        if tileNumber == 4:
            return 4,1
        if tileNumber == 5:
            return 3,1
        if tileNumber == 6:
            return 2,1
        if tileNumber == 7:
            return 1,1
        if tileNumber == 8:
            return 0,1
    
    if tileLetter == 'c':
        if tileNumber == 1:
            return 7,2
        if tileNumber == 2:
            return 6,2
        if tileNumber == 3:
            return 5,2
        if tileNumber == 4:
            return 4,2
        if tileNumber == 5:
            return 3,2
        if tileNumber == 6:
            return 2,2
        if tileNumber == 7:
            return 1,2
        if tileNumber == 8:
            return 0,2
    
    if tileLetter == 'd':
        if tileNumber == 1:
            return 7,3
        if tileNumber == 2:
            return 6,3
        if tileNumber == 3:
            return 5,3
        if tileNumber == 4:
            return 4,3
        if tileNumber == 5:
            return 3,3
        if tileNumber == 6:
            return 2,3
        if tileNumber == 7:
            return 1,3
        if tileNumber == 8:
            return 0,3
        
    if tileLetter == 'e':
        if tileNumber == 1:
            return 7,4
        if tileNumber == 2:
            return 6,4
        if tileNumber == 3:
            return 5,4
        if tileNumber == 4:
            return 4,4
        if tileNumber == 5:
            return 3,4
        if tileNumber == 6:
            return 2,4
        if tileNumber == 7:
            return 1,4
        if tileNumber == 8:
            return 0,4
    
    if tileLetter == 'f':
        if tileNumber == 1:
            return 7,5
        if tileNumber == 2:
            return 6,5
        if tileNumber == 3:
            return 5,5
        if tileNumber == 4:
            return 4,5
        if tileNumber == 5:
            return 3,5
        if tileNumber == 6:
            return 2,5
        if tileNumber == 7:
            return 1,5
        if tileNumber == 8:
            return 0,5
          
    if tileLetter == 'g':
        if tileNumber == 1:
            return 7,6
        if tileNumber == 2:
            return 6,6
        if tileNumber == 3:
            return 5,6
        if tileNumber == 4:
            return 4,6
        if tileNumber == 5:
            return 3,6
        if tileNumber == 6:
            return 2,6
        if tileNumber == 7:
            return 1,6
        if tileNumber == 8:
            return 0,6
    
    if tileLetter == 'h':
        if tileNumber == 1:
            return 7,7
        if tileNumber == 2:
            return 6,7
        if tileNumber == 3:
            return 5,7
        if tileNumber == 4:
            return 4,7
        if tileNumber == 5:
            return 3,7
        if tileNumber == 6:
            return 2,7
        if tileNumber == 7:
            return 1,7
        if tileNumber == 8:
            return 0,7
    else:
        return 0,0

def PiecesCollide(turn):
    # Detects if a piece collides with another and removes the one that is not moving from the board 
    # Then it adds the removed piece to the captured list
    whiteCollisionList = [whitePawn1,whitePawn2,whitePawn3,whitePawn4,whitePawn5,whitePawn6,whitePawn7,whitePawn8,
                          whiteCastle1, whiteCastle2, whiteKnight1, whiteKnight2, whiteBishop1,whiteBishop2,
                          whiteQueen1, whiteQueen2, whiteQueen3, whiteQueen4, whiteQueen5, whiteQueen6, whiteQueen7, whiteQueen8, whiteQueen9]

    blackCollisionList = [blackPawn1,blackPawn2,blackPawn3,blackPawn4,blackPawn5,blackPawn6,blackPawn7,blackPawn8,
                          blackCastle1,blackCastle2,blackKnight1,blackKnight2,blackBishop1,blackBishop2,
                          blackQueen1,blackQueen2,blackQueen3,blackQueen4,blackQueen5,blackQueen6,blackQueen7,blackQueen8, blackQueen9]
    
    blackCapturedIncrement = 0
    whiteCapturedIncrement = 0
    
    if turn == 'white':
     for x in range(0,23):
         if whiteCollisionList[x].rect.collideobjects(blackCollisionList) != None:
             
            piece = whiteCollisionList[x].rect.collideobjects(blackCollisionList)
            piece.rect.x, piece.rect.y = 1700+(60*blackCapturedIncrement),1600
            piece.pos = (0,0)
            piece.indexIOnLogicArray, piece.indexJOnLogicArray = 10,10
            piece.onBoard = False
            capturedBlackPieces.append(piece)
            blackCapturedIncrement+=1
            break
    
    elif turn == 'black':
        for x in range(0,23):
            if blackCollisionList[x].rect.collideobjects(whiteCollisionList) != None:

                piece = blackCollisionList[x].rect.collideobjects(whiteCollisionList)
                piece.rect.x, piece.rect.y = 1600+(60*whiteCapturedIncrement),1500
                piece.pos = (0,0)
                piece.indexIOnLogicArray, piece.indexJOnLogicArray = 10,10 
                piece.onBoard = False
                capturedWhitePieces.append(piece)
                whiteCapturedIncrement+=1
                break

def DetermineAllPotentialMoves(turn):
    # Determines all potential moves that a side can make
    if turn == 'white':
        allPotentialMoves = []
        allPotentialMoves.append(WhereCanKingMove('black'))
        for x in range(1,10):
            if x < 3:
                allPotentialMoves.append(WhereCanKnightMove('black', x))
                allPotentialMoves.append(WhereCanBishopMove('black', x, True))
                allPotentialMoves.append(WhereCanCastleMove('black', x, True))
            if x < 9:
                allPotentialMoves.append(WhereCanPawnMove('black', x))
            allPotentialMoves.append(WhereCanQueenMove('black', x))
            
        return allPotentialMoves
    elif turn == 'black':
        allPotentialMoves = []
        allPotentialMoves.append(WhereCanKingMove('white'))
        for x in range(1,10):
            if x < 3:
                allPotentialMoves.append(WhereCanKnightMove('white', x))
                allPotentialMoves.append(WhereCanBishopMove('white', x, True))
                allPotentialMoves.append(WhereCanCastleMove('white', x, True))
            if x < 9:
                allPotentialMoves.append(WhereCanPawnMove('white', x))


            allPotentialMoves.append(WhereCanQueenMove('white', x))
            
        return allPotentialMoves
                

def Check(turn):
    # Determines if a side is in check
    potentialMoves = DetermineAllPotentialMoves(turn)
    # White king position
    whiteKingTileLetter, whiteKingTileNumber = whiteKing.pos
    whiteKingTile =  LocatingTheTileRects(whiteKingTileLetter, whiteKingTileNumber)
    # Black king position
    blackKingTileLetter, blackKingTileNumber = blackKing.pos
    blackKingTile = LocatingTheTileRects(blackKingTileLetter, blackKingTileNumber)
    # Looping through all possible moves of the opposing colour in every turn and comparing them to the kings position
    if turn == 'white':
        for x in range(0, len(potentialMoves)):
            if potentialMoves[x] != None:
                for y in range(0, len(potentialMoves[x])):
                    if potentialMoves[x][y] != None:
                        tileLetter, tileNumber =  potentialMoves[x][y]
                        tile =  LocatingTheTileRects(tileLetter, tileNumber)
                        if whiteKingTile == tile:
                            return True
        return False        
    elif turn == 'black':
        for x in range(0, len(potentialMoves)):
            if potentialMoves[x] != None:
                for y in range(0, len(potentialMoves[x])):
                    if potentialMoves[x][y] != None:
                        tileLetter, tileNumber =  potentialMoves[x][y]
                        tile =  LocatingTheTileRects(tileLetter, tileNumber)
                        if blackKingTile == tile:
                            return True
        return False        
          
gameFont = pygame.font.Font("freesansbold.ttf", 32)
light_grey = (200,200,200)

# Game setup method and variable
CreateBlackPawns()
CreateWhitePawns()

CreateBlackCastles()
CreateWhiteCastles()

CreateBlackKnights()
CreateWhiteKnights()

CreateBlackBishops()
CreateWhiteBishops()

CreateBlackQueen()
CreateWhiteQueen()

CreateBlackKing()
CreateWhiteKing()

CreatePromotedQueens()

draggingPawn = False
draggingCastle = False
draggingKnight = False
draggingBishop = False
draggingQueen = False
draggingKing = False

currentMovingPawn = 0
currentMovingCastle = 0
currentMovingKnight = 0
currentMovingBishop = 0
currentMovingQueen = 0

check = False

def GameLoop(check, whichPlayersTurn, draggingPawn, draggingCastle, draggingKnight, draggingBishop, draggingQueen, draggingKing, currentMovingPawn, currentMovingCastle, currentMovingKnight, currentMovingBishop, currentMovingQueen):
    # Game loop
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Checking to see if the mouse is over a piece when it is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if collidePawn:
                    draggingPawn = True
                    currentMovingPawn = WhichPawnIsCollidedWith(whichPlayersTurn, whereMouseIs)
                elif collideCastle:
                    draggingCastle = True
                    currentMovingCastle = WhichCastleIsCollidedWith(whichPlayersTurn, whereMouseIs)
                elif collideKnight:
                    draggingKnight = True
                    currentMovingKnight = WhichKnightIsCollidedWith(whichPlayersTurn, CollidingWithAKnight(whichPlayersTurn, whereMouseIs), whereMouseIs)
                elif collideBishop:
                    draggingBishop = True
                    currentMovingBishop = WhichBishopIsCollidedWith(whichPlayersTurn, CollidingWithABishop(whichPlayersTurn, whereMouseIs), whereMouseIs)
                elif collideQueen:
                    draggingQueen = True
                    currentMovingQueen = WhichQueenIsCollidedWith(whichPlayersTurn, whereMouseIs)
                elif collideKing:
                    draggingKing = True
                    
            # On mouse release it moves a piece if there was a potential move avaliable
            # If a piece is moved the turn changes and then the check method is called to see if the new move caused a check
            if event.type == pygame.MOUSEBUTTONUP and CheckIfMouseIsWithinBoardBorder(whereMouseIs):
                if draggingPawn:
                    
                    MovePositionOfPawn(whichPlayersTurn, currentMovingPawn, WhereCanPawnMove(whichPlayersTurn, currentMovingPawn), whereMouseIs)
                    # After a pawn move if they enter the promotion zone they are promoted to a queen
                    if PawnCollidesWithPromotionZone(whichPlayersTurn, currentMovingPawn):
                        PawnPromotion(whichPlayersTurn, currentMovingPawn)
                    
                    if switchTurn:
                        if whichPlayersTurn == 'white':
                            whichPlayersTurn = 'black'
                        elif whichPlayersTurn == 'black':
                            whichPlayersTurn = 'white'
                    check = Check(whichPlayersTurn)
                    draggingPawn = False
                    
                elif draggingCastle:
                    
                    MovePositionOfCastle(whichPlayersTurn, currentMovingCastle, WhereCanCastleMove(whichPlayersTurn, currentMovingCastle, True), whereMouseIs)
                    
                    if switchTurn:
                        if whichPlayersTurn == 'white':
                            whichPlayersTurn = 'black'
                        elif whichPlayersTurn == 'black':
                            whichPlayersTurn = 'white'
                    check = Check(whichPlayersTurn)
                    draggingCastle = False
                    
                elif draggingKnight:
                    
                    MovePositionOfKnight(whichPlayersTurn, currentMovingKnight, WhereCanKnightMove(whichPlayersTurn, currentMovingKnight), whereMouseIs)
                    
                    if switchTurn:
                        if whichPlayersTurn == 'white':
                            whichPlayersTurn = 'black'
                        elif whichPlayersTurn == 'black':
                            whichPlayersTurn = 'white'
                    check = Check(whichPlayersTurn)
                    draggingKnight = False
                
                elif draggingBishop:
                    
                    MovePositionOfBishop(whichPlayersTurn, currentMovingBishop, WhereCanBishopMove(whichPlayersTurn, currentMovingBishop, draggingBishop), whereMouseIs)
                    
                    if switchTurn:
                        if whichPlayersTurn == 'white':
                            whichPlayersTurn = 'black'
                        elif whichPlayersTurn == 'black':
                            whichPlayersTurn = 'white'
                    check = Check(whichPlayersTurn)
                    draggingBishop = False
                
                elif draggingQueen:
                    
                    MovePositionOfQueen(whichPlayersTurn, WhereCanQueenMove(whichPlayersTurn, currentMovingQueen), currentMovingQueen, whereMouseIs)

                    if switchTurn:
                        if whichPlayersTurn == 'white':
                            whichPlayersTurn = 'black'
                        elif whichPlayersTurn == 'black':
                            whichPlayersTurn = 'white'
                    check = Check(whichPlayersTurn)
                    draggingQueen = False
                
                elif draggingKing:
                    
                    MovePositionOfKing(whichPlayersTurn, WhereCanKingMove(whichPlayersTurn), whereMouseIs)

                    if switchTurn:
                        if whichPlayersTurn == 'white':
                            whichPlayersTurn = 'black'
                        elif whichPlayersTurn == 'black':
                            whichPlayersTurn = 'white'
                    check = Check(whichPlayersTurn)
                    draggingKing = False
                    
            
                    
        screen.fill((255,255,255))
        whereMouseIs = pygame.mouse.get_pos()
        
        # Board set up
        InstallBoardInLoop()
        PutPiecesOnTheBoard()
        DrawBoardBorder()
        DrawTilePositions()
        
        # Shows which players turn it is and if check is occuring
        if check:
            whichPlayersTurnTextAndCheck = gameFont.render(f"{whichPlayersTurn} is in check", False, (0,0,0))
            screen.blit(whichPlayersTurnTextAndCheck, (350,10))
        else:
            whichPlayersTurnText = gameFont.render(f"{whichPlayersTurn}'s Turn", False, (0,0,0))
            screen.blit(whichPlayersTurnText, (400,10))
        
        # Detect if mouse collides with a piece
        collidePawn = CollidingWithAPawn(whichPlayersTurn, whereMouseIs)
        collideCastle = CollidingWithACastle(whichPlayersTurn, whereMouseIs)
        collideKnight = CollidingWithAKnight(whichPlayersTurn, whereMouseIs)
        collideBishop = CollidingWithABishop(whichPlayersTurn, whereMouseIs)
        collideQueen = CollidingWithAQueen(whichPlayersTurn, whereMouseIs)
        collideKing = CollidingWithAKing(whichPlayersTurn, whereMouseIs)
        
        # Drawing rectangles over all tiles to allow for collisions
        pygame.draw.rect(screen, (255,255,255), whiteA8, 1)
        pygame.draw.rect(screen, (0,0,0), blackB8, 1)
        pygame.draw.rect(screen, (255,255,255), whiteC8, 1)
        pygame.draw.rect(screen, (0,0,0), blackD8, 1)
        pygame.draw.rect(screen, (255,255,255), whiteE8, 1)
        pygame.draw.rect(screen, (0,0,0), blackF8, 1)
        pygame.draw.rect(screen, (255,255,255), whiteG8, 1)
        pygame.draw.rect(screen, (0,0,0), blackH8, 1)
        
        pygame.draw.rect(screen, (0,0,0), blackA7, 1)
        pygame.draw.rect(screen, (255,255,255), whiteB7, 1)
        pygame.draw.rect(screen, (0,0,0), blackC7, 1)
        pygame.draw.rect(screen, (255,255,255), whiteD7, 1)
        pygame.draw.rect(screen, (0,0,0), blackE7, 1)
        pygame.draw.rect(screen, (255,255,255), whiteF7, 1)
        pygame.draw.rect(screen, (0,0,0), blackG7, 1)
        pygame.draw.rect(screen, (255,255,255), whiteH7, 1)
        
        pygame.draw.rect(screen, (255,255,255), whiteA6, 1)
        pygame.draw.rect(screen, (0,0,0), blackB6, 1)
        pygame.draw.rect(screen, (255,255,255), whiteC6, 1)
        pygame.draw.rect(screen, (0,0,0), blackD6, 1)
        pygame.draw.rect(screen, (255,255,255), whiteE6, 1)
        pygame.draw.rect(screen, (0,0,0), blackF6, 1)
        pygame.draw.rect(screen, (255,255,255), whiteG6, 1)
        pygame.draw.rect(screen, (0,0,0), blackH6, 1)
        
        pygame.draw.rect(screen, (0,0,0), blackA5, 1)
        pygame.draw.rect(screen, (255,255,255), whiteB5, 1)
        pygame.draw.rect(screen, (0,0,0), blackC5, 1)
        pygame.draw.rect(screen, (255,255,255), whiteD5, 1)
        pygame.draw.rect(screen, (0,0,0), blackE5, 1)
        pygame.draw.rect(screen, (255,255,255), whiteF5, 1)
        pygame.draw.rect(screen, (0,0,0), blackG5, 1)
        pygame.draw.rect(screen, (255,255,255), whiteH5, 1)
        
        pygame.draw.rect(screen, (255,255,255), whiteA4, 1)
        pygame.draw.rect(screen, (0,0,0), blackB4, 1)
        pygame.draw.rect(screen, (255,255,255), whiteC4, 1)
        pygame.draw.rect(screen, (0,0,0), blackD4, 1)
        pygame.draw.rect(screen, (255,255,255), whiteE4, 1)
        pygame.draw.rect(screen, (0,0,0), blackF4, 1)
        pygame.draw.rect(screen, (255,255,255), whiteG4, 1)
        pygame.draw.rect(screen, (0,0,0), blackH4, 1)
        
        pygame.draw.rect(screen, (0,0,0), blackA3, 1)
        pygame.draw.rect(screen, (255,255,255), whiteB3, 1)
        pygame.draw.rect(screen, (0,0,0), blackC3, 1)
        pygame.draw.rect(screen, (255,255,255), whiteD3, 1)
        pygame.draw.rect(screen, (0,0,0), blackE3, 1)
        pygame.draw.rect(screen, (255,255,255), whiteF3, 1)
        pygame.draw.rect(screen, (0,0,0), blackG3, 1)
        pygame.draw.rect(screen, (255,255,255), whiteH3, 1)
        
        pygame.draw.rect(screen, (255,255,255), whiteA2, 1)
        pygame.draw.rect(screen, (0,0,0), blackB2, 1)
        pygame.draw.rect(screen, (255,255,255), whiteC2, 1)
        pygame.draw.rect(screen, (0,0,0), blackD2, 1)
        pygame.draw.rect(screen, (255,255,255), whiteE2, 1)
        pygame.draw.rect(screen, (0,0,0), blackF2, 1)
        pygame.draw.rect(screen, (255,255,255), whiteG2, 1)
        pygame.draw.rect(screen, (0,0,0), blackH2, 1)
        
        pygame.draw.rect(screen, (0,0,0), blackA1, 1)
        pygame.draw.rect(screen, (255,255,255), whiteB1, 1)
        pygame.draw.rect(screen, (0,0,0), blackC1, 1)
        pygame.draw.rect(screen, (255,255,255), whiteD1, 1)
        pygame.draw.rect(screen, (0,0,0), blackE1, 1)
        pygame.draw.rect(screen, (255,255,255), whiteF1, 1)
        pygame.draw.rect(screen, (0,0,0), blackG1, 1)
        pygame.draw.rect(screen, (255,255,255), whiteH1, 1)
        
        
        pygame.display.flip()
        clock.tick(60)


BG = pygame.image.load("/Users/michael/Python/Programming-and-design-project/background.jpg")

def draw_text(text, font, color, surface, x, y): # defining a function draw_text for drawing words on buttons that takes the following peramiteres.
    text_obj = font.render(text, True, color) # renders text
    text_rect = text_obj.get_rect() 
    text_rect.center = (x, y) # gets position
    surface.blit(text_obj, text_rect) # draws rendered text on desired position
    

# Main menu loop function
def main_menu():

    while True: # started our loop
        playButtonRect = pygame.Rect(screenWidth // 2 - 100, screenHeight // 2 - 50, 200, 100) # start button variable position
        quitButtonRect = pygame.Rect(screenWidth // 2 - 100, screenHeight // 2 - -100, 200, 100) # quit button variable positioning
        # Iterates over every action taken by the user
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if the event type is quitting pygame application, exit pygame and sys.
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButtonRect.collidepoint(pygame.mouse.get_pos()):
                    # if the event taken was a mouse click by the user, and the collidepoint is on the start button;
                    # Transition to next screen
                    secondScreen()
                if quitButtonRect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                    

        screen.blit(BG, (0, 0)) # Here we initialise the BG variable to set background of menu screen
        draw_text("Chess Game", pygame.font.Font(None, 60), (0, 0, 0), screen, screenWidth // 2, 100) # title drawn using draw_text function
        colourOfButton = (0, 0, 0) # addding colour of start button
        colourOfQuitButton = (20,20,20) # colour of quit button
        pygame.draw.rect(screen, colourOfButton, playButtonRect) # drawing start button
        pygame.draw.rect(screen, colourOfQuitButton, quitButtonRect) # drawing quit button
        # taken from existing pygame Font class
        draw_text("Start", pygame.font.Font(None, 60), (255, 0, 0), screen, screenWidth // 2, screenHeight // 2,)
        draw_text("Quit", pygame.font.Font(None, 60), (255, 0, 0), screen, screenWidth // 2, screenHeight // 1.4 - 60)
        pygame.display.flip() # turns to next screen once button clicked
        clock.tick(60)

def secondScreen(): # second screen(colour choice) function
    while True: # same loop as first screen
        whiteButtonRect = pygame.Rect(screenWidth // 2 - -100, screenHeight // 2 - 50, 200, 100) # white button variable
        blackButtonRect = pygame.Rect(screenWidth // 2 - 350, screenHeight // 2 - 50, 200, 100) # black button variable
        backButtonRect = pygame.Rect(screenWidth // 2 - 100, screenHeight // 2- -100, 200, 100) # back button variable
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if whiteButtonRect.collidepoint(pygame.mouse.get_pos()):
                        # Transition back to first main menu screen ~ (work in progress) - wont take you to main menu in final design
                        GameLoop(check, whichPlayersTurn, draggingPawn, draggingCastle, draggingKnight, draggingBishop, draggingQueen, draggingKing, currentMovingPawn, currentMovingCastle, currentMovingKnight, currentMovingBishop, currentMovingQueen)
                    if blackButtonRect.collidepoint(pygame.mouse.get_pos()):
                        GameLoop(check, whichPlayersTurn, draggingPawn, draggingCastle, draggingKnight, draggingBishop, draggingQueen, draggingKing, currentMovingPawn, currentMovingCastle, currentMovingKnight, currentMovingBishop, currentMovingQueen)
                    if backButtonRect.collidepoint(pygame.mouse.get_pos()):
                        main_menu() # this one does stay like this... 
                        
        screen.blit(BG, (0, 0))
        draw_text("Player One, Please Choose Your Colour", pygame.font.Font(None, 60), (0, 0, 0), screen, screenWidth // 2, 100)
        colourOfButtonWhite = (255,255,255) # adding colour of white button
        colourOfButtonBlack = (0,0,0) # adding colour of black button
        colourOfButtonBack = (20,20,20) # colour of back button
        pygame.draw.rect(screen, colourOfButtonWhite, whiteButtonRect) # drawing white button on screen
        pygame.draw.rect(screen, colourOfButtonBlack, blackButtonRect) # drawing black button on screen
        pygame.draw.rect(screen, colourOfButtonBack, backButtonRect) # drawing back button on screen
        draw_text("White", pygame.font.Font(None, 60), (0,0,0), screen, screenWidth // 1.4 - 20, screenHeight // 2,)
        draw_text("Black", pygame.font.Font(None, 60), (255,255,255), screen, screenWidth // 4, screenHeight // 2,)
        draw_text("Back", pygame.font.Font(None, 60), (255,0,0), screen, screenWidth // 2, screenHeight // 1.4 - 60) #same as quit button positioning
        
        pygame.display.flip() # in this instance flips back to main menu screen (for now...)
        clock.tick(60)

main_menu() # runs program