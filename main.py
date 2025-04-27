# Imports
import pygame # Imports pygame package to create the game
import sys # Imports sys library for safe exit of the game
import random # Imports random to create random stoplight intervals
import math # Imports math used only for visual effects in cars movement

# Initialize Pygame
pygame.init() # Initializes all pygame modules (Fonts, images, graphics, events)

# Set up the window
width, height = 1000, 600 # Creates variables that set game window W and H (pixels)
screen = pygame.display.set_mode((width, height)) # Displays the window
pygame.display.set_caption("Red Light, Green Light - Home From Work") # Sets a caption for the window
clock = pygame.time.Clock() # Creates variable allowing use of internal clock
font = pygame.font.SysFont(None, 48) # Creates variable for users system font

# Load Images
CAR_IMG = pygame.transform.scale(pygame.image.load("images/VECTEEZY_CAR_IMG.png"), (250, 200))
RED_LIGHT_IMG = pygame.image.load("images/RED_LIGHT_IMG.png")
YELLOW_LIGHT_IMG = pygame.image.load("images/YELLOW_LIGHT_IMG.png")
GREEN_LIGHT_IMG = pygame.image.load("images/GREEN_LIGHT_IMG.png")
# Car image uses (.transform.scale) to resize (.image.load) of the car by W and H

### Game Constant Variables ###
## Car's state ##
car_x = 350 # Cars x position
car_y = 350 # Cars y position
car_speed = 10 # How fast we want the car to "move" in pixels
moving = False # Car stopped before beginning game

## Traffic Light State ##
light_color = "green" # Light set to green to begin game
last_switch_time = pygame.time.get_ticks() # Creates a variable for the milliseconds since the game started
light_duration = 18000 # Light is green through the countdown and instructions

## Game State ##
game_over = False # Games ending status
scroll = 0 # Tracks in pixels how far the background has scrolled
win = False # Games win status
game_started = False # Games start status

## Scrolling ##
max_scroll = 20000 # Distance in pixels needed to trigger win
pixels_per_mile = 1000 # Used to convert pixels to miles

## Colors ##
WHITE = (255, 255, 255)
BLACK = (0, 0, 0) # These color variables were created to organize coloring of items
RED = (200, 0, 0) # Used in fonts, backgrounds, and fills
GREEN = (0, 200, 0) # Used to make later code easier to read
GRAY = (100, 100, 100)

# Load background road fill
road_surface = pygame.Surface((width, height)) # Creates variable creating the games road surface
road_surface.fill(GRAY) # Fills the surface with GRAY

for stripe in range(0, width, 40): # Stripe will become 0, 40, 80, 120... until stripe reaches width (1000)
    pygame.draw.rect(road_surface, WHITE, (stripe, height // 2, 20, 10)) # Draws road stripes on road_surface
                                                                         # Every 40th x position half(//2) the height
                                                                         # Each road stripe is w=20 and h=10
# Game Instructions
def game_instructions():
    """Loops through an instructions list, displays a black background, and displays the centered text in white."""
    instructions = ["Press the space-bar to move forward",
                    "Release to stop",                             # List of instructions
                    "Good luck making it home!"]
    for count in instructions: # Loops through the instructions list
        screen.fill(BLACK) # Fills screen black
        text_surface = font.render(count,True, WHITE) # Creates a variable for the WHITE countdown text
        text_rect = text_surface.get_rect(center=(width //2, height //2)) # Centers the text
        screen.blit(text_surface, text_rect) # Adds the text to the screen
        pygame.display.flip() # Updates the display
        pygame.time.delay(3000) # Delays 3 seconds to allow user to read instructions

# Countdown Function
def show_countdown():
    """Loops through a countdown list, displays a black background, and displays the centered text in white."""
    for count in ["3", "2", "1", "GO!"]: # Loops through countdown list
        screen.fill(BLACK) # Fills screen black
        text_surface = font.render(count, True, WHITE) # Creates a variable for the WHITE countdown text
        text_rect = text_surface.get_rect(center=(width // 2, height // 2)) # Centers the text
        screen.blit(text_surface, text_rect) # Adds the text to the screen
        pygame.display.flip() # Updates the display
        pygame.time.delay(1500) # Delays 1.5 seconds to simulate countdown

# Reset Game Function
def reset_game():
    """Resets globally defined variables to reset the game."""
    global light_color, last_switch_time, light_duration, moving, game_over, scroll, win, game_started
    light_color = "green"
    last_switch_time = pygame.time.get_ticks()
    light_duration = 18000
    moving = False
    game_over = False
    scroll = 0
    win = False
    game_started = False

# Main Game Loop
running = True # Keeps the game in a constant loop until the user quits (running = False)
while running:
    if not game_started: # If not game_started == True: (at this point it is not)
        game_instructions()  # And the instructions are displayed
        show_countdown() # So the countdown begins
        game_started = True # And the game_started variable is turned to True

    clock.tick(60) # Keeps game running at fps for constant gameplay across devices

    # Event Handler
    for event in pygame.event.get(): # Process all events in the event queue
        if event.type == pygame.QUIT: # Checks if users event is QUIT
            running = False # Stops running if so

        if not game_over == True: # If game_over is not currently True
            if event.type == pygame.KEYDOWN: # If event is user pressing key
                if event.key == pygame.K_SPACE: # Only if it is the space-bar key
                    moving = True # Set moving to True
            if event.type == pygame.KEYUP: # If event is user releasing key
                if event.key == pygame.K_SPACE: # Only if it is the space-bar key
                    moving = False # Set moving back to False
        else: # If game_over is True
            if event.type == pygame.KEYDOWN: # If event is user pressing key
                if event.key == pygame.K_r: # Only if it is the "R" key
                    reset_game() # Calls function to reset the game

    # Update Light
    current_time = pygame.time.get_ticks() # Captures the current time
    if current_time - last_switch_time > light_duration: # If enough time has passed and difference is greater than
        if light_color == "green": # Light is green       # Light duration, it's time to switch the light
            light_color = "yellow" # Then changes to yellow
            light_duration = random.randint(200, 1000) # For a random duration
        elif light_color == "yellow": # Light is yellow
            light_color = "red" # Then changes to red
            light_duration = random.randint(1000, 8000) # For a random duration
        elif light_color == "red": # Light is red
            light_color = "green" # Then changes to green
            light_duration = random.randint(100, 6000) # For a random duration
        last_switch_time = current_time # Next light change happens based on new current time

    # Update Scroll
    if moving and not game_over: # If moving is True and # game_over is False
        scroll -= car_speed # Scroll starts at 0 and decreases by car_speed (pixels)
    if scroll <= -max_scroll and not game_over: # If scroll ever reaches -max_scroll
        game_over = True # Game is over
        win = True # User wins

    # Check Violation
    if moving and light_color == "red": # If moving is True during "red"
        game_over = True # Game is over

    # Draw Scrolling Background
    scroll_x = scroll % width # Creates a variable that loops 999-0
    screen.blit(road_surface, (scroll_x - width, 0)) # Draws one surface off-screen to the left
    screen.blit(road_surface, (scroll_x, 0)) # Draws another surface on-screen
                                                  # Together these surfaces loop repeatedly using our scroll_x variable
    # Draw Car
    screen.blit(CAR_IMG, (car_x, car_y)) # Draws the car image at the designated x and y position

    # Car animation
    if moving: #if moving is True                                 # This equation helps create a bouncing effect
        car_y = 350 + math.sin(pygame.time.get_ticks() / 100) * 4 # As time increases, car_y will change from 354 to 346
                                                                  # Dividing by 100 allows slowing of the bounce
    # Draw Traffic Light
    light_pos = (width - 120, 50) # Creates a variable for the position of the stoplight
    if light_color == "green": # If the light_color variable is green
        screen.blit(GREEN_LIGHT_IMG, light_pos) # Draw the green light image in the light_pos
    elif light_color == "yellow": # Elif the light_color variable is yellow
        screen.blit(YELLOW_LIGHT_IMG, light_pos) # Draw the yellow light image in the light_pos
    elif light_color == "red": # Elif the light_color variable is red
        screen.blit(RED_LIGHT_IMG, light_pos) # Draw the red light image in the light_pos

    # Calculate Miles Left                                        # Variable calculating how far is left in pixels, then
    miles_left = max(0, (max_scroll + scroll) // pixels_per_mile) # we convert that to miles, and use max to not go neg
    miles_text = font.render(f"Miles to home: {miles_left}", True, BLACK) # Creates f"" to update variable
    screen.blit(miles_text, (20, 20)) # Draws "Miles to home: XX" at x = 20 y = 20

    # Show Game Over
    if game_over: # If game_over is True
        if not win: # If win is False
            text = font.render("You moved on RED!", True, RED) # Losing text variable
            screen.blit(text, (width // 2 - 160, height // 2 - 150)) # Draws the text on the screen
        else: # If win is True
            text = font.render( "Welcome home! Enjoy your evening!", True, GREEN) # Winning text variable
            screen.blit(text, (width // 2 - 300, height // 2 - 150)) # Draws the text on the screen
        restart_text = font.render("Press 'R' to restart", True, BLACK) # Restart text variable

        screen.blit(restart_text, (width // 2 - 150, height // 2 - 100)) # Draws text on screen in both cases

    pygame.display.flip() # # Updates the entire screen to display all changes made to the surface


pygame.quit() #shuts down pygame modules
sys.exit() #exits the python script
