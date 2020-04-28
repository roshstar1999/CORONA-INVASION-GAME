import sys
from time import sleep
import pygame
from pygame.sprite import Group
from  Settingss import Settings
from game_stats import GameStats
from button import Button
from sanitizer import Sanitizer
from scoreboard import Scoreboard
from coro import Coro
from bubble import Bubble
import functions as f
def rungame():

    #initializin pygame,settings,and scr objs
    pygame.init()

    s = Settings()
    
    screen = pygame.display.set_mode((s.screen_width,s.screen_height))
    pygame.display.set_caption("CORONA INVASION!")

    #make the play button
    play_button = Button(s,screen,"Play")

    #create instance to store game statistics and create a scoreboard
    stats = GameStats(s)
    sb = Scoreboard(s,screen,stats)


    #time to make a ship
    sanit = Sanitizer(s , screen)
    #make a  virus
    #coro = Coro(s,screen)                                    ####optional for now
    #making a group to store bullets in
    bubbles = Group()
    coros = Group()
    #create fleet of viruses
    f.create_fleet(s,screen,sanit,coros)
  

    #main loop for the game
    while True:
        f.check_events(s,screen,stats,sb,play_button,sanit,coros,bubbles) 


           
        bubbles.update()
        
        if stats.game_active:
            sanit.update()
            f.update_bubbles(s,screen,stats,sb,sanit,coros,bubbles)
            f.update_coros(s,screen,stats,sb,sanit,coros,bubbles)
            f.update_screen(s,screen,stats,sb,sanit,coros,bubbles,play_button)
            
        
       
rungame()