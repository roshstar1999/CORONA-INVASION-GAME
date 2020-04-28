import pygame
from pygame.sprite import Sprite
class Coro(Sprite):
    #to rpresent single alien in the fleet

    def __init__(self,s,screen):
        #initialize corona and set start pos
        super(Coro,self).__init__()
        self.screen = screen
        self.s = s

        #load image 
        self.image = pygame.image.load('images/coroo.bmp')
        self.rect = self.image.get_rect()

        #start each coro virus near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #virus exact pos
        self.x = float(self.rect.x)

    def blitme(self):
        #draw virus at curr loc
        self.screen.blit(self.image , self.rect)

    def update(self):
        '''move virus right or left'''
        self.x += (self.s.coro_speed_factor*self.s.fleet_direction)
        self.rect.x = self.x
        
    def check_edges(self):
        #return true if coro at edge of screen
        screen_rect  = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True
