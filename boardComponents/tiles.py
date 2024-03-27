import pygame


class Tiles:
    # A tile object takes color, usually an rgb tuple, and position which is a tuple containing a char and an int
    # Which should come from board
    def __init__(self,color, position):
        self.width, self.height =  100, 100
        self.color = color
        self.surface = self.CreateTileSurface()
        self.rect = self.surface.get_rect()
        self.xPosition, self.yPosition = position
        
        self.FillSurface()
        
    def CreateTileSurface(self):
        return pygame.Surface((self.width, self.height))
    
    def FillSurface(self):
        self.surface.fill(self.color)