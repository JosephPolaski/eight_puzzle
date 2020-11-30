"""
Eight Puzzle Game


Reference Cited
Title: Chapter 4 - Slide Puzzle
Authors: Al Sweigart
License: Creative Commons BY-NC-SA 3.0 US
URL: https://inventwithpython.com/pygame/chapter4.html

Note: I used this reference as a general guide for setting up and rendering the window of a sliding puzzle game using pygame.
However, I developed my own code and methods for how my front-end renders and interacts with the puzzle generation
and verification that I created.
"""
from puzzle_board import puzzle_board as pb 
import verify_puzzle as vpuz
import pygame, sys
from pygame.locals import *


pygame.init()   # Initialize all imported pygame modules

"""
GLOBAL CONFIGURATION CONSTANTS
==============================
"""
# DECLARE GLOBAL RGB COLORS
CHARCOAL = (47, 62, 78)
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
TILE_FONT = pygame.font.SysFont('Arial Bold', (FONTSIZE * 10))
BACKGROUNDCOLOR = CHARCOAL
NUMBOXCOLOR = CHARCOAL
TEXTCOLOR = WHITE
BOXBORDER = PAPAYA
BUTTONCOLOR = SPACE

# DECLARE GUI CONSTRAINT CONSTANTS
WIN_WIDTH = 720
WIN_HEIGHT = WIN_WIDTH
TITLE = 'WELCOME TO EIGHT PUZZLE!!!'

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
    global GAME_CLOCK, RENDER_WINDOW, GAME_PUZZLE, BOARD
    
    GAME_CLOCK =  pygame.time.Clock() # clock will assist with screen updates

    RENDER_WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # set render window function 

    GAME_PUZZLE = generate_new_puzzle()  # generate new puzzle for the game

    run_game = True  # establish case for game loop

    # MAIN GAME LOOP
    while run_game:

        # Draw Game Screen and GUI
        # ============
        draw_game()        

        # Main Event Handler Loop
        # =======================
        for event in pygame.event.get(): # check for user interaction

            # check if user is exiting game
            if event.type == pygame.QUIT:
                pygame.quit()  # deactivate Pygame Libraries (undoes init())
                sys.exit()  # terminate program

            # Mouse click even listener
            if event.type == MOUSEBUTTONDOWN:

                position = pygame.mouse.get_pos()  # mouse position
                tile_index = tile_clicked(position) # gets tile index if clicked
                
                # NUMBER TILE CLICKED
                if tile_index:
                    
                    # get blank position
                    blank_position = GAME_PUZZLE.get_blank_pos() 

                    # if the tile clicked was not the blank tile
                    if tile_index != blank_position:
                        move_direction = get_move_type(tile_index, blank_position) # determine move direction

                        GAME_PUZZLE.make_move(move_direction) # make move
                        draw_puzzle() # render update
        
        pygame.display.flip()
        GAME_CLOCK.tick(30) # limit to 30 Frames per second

def draw_game():
    """
    This will draw the objects to the window
    including messages to user
    """
    # Fill window with background color
    RENDER_WINDOW.fill(BACKGROUNDCOLOR)

    # Draw Game Title
    draw_title()

    # Draw Puzzle
    draw_puzzle()
    
    # Draw buttons to GUI  
    draw_buttons()  

def draw_buttons():
    """ Draws All Buttons to GUI"""

    # DEFINE BUTTONS
    # ==============    
    # Reset Button
    btn_reset = pygame.Rect(630, 625, 75, 30) # creates a rectangle object
    reset_txt = BTN_FONT.render('Reset', True, TEXTCOLOR)   # render font 

    # Check Button
    btn_check = pygame.Rect(630, 665, 75, 30) # creates a rectangle object
    check_txt = BTN_FONT.render('Check', True, TEXTCOLOR)   # render font   

    # DRAW BUTTONS
    # ============
    # Reset Button
    pygame.draw.rect(RENDER_WINDOW, BUTTONCOLOR, btn_reset)  #draw reset button  
    RENDER_WINDOW.blit(reset_txt, (btn_reset.x + 7, btn_reset.y + 5)) # render text centered on button

    # Check Button
    pygame.draw.rect(RENDER_WINDOW, BUTTONCOLOR, btn_check)  #draw check button  
    RENDER_WINDOW.blit(check_txt, (btn_check.x + 7, btn_check.y + 5)) # render text centered on button

def draw_title():
    """Draws the game title"""
    # Define Title
    title = pygame.Rect(110, 25, 500, 35) # creates a rectangle object
    title_txt = BTN_FONT.render(TITLE, True, TEXTCOLOR)   # creates font 

    # Draw Title
    pygame.draw.rect(RENDER_WINDOW, BUTTONCOLOR, title)  #draw title rectangle 
    RENDER_WINDOW.blit(title_txt, (title.x + 100, title.y + 5)) # render text centered on button

def draw_puzzle():
    """Draws the game title"""
    # Define Baseboard
    baseboard = pygame.Rect(111, 70, 498, 498) # creates a rectangle object   

    # Draw Baseboard
    pygame.draw.rect(RENDER_WINDOW, TEXTCOLOR, baseboard)

    tiles = GAME_PUZZLE.puzzle  # fetch game puzzle

    gameboard = []  # mimics the puzzle_board.puzzle

    # define first tile position
    start_x = 112   
    start_y = 71

    # build a tile for each item in the game puzzle
    for i in range(0,len(tiles)):
        row = []
        for j in range(0, len(tiles[i])):

            if tiles[i][j] is not None: # only draw non - blank tile
                new_tile = pygame.Rect(start_x, start_y, 164, 164) # creates a rectangle object

                tile_txt = TILE_FONT.render(str(tiles[i][j]), True, TEXTCOLOR)   # creates font 

                row.append(new_tile) # add tile to row in 2d list

                pygame.draw.rect(RENDER_WINDOW, BUTTONCOLOR, new_tile)  #draw title rectangle

                RENDER_WINDOW.blit(tile_txt, (new_tile.x + 40, new_tile.y + 20)) # render text centered on Tile
            else:
                new_tile = pygame.Rect(start_x, start_y, 164, 164) # creates a WHITE rectangle object
                row.append(new_tile)
                pygame.draw.rect(RENDER_WINDOW, TEXTCOLOR, new_tile)  #draw title rectangle
            
          
            start_x += 166

        gameboard.append(row)
        start_x = 112 # reset for each row
        start_y += 166
    
    # update the global Board
    global BOARD
    BOARD = gameboard

def tile_clicked(position):
    """
    Checks if number tile was clicked

    :return [i, j]: index position of clicked tile
    :return False: if no number tile was clicked
    """

    # retrieve tile index
    for i in range(0, len(BOARD)):
        for j in range(0, len(BOARD[i])):
            if BOARD[i][j].collidepoint(position):
                return [i, j]
    
    return False

def get_move_type(clicked_tile_position, blank_position):
    """
    Determines what type of move is being attempted

    :param clicked_tile_position: self explanitory
    :return move_type: UP, DOWN, LEFT or RIGHT
    """
    move_type = None # will hold move type

    clicked_row = clicked_tile_position[0] # get clicked row number
    clicked_col = clicked_tile_position[1] # get clicked column number

    blank_row = blank_position[0] # get blank row number
    blank_col = blank_position[1] # get blank column number

    # check UP or DOWN
    if clicked_row > blank_row and clicked_col == blank_col: # DOWN move
        move_type = 'down'
    elif clicked_row < blank_row and clicked_col == blank_col: # UP move
        move_type = 'up'
    
    # check LEFT or RIGHT
    if clicked_col > blank_col and clicked_row == blank_row: # RIGHT move
        move_type = 'right'
    elif clicked_col < blank_col and clicked_row == blank_row: # LEFT move
        move_type = 'left'
    
    return move_type

def generate_new_puzzle():
    """Generates a new game puzzle"""
    return pb() # new puzzle


if __name__=="__main__":
    """Execute Module as Script"""
    game_main() # Run Game