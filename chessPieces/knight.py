import pygame

class Knight:
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
            return pygame.image.load('chessPieces/images/Black Chess Pieces/Black Knight.png')
        if self.colour.lower() == 'white':
            return pygame.image.load('chessPieces/images/White Chess Pieces/White Knight.png')
        
    def ReduceImageToNeededSize(self):
        return pygame.transform.scale(self.GetImage(), self.size)
    
    def GetInitialCoordinates(self):
        if self.colour.lower() == "white":
            if self.pos == ("b", 1):
                return (250, 850)
            elif self.pos == ("g", 1):
                return (750, 850)
        elif self.colour.lower() == "black":
            if self.pos == ("b", 8):
                return (250, 150)
            elif self.pos == ("g", 8):
                return (750, 150) 