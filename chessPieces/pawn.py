import pygame
from chessPieces.chessPiece import ChessPiece

class Pawn(ChessPiece):
    
    def __init__(self, colour, pos, indexIOnLogicArray, indexJOnLogicArray, onBoard):
        self.size = (50,50)
        self.colour = colour
        self.surface = self.ReduceImageToNeededSize()
        self.pos = pos
        self.indexIOnLogicArray = indexIOnLogicArray
        self.indexJOnLogicArray = indexJOnLogicArray
        self.xInitialCoordinate, self.yInitialCoordinate = self.GetInitialCoordinates()
        self.x, self.y = 0 ,0
        self.rect = self.surface.get_rect(center = (self.xInitialCoordinate, self.yInitialCoordinate))
        self.firstMove = True
        self.onBoard = onBoard
        self.justMovedTwoSpace = False
        if self.x != 0 and self.y != 0:
            self.rect = self.GetNewRect()
            
        
    def GetImage(self):
        if self.colour.lower() == 'black':
            return pygame.image.load('/Users/michael/Python/PackageControlTesting/chessPieces/images/Black Chess Pieces/Black Pawn.png')
        if self.colour.lower() == 'white':
            return pygame.image.load('/Users/michael/Python/PackageControlTesting/chessPieces/images/White Chess Pieces/White Pawn.png')
        
    def ReduceImageToNeededSize(self):
        return pygame.transform.scale(self.GetImage(), self.size)
    
    def GetInitialCoordinates(self):
        if self.colour.lower() == "white":
            if self.pos == ("a", 2):
                return  (150, 750)
            elif self.pos == ("b", 2):
                return (250, 750)
            elif self.pos == ("c", 2):
                return (350, 750)
            elif self.pos == ("d", 2):
                return (450,750)
            elif self.pos == ("e", 2):
                return (550, 750)
            elif self.pos == ("f", 2):
               return (650,750)
            elif self.pos == ("g", 2):
               return (750,750)
            elif self.pos == ("h", 2):
                return (850,750)
        if self.colour.lower() == "black":
            if self.pos == ("a", 7):
                return (150, 250)
            elif self.pos == ("b", 7):
                return (250, 250)
            elif self.pos == ("c", 7):
                return (350 , 250)
            elif self.pos == ("d", 7):
                return (450, 250)
            elif self.pos == ("e", 7):
                return (550, 250)
            elif self.pos == ("f", 7):
               return (650, 250)
            elif self.pos == ("g", 7):
                return (750, 250)
            elif self.pos == ("h", 7):
                return (850, 250)
                
    def GetNewRect(self):
        return self.surface.get_rect(center =  (self.x, self.y))