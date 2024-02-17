import pygame
class Tiles:
    def _init_(self, color):
        self.width, self.height =  100
        self.color = color
        self.surface = self.CreateTileSurface()
        
        self.FillSurface()
        
    def CreateTileSurface(self):
        return pygame.Surface((self.width, self.height))
    
    def FillSurface(self):
        self.surface.fill(self.color)
        
    