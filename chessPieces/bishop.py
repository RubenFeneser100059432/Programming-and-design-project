import pygame

class Bishop:
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
    
    def GetImage(self):
        if self.colour.lower() == 'black':
            return pygame.image.load('chessPieces/images/Black Chess Pieces/Black Bishop.png')
        if self.colour.lower() == 'white':
            return pygame.image.load('/Users/michael/Python/PackageControlTesting/chessPieces/images/White Chess Pieces/White Bishop.png')
        
    def ReduceImageToNeededSize(self):
        return pygame.transform.scale(self.GetImage(), self.size)
    
    def GetInitialCoordinates(self):
        if self.colour.lower() == "white":
            if self.pos == ("c", 1):
                return (350, 850)
            elif self.pos == ("f", 1):
                return (650, 850)
        elif self.colour.lower() == "black":
            if self.pos == ("c", 8):
                return (350, 150)
            elif self.pos == ("f", 8):
                return (650, 150)  