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
import pygame, sys, copy
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
DIR_FONT = pygame.font.SysFont('Arial', 12)
BACKGROUNDCOLOR = CHARCOAL
NUMBOXCOLOR = CHARCOAL
TEXTCOLOR = WHITE
BOXBORDER = PAPAYA
BUTTONCOLOR = SPACE

# DECLARE GUI CONSTRAINT CONSTANTS
WIN_WIDTH = 1024
WIN_HEIGHT = 768
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
    global GAME_CLOCK, RENDER_WINDOW, GAME_PUZZLE, BOARD, MOVE_COUNT_BOX, MOVE_COUNT, PUZZLE_COPY, RESET_BTN, CHECK_BTN, NEW_BTN, K_VAL, SOLVED, RESULT
    
    GAME_CLOCK =  pygame.time.Clock() # clock will assist with screen updates

    RENDER_WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # set render window function 

    GAME_PUZZLE = generate_new_puzzle()  # generate new puzzle for the game

    PUZZLE_COPY = copy.deepcopy(GAME_PUZZLE)    # make a copy of the puzzle for resetting

    K_VAL = '' # set k value text to nothing

    SOLVED = '' # set solved text to nothing

    MOVE_COUNT = '0' # initialize move count

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
                        MOVE_COUNT = str(int(MOVE_COUNT) + 1)
                        draw_puzzle() # render update
                
                # RESET BUTTON CLICKED
                if RESET_BTN.collidepoint(position):

                    # Reset Puzzle
                    GAME_PUZZLE = copy.deepcopy(PUZZLE_COPY)

                    # Reset Game Values
                    MOVE_COUNT = '0'
                    SOLVED = ''
                    K_VAL = ''

                    # Render Update 
                    draw_puzzle() 

                # NEW GAME BUTTON CLICKED
                if NEW_BTN.collidepoint(position):

                    # Generate NEW
                    GAME_PUZZLE = generate_new_puzzle()

                    # make a copy of the puzzle for resetting
                    PUZZLE_COPY = copy.deepcopy(GAME_PUZZLE)

                    # Reset Game Values
                    MOVE_COUNT = '0'
                    SOLVED = ''
                    K_VAL = ''

                    # Render Update 
                    draw_puzzle()                    
                
                # CHECK BUTTON WAS CLICKED
                if CHECK_BTN.collidepoint(position):
                    
                    result = None # holds the result of the outcome
                    moves = 0

                    # check for a k - value
                    if K_VAL != '':
                        k = int(K_VAL) # transform to integer

                        outcome = vpuz.build_move_tree(GAME_PUZZLE, k) # determine if solvable in k moves
                        
                        if outcome[0] is True:  # Game Was Solved
                            result = 'Solved'  
                            MOVE_COUNT= str(outcome[3].generation) # set number of moves
                            SOLVED = ','.join(vpuz.get_solving_moves(outcome[3])) # join returned list into comma separated string
                        else:
                            SOLVED = 'Unsolvable in ' + K_VAL + ' moves...' # not solvable in k moves
                            
            
            # Key Pressed Event Listener
            if event.type == pygame.KEYDOWN:

                #backspace
                if event.key == pygame.K_BACKSPACE:
                    K_VAL = K_VAL[:-1]  # subtract one character from end
                elif event.key == pygame.K_DELETE:
                    K_VAL = ''  # delete number 
                else:
                    K_VAL += event.unicode # otherwise enter number


        pygame.display.set_caption("Eight Puzzle: By Joseph Polaski")
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

    # Draw Text
    draw_text()  

def draw_buttons():
    """ Draws All Buttons to GUI"""

    # DEFINE BUTTONS
    # ==============    
    # Reset Button
    btn_reset = pygame.Rect(486, 651, 75, 30) # creates a rectangle object
    res_border = pygame.Rect(485, 650, 77, 32) # creates a rectangle object
    reset_txt = BTN_FONT.render('Reset', True, TEXTCOLOR)   # render font 

    global RESET_BTN
    RESET_BTN = btn_reset

    # Check Button
    btn_check = pygame.Rect(401, 651, 75, 30) # creates a rectangle object
    check_border = pygame.Rect(400, 650, 77, 32) # creates a rectangle object
    check_txt = BTN_FONT.render('Check', True, TEXTCOLOR)   # render font   

    global CHECK_BTN
    CHECK_BTN = btn_check

    # New Game Button
    new_game = pygame.Rect(401, 691, 160, 30) # creates a rectangle object
    ng_border = pygame.Rect(400, 690, 162, 32) # creates a rectangle object
    ng_txt = BTN_FONT.render('New Game', True, TEXTCOLOR)   # render font   

    global NEW_BTN
    NEW_BTN = new_game

    # DRAW BUTTONS
    # ============
    # Reset Button
    pygame.draw.rect(RENDER_WINDOW, TEXTCOLOR, res_border)  #draw reset button border
    pygame.draw.rect(RENDER_WINDOW, BUTTONCOLOR, btn_reset)  #draw reset button        
    RENDER_WINDOW.blit(reset_txt, (btn_reset.x + 10, btn_reset.y + 4)) # render text centered on button

    # Check Button
    pygame.draw.rect(RENDER_WINDOW, TEXTCOLOR, check_border)  #draw check button border
    pygame.draw.rect(RENDER_WINDOW, BUTTONCOLOR, btn_check)  #draw check button  
    RENDER_WINDOW.blit(check_txt, (btn_check.x + 8, btn_check.y + 4)) # render text centered on button

    # New Game Button
    pygame.draw.rect(RENDER_WINDOW, TEXTCOLOR, ng_border)  #draw check button border
    pygame.draw.rect(RENDER_WINDOW, BUTTONCOLOR, new_game)  #draw check button  
    RENDER_WINDOW.blit(ng_txt, (new_game.x + 35, new_game.y + 4)) # render text centered on button
    

def draw_title():
    """Draws the game title"""
    # Define Title
    title = pygame.Rect(60, 25, 500, 35) # creates a rectangle object
    title_txt = BTN_FONT.render(TITLE, True, TEXTCOLOR)   # creates font 

    # Draw Title
    pygame.draw.rect(RENDER_WINDOW, BUTTONCOLOR, title)  #draw title rectangle 
    RENDER_WINDOW.blit(title_txt, (title.x + 100, title.y + 5)) # render text centered on button

def draw_puzzle():
    """Draws the game title"""
    # Define Baseboard
    baseboard = pygame.Rect(61, 70, 498, 498) # creates a rectangle object   

    # Draw Baseboard
    pygame.draw.rect(RENDER_WINDOW, TEXTCOLOR, baseboard)

    tiles = GAME_PUZZLE.puzzle  # fetch game puzzle

    gameboard = []  # mimics the puzzle_board.puzzle

    # define first tile position
    start_x = 62   
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
        start_x = 62 # reset for each row
        start_y += 166
    
    # update the global Board
    global BOARD
    BOARD = gameboard

def draw_text():
    """Draws All Text Boxes to screen"""

    # Enter K value
    enter_k = pygame.Rect(75, 575, 500, 30) # creates a rectangle object
    enterk_txt = DIR_FONT.render('Enter K value (integer) below to check if this puzzle is solvable in, at most, K moves.', True, TEXTCOLOR)   # render font 

    # Or Play Message
    play_it = pygame.Rect(75, 595, 500, 20) # creates a rectangle object
    play_txt = DIR_FONT.render('Or Just play it yourself and find out!', True, TEXTCOLOR)   # render font

    # Draw K value text
    pygame.draw.rect(RENDER_WINDOW, BACKGROUNDCOLOR, enter_k)  #draw K value directions  
    RENDER_WINDOW.blit(enterk_txt, (enter_k.x + 7, enter_k.y + 5)) # render text centered on button

    # Play it text
    pygame.draw.rect(RENDER_WINDOW, BACKGROUNDCOLOR, play_it)  #draw K value directions  
    RENDER_WINDOW.blit(play_txt, (play_it.x + 7, play_it.y + 5)) # render text centered on button

    # K value entry box
    border_box = pygame.Rect(330, 650, 52, 32) # creates a rectangle object
    pygame.draw.rect(RENDER_WINDOW, BLACK, border_box)  #draw K value directions

    k_value = pygame.Rect(331, 651, 50, 30) # creates a rectangle object
    k_text = BTN_FONT.render(K_VAL, True, BLACK)   # render font 
    pygame.draw.rect(RENDER_WINDOW, TEXTCOLOR, k_value)  #draw K value directions
    RENDER_WINDOW.blit(k_text, (k_value.x + 10, k_value.y + 3)) # render text centered on button

    # 'K =' text
    k_equals = pygame.Rect(270, 650, 52, 32) # creates a rectangle object
    equals_txt = BTN_FONT.render('K = ', True, TEXTCOLOR)   # render font

    pygame.draw.rect(RENDER_WINDOW, BACKGROUNDCOLOR, k_equals)  #draw K value directions
    RENDER_WINDOW.blit(equals_txt, (k_equals.x + 7, k_equals.y + 5)) # render text centered on button

    # Move Counter
    move_count = pygame.Rect(30, 650, 150, 30) # creates a rectangle object
    move_txt = BTN_FONT.render('Move Counter:', True, TEXTCOLOR)   # render font

    pygame.draw.rect(RENDER_WINDOW, BACKGROUNDCOLOR, move_count)  #draw K value directions
    RENDER_WINDOW.blit(move_txt, (move_count.x + 7, move_count.y + 5)) # render text centered on button

    # Count Number
    count_num = pygame.Rect(190, 650, 50, 30) # creates a rectangle object
    countnum_txt = BTN_FONT.render(MOVE_COUNT, True, TEXTCOLOR)   # render font

    pygame.draw.rect(RENDER_WINDOW, BACKGROUNDCOLOR, count_num)  #draw K value directions
    RENDER_WINDOW.blit(countnum_txt, (count_num.x + 7, count_num.y + 5)) # render text centered on button

    # Solved Status
    solved_status = pygame.Rect(30, 700, 300, 30) # creates a rectangle object
    solved_txt = BTN_FONT.render(SOLVED, True, TEXTCOLOR)   # render font

    pygame.draw.rect(RENDER_WINDOW, BACKGROUNDCOLOR, solved_status)  #draw K value directions
    RENDER_WINDOW.blit(solved_txt, (solved_status.x + 7, solved_status.y + 5)) # render text centered on button

    global RESULT
    RESULT = solved_status


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
    new_puzzle = pb() 

    # only generate solvable puzzles
    while not new_puzzle.is_solvable():
        new_puzzle = pb()

    return new_puzzle


if __name__=="__main__":
    """Execute Module as Script"""
    game_main() # Run Game