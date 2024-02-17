import pygame
class Tiles:
    def __init__(self, color):
        self.width, self.height =  100, 100
        self.color = color
        self.surface = self.CreateTileSurface()
        
        self.FillSurface()
        
    def CreateTileSurface(self):
        return pygame.Surface((self.width, self.height))
    
    def FillSurface(self):
        self.surface.fill(self.color)
        
    