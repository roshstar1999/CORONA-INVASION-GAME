import pygame
from pygame.sprite import Sprite
import Settingss 
class Sanitizer(Sprite):

    def __init__(self,s,screen):
        #sanitizer  start pos set
        super(Sanitizer,self).__init__()
        self.screen = screen
        self.s = s                   #s is for settings class instance

        #load image and get its rect
        self.image = pygame.image.load('images/sanit1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start new sanit at bottom centre(matching sanitizer and screen bootom centre)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False        #flags for movement
        self.moving_left = False
        
        #decimal val for bottle center as centerx only stores int vals
        self.center = float(self.rect.centerx)
    
    def center_sanit(self):
        #center bottle on screen
        self.center = self.screen_rect.centerx
        

    def update(self):
        #sanitizer pos updating as per flag 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.s.sanit_speed_factor
        
        if self.moving_left and self.rect.left > 0:
            self.center -= self.s.sanit_speed_factor
        
        #updating rect obj from self.center
        self.rect.centerx = self.center
       
    def blitme(self):
        '''drawing sanit at curr location'''
        self.screen.blit(self.image,self.rect)
        

