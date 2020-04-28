class GameStats():
    #track stats for corona invasion

    def __init__(self,s):
        #initialize stats
        self.s = s                #s is for settings
        self.reset_stats()
        #high score should never be reset
        self.high_score = 0

        #start coro invasion in inactive state
        self.game_active =False

    def reset_stats(self):
        #initialize stats that may change during the game
        self.sanits_left = self.s.sanit_limit
        self.score = 0
        self.level =1
