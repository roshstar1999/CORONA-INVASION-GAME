class Settings():
    '''A class to store all settings for my alien invasion'''
    
    def __init__(self):
        '''initialize the game stats'''
        self.screen_width = 1500
        self.screen_height = 800
        self.bg_color = (254, 254, 254)                             #21, 23, 74
        self.sanit_limit = 3
        
    
        #for bubble setting
        
        self.bub_color= (240, 153, 225)
        self.bub_height= 20
        self.bub_width = 20
        self.bubbles_allowed = 3

        #coro settings
        
        self.fleet_drop_speed = 8

        #how quickly game speeds up
        self.speedup_scale = 1.1

        #how quickly coro point value increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        
    
    
    def initialize_dynamic_settings(self):
        #init settings that would change in the game
        self.sanit_speed_factor = 1.5
        self.bub_speed_factor = 3
        self.coro_speed_factor = 1
        #fleet_direction of 1 represents right; -1 = left
        self.fleet_direction =1

        #scoring
        self.coro_points = 50
    

    def increase_speed(self):
        #increase speed settings and coro point values
        self.sanit_speed_factor *= self.speedup_scale
        self.bub_speed_factor *= self.speedup_scale
        self.coro_speed_factor *= self.speedup_scale

        self.coro_points = int(self.coro_points*self.score_scale)
        #print(self.coro_points)




