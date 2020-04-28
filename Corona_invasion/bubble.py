import pygame
from pygame.sprite import Sprite
class Bubble(Sprite):
    #class to manage soap drops fired by our sanitizer

    def __init__(self, s,screen,sanit):
        #create bubble 
        super().__init__()
        self.screen = screen
        
        self.rect = pygame.Rect(0,0,s.bub_width,s.bub_height)
        

        #Start new sanit at bottom centre(matching sanitizer and bubble top centre)
        #this will give feel as if the bubble is being fired from the bottle
        self.rect.centerx = sanit.rect.centerx                     
        self.rect.top = sanit.rect.top

        #store soap buble position as decimal value
        self.y =float(self.rect.y)
        self.speed_factor = s.bub_speed_factor
        self.color = s.bub_color

    def update(self):
        #to move bubble up the screen
        #updating decimal pos of the bubble
        self.y -= self.speed_factor           #cuz the bullet has to move up(decreasing y cordinate)
        #update rect position
        self.rect.y = self.y

    def draw_bub(self):
        #draw bubble to screen
        pygame.draw.rect(self.screen,self.color,self.rect)