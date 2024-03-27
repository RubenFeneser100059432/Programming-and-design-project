import pygame

class Queen:
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
            return pygame.image.load('/Users/michael/Python/PackageControlTesting/chessPieces/images/Black Chess Pieces/Black Queen.png')
        if self.colour.lower() == 'white':
            return pygame.image.load('/Users/michael/Python/PackageControlTesting/chessPieces/images/White Chess Pieces/White Queen.png')
    
    def ReduceImageToNeededSize(self):
        return pygame.transform.scale(self.GetImage(), self.size)
    
    def GetInitialCoordinates(self):
        if self.colour.lower() == "white":
            if self.pos == (0,0):
                return (2000,2000)
            elif self.pos == ("d", 1):
                return (450, 850)
            elif self.pos == ('a', 8):
                return (150,150)
            elif self.pos == ('b', 8):
                return (250, 150)
            elif self.pos == ('c', 8):
                return (350, 150)
            elif self.pos == ('d', 8):
                return (450, 150)
            elif self.pos == ('e', 8):
                return (550, 150)
            elif self.pos == ('f', 8):
                return (550, 150)
            elif self.pos == ('g', 8):
                return (750, 150)
            elif self.pos == ('h', 8):
                return (850, 150)
            
        elif self.colour.lower() == "black":
            if self.pos == (0,0):
                return (2200, 2200)
            elif self.pos == ("d", 8):
                return (450, 150)
            elif self.pos == ('a', 1):
                return (150,850)
            elif self.pos == ('b', 1):
                return (250, 850)
            elif self.pos == ('c', 1):
                return (350, 850)
            elif self.pos == ('d', 1):
                return (450, 850)
            elif self.pos == ('e', 1):
                return (550, 850)
            elif self.pos == ('f', 1):
                return (550, 850)
            elif self.pos == ('g', 1):
                return (750, 850)
            elif self.pos == ('h', 1):
                return (850, 850)