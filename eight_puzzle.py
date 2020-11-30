"""
Eight Puzzle Game


Reference Cited
Title: Chapter 4 - Slide Puzzle
Authors: Al Sweigart
License: Creative Commons BY-NC-SA 3.0 US
URL: https://inventwithpython.com/pygame/chapter4.html

Note: I referenced his method for rendering the front-end portion of a sliding puzzle game using pygame and 
handle events.This was extremely helpful since I never worked with pygame before.
"""

import pygame, sys, random
from pygame.locals import *

pygame.init()   # Initialize all imported pygame modules

"""
GLOBAL CONFIGURATION CONSTANTS
==============================
"""
# DECLARE GLOBAL RGB COLORS
METALBLUE = (50, 88, 134)
STEELBLUE = (68, 122, 185)
VISTABLUE = (130, 167, 214)
MEDCHAMP = (252, 232, 164)
PAPAYA = (254, 238, 212)
WHITE = ( 255, 255, 255)
BLACK = ( 0, 0, 0)
SPACE = (64, 71, 79)

# CREATE CONSTANT REFERENCES TO COLORS AND SET DEFAULT FONT SIZE
FONTSIZE = 20
BTN_FONT = pygame.font.SysFont('Arial', FONTSIZE)
BACKGROUNDCOLOR = SPACE
NUMBOXCOLOR = METALBLUE
TEXTCOLOR = PAPAYA
BOXBORDER = PAPAYA
BUTTONCOLOR = METALBLUE

# DECLARE GUI CONSTRAINT CONSTANTS
WIN_WIDTH = 720
WIN_HEIGHT = WIN_WIDTH
ROWS = 3
COLUMNS = 3
TITLE = 'WELCOME TO EIGHT PUZZLE!!!\nby: Joe Polaski'
BOX_SIZE = 100
EMPTY_BOX = None

# DECLARE MARGIN WIDTH TO CENTER GAME ON BACKGROUND
MARGIN_AROUND = int((WIN_WIDTH - (BOX_SIZE * COLUMNS + (COLUMNS - 1))) / 2)

# DECLARE CONSTANT REFERENCE 
# TO DIRECTION STRINGS
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


"""
GAME OPERATIONAL FUNCTIONS
==============================
"""
def game_main():
    """
    This function will serve as the main game function
    it contains the main game loop and coordinates the 
    front and back end.
    """
    # global variables that will be used in other functions
    global GAME_CLOCK, RENDER_WINDOW
    
    GAME_CLOCK =  pygame.time.Clock() # clock will assist with screen updates

    RENDER_WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # set render window function  

    run_game = True  # establish case for game loop

    # MAIN GAME LOOP
    while run_game:

        # Draw Objects
        # ============
        draw_game(RENDER_WINDOW,'')
        

        # Main Event Handler Loop
        # =======================
        for event in pygame.event.get(): # check for user interaction

            # check if user is exiting game
            if event.type == pygame.QUIT:
                pygame.quit()  # deactivate Pygame Libraries (undoes init())
                sys.exit()  # terminate program
        
        pygame.display.flip()
        GAME_CLOCK.tick(30) # limit to 30 Frames per second

def draw_game(window, text):
    """
    This will draw the objects to the window
    including messages to user
    """

    RENDER_WINDOW.fill(BACKGROUNDCOLOR)  # fill window with background color 

    draw_buttons() # draw buttons to GUI   

def draw_buttons():
    """ Draws All Buttons to GUI"""

    # Define Buttons
    btn_reset = pygame.Rect(575, 575, 125, 30) # creates a rectangle object
    reset_txt = BTN_FONT.render('Reset', True, TEXTCOLOR)   # creates font

    #BTN_NEW = pygame.Rect(575, 575, 125, 30) # creates a rectangle object
    #BTN_SOLVABLE = pygame.Rect(575, 575, 125, 30) # creates a rectangle object

    # Draw buttons
    pygame.draw.rect(RENDER_WINDOW, METALBLUE, btn_reset)  #draw reset button  
    RENDER_WINDOW.blit(reset_txt, (btn_reset.x + 35, btn_reset.y + 5)) # render text centered on button



if __name__=="__main__":
    """Execute Module as Script"""
    game_main() # Run Game