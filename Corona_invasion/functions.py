import sys
import pygame
from coro import Coro
from bubble import Bubble 
from time import sleep

def check_keydown_events(event,s,screen,sanit,bubbles):
    if event.key == pygame.K_RIGHT:
        #move sanit to right
        sanit.moving_right = True
    elif event.key == pygame.K_LEFT:
        #move sanit to right
        sanit.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire(s,screen,sanit,bubbles)

def check_keyup_events(event,sanit):
    if event.key == pygame.K_RIGHT:
        #stop moving 
        sanit.moving_right = False
    elif event.key == pygame.K_LEFT:
        #stop moving 
        sanit.moving_left = False

def check_events(s,screen,stats,sb,play_button,sanit,coros,bubbles):
    #watch for keyboard and mouse events
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN :
                mouse_x,mouse_y = pygame.mouse.get_pos()
                check_play_button(s,screen,stats,sb,play_button,sanit,coros,bubbles,mouse_x,mouse_y)
            
            #Responding to key presses
            elif event.type == pygame.KEYDOWN:         #key pressed
                check_keydown_events(event,s,screen,sanit,bubbles)
               
            #Responding to key releases
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,sanit)



def update_screen(s,screen,stats,sb,sanit,coros,bubbles,play_button):
    '''update image on screen and new screen '''
    #make recent drawn screen visible
    screen.fill(s.bg_color)

    #redraw all bubbles behind sait and aliens
    for bubble in bubbles.sprites():
        bubble.draw_bub()
    sanit.blitme()
    coros.draw(screen)
    #coro.blitme()                                    '''wether to use or not'''
    
    #draw score info
    sb.show_score()


    #draw the play button if the game is INACTIVE
    if not stats.game_active:
        play_button.draw_button()

    #to make recent drawn pic visible
    pygame.display.flip()


def update_bubbles(s,screen,stats,sb,sanit,coros,bubbles):
    #get rid of bullets diappeared
    for bubble in bubbles.copy():
        if bubble.rect.bottom <= 0:
            bubbles.remove(bubble)
    check_bubble_coro_collisions(s,screen,stats,sb,sanit,coros,bubbles)
    

def check_bubble_coro_collisions(s,screen,stats,sb,sanit,coros,bubbles):
    #check if any bubble hit the virus
    #if so get rid rid of bubble and virus
    collisions = pygame.sprite.groupcollide(bubbles,coros,True,True)  #the true here will tell the func to delete the collided args or not 
    if collisions:
        for coros in collisions.values():

            stats.score +=s.coro_points*len(coros)
            sb.prep_score()
        check_high_score(stats,sb)

    if len(coros) == 0:
        #Destroy existing bubbles and create new fleet ,start new level
        bubbles.empty()
        s.increase_speed()

        #increase level
        stats.level += 1
        sb.prep_level()
        create_fleet(s,screen,sanit,coros)



def fire(s,screen,sanit,bubbles):
    #fire a bubble if limit not reached
        if len(bubbles) < s.bubbles_allowed:
            new_bubble = Bubble(s,screen,sanit)
            bubbles.add(new_bubble)


def update_coros(s,screen,stats,sb,sanit,coros,bubbles):
    #check if fleet is reached the edge
    check_fleet_edges(s,coros)
    
    #update pos of all coros in the fleet
    coros.update()

    #look for coro-sanitizer collision
    if pygame.sprite.spritecollideany(sanit,coros):
        #print("BOTTLE HIT!")
        sanit_hit(s,screen,stats,sb,sanit,coros,bubbles)
    #look for virus hitting bottom of the screen
    check_coros_bottom(s,screen,stats,sb,sanit,coros,bubbles)

def check_coros_bottom(s,screen,stats,sb,sanit,coros,bubbles):
    #check if any coros reached bottom
    screen_rect = screen.get_rect()
    for coro in coros.sprites():
        if coro.rect.bottom >=screen_rect.bottom:
            #treat same as if ship got hit
            sanit_hit(s,screen,stats,sb,sanit,coros,bubbles)

def sanit_hit(s,screen,stats,sb,sanit,coros,bubbles):
    #respond to ship being hit by coro
    
    if stats.sanits_left > 0:

        #Decrement bottles left
        stats.sanits_left -=1

        #update scoreboard
        sb.prep_sanits()

        #empty list of coros and bubbles
        coros.empty()
        bubbles.empty()

        #create new fleet and center the bottle
        create_fleet(s,screen,sanit,coros)

        #Pause
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)



def check_play_button(s,screen,stats,sb,play_button,sanit,coros,bubbles,mouse_x,mouse_y):
    #start new game when player clicks play
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active :

        #reset game settings
        s.initialize_dynamic_settings()

        #hide mouse cursor
        pygame.mouse.set_visible(False)
        #Reset game statistics
        stats.reset_stats()
        stats.game_active = True

        #Reset the scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_sanits()

        #empty list of coros and bubbles
        coros.empty()
        bubbles.empty()

        #Create a new fleet and centre the bottle
        create_fleet(s,screen,sanit,coros)
        sanit.center_sanit()


def get_number_coros_x(s,coro_width):
    available_space_x = s.screen_width-2*coro_width
    #spacing betn each coro =one coro width
    number_of_coros = int(available_space_x/(2*coro_width))
    return(number_of_coros)

def get_num_of_rows(s,sanit_height,coro_height):
    #find no. of rows of virus that fit in screen
    available_space_y = (s.screen_height-3*coro_height-sanit_height)
    num_of_rows =int( available_space_y/(2*coro_height))                      #since empty spaces betn rows is being considered as to one coro
    return num_of_rows

def create_coro(s,screen,coros,coro_number,row_number):
    #create a coro and place in row
    coro = Coro(s,screen)
    coro_width = coro.rect.width
    coro.x = coro_width + 2*coro_width *coro_number
    coro.rect.x = coro.x
    coro.rect.y = coro.rect.height +2*coro.rect.height*row_number
    coros.add(coro)


def create_fleet(s,screen,sanit,coros):
    #create full fleet of viruses
    #first a virus and finding no. of coros in a row
    coro = Coro(s,screen)
    number_coros_x = get_number_coros_x(s,coro.rect.width)
    num_of_rows = get_num_of_rows(s,sanit.rect.height,coro.rect.height)


    for row_number in range(num_of_rows):
        #creating frst row of coros
        for coro_number in range(number_coros_x):
            create_coro(s,screen,coros,coro_number,row_number)

def check_fleet_edges(s,coros):
    #respond correctly if viruses have reached the edge
    for coro in coros.sprites():
        if coro.check_edges():
            change_fleet_direction(s,coros)
            break

def change_fleet_direction(s,coros):
    #drop entire fleet and change dir
    for coro in coros.sprites():
        coro.rect.y += s.fleet_drop_speed
    s.fleet_direction *=-1

def check_high_score(stats,sb):
    #check to see if theres new score
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

