import pygame

class King:
    def __init__(self, colour, pos, indexIOnLogicArray, indexJOnLogicArray, onBoard):
        self.size = (50,50)
        self.colour = colour
        self.surface = self.ReduceImageToNeededSize()
        self.pos = pos
        self.indexIOnLogicArray = indexIOnLogicArray
        self.indexJOnLogicArray = indexJOnLogicArray
        self.xCoordinate, self.yCoordinate = self.GetInitialCoordinates()
        self.rect = self.surface.get_rect(center = (self.xCoordinate, self.yCoordinate))
        self.onBoard = onBoard

        self.moved = False
    def GetImage(self):
        if self.colour.lower() == 'black':
            return pygame.image.load('/Users/michael/Python/PackageControlTesting/chessPieces/images/Black Chess Pieces/Black King.png')
        if self.colour.lower() == 'white':
            return pygame.image.load('/Users/michael/Python/PackageControlTesting/chessPieces/images/White Chess Pieces/White King.png')
        
    def ReduceImageToNeededSize(self):
        return pygame.transform.scale(self.GetImage(), self.size)
    
    def GetInitialCoordinates(self):
        if self.colour.lower() == "white":
            if self.pos == ("e", 1):
                return (550, 850)
            
        elif self.colour.lower() == "black":
            if self.pos == ("e", 8):
                return (550, 150)
           