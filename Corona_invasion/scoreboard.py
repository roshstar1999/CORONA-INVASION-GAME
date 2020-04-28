import pygame.font
from pygame.sprite import Group
from sanitizer import Sanitizer
class Scoreboard():
    #class to report scoring info

    def __init__(self,s,screen,stats):
        #initialize scorekeeping attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.s = self.stats = stats
        self.bg_color =s.bg_color
        #font settings
        self.text_color = (21, 117, 36)
        self.font = pygame.font.SysFont(None,48)

        #prepare initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_sanits()

    def prep_sanits(self):
        #show how many bottles left
        self.sanits = Group()
        for sanit_number in range(self.stats.sanits_left):
            sanit = Sanitizer(self.s,self.screen)
            sanit.rect.x = 10 + sanit_number*sanit.rect.width
            sanit.rect.y =10
            self.sanits.add(sanit)


    def prep_score(self):

        rounded_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_score)

        #turn score into given image
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.bg_color)

        #display score at top right of the screen
        self.score_rect = self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        #draw score and bottles to the screen
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.score_rect)
        self.screen.blit(self.level_image,self.level_rect)

        #draw bottles
        self.sanits.draw(self.screen)

    def prep_high_score(self):
        #turn high score on to rendered image
        high_score = int(round(self.stats.high_score,-1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image =self.font.render(high_score_str,True,self.text_color,self.bg_color)

        #center the high score at top of screen 
        self.high_score_rect =self.high_score_image.get_rect()
        self.high_score_rect =self.screen_rect.centerx
        self.high_score_rect = self.score_rect.top
    

    def prep_level(self):
        #turn level into rendered image
        self.level_image = self.font.render(str(self.stats.level),True,self.text_color,self.bg_color)

        #position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom+10
