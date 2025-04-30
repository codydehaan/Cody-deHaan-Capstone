"""Main game loop and logic for the traffic simulation game."""

# Imports
import sys  # Imports sys library for safe exit of the game
import random  # Imports random to create random stoplight intervals
import math  # Imports math used only for visual effects in cars movement
import pygame  # Imports pygame package to create the game

# Initialize Pygame
# Initializes all pygame modules (Fonts, images, graphics, events)
pygame.init()  # pylint: disable=no-member
# Initializes the sound module in Pygame
pygame.mixer.init()  # pylint: disable=no-member

# Set up the game window
# Creates variables that set the game window
width, height = 1000, 600
screen = pygame.display.set_mode((width, height))  # Displays the window
# Sets a caption for the window
pygame.display.set_caption("Red Light, Green Light - Home From Work")
clock = pygame.time.Clock()  # Creates variable allowing use of internal clock
font = pygame.font.SysFont(None, 48)  # Creates variable for users system font

# Load Images
CAR_IMG = pygame.transform.scale(
    pygame.image.load("Images/VECTEEZY_CAR_IMG.png"), (250, 200)
)
RED_LIGHT_IMG = pygame.image.load("Images/RED_LIGHT_IMG.png")
YELLOW_LIGHT_IMG = pygame.image.load("Images/YELLOW_LIGHT_IMG.png")
GREEN_LIGHT_IMG = pygame.image.load("Images/GREEN_LIGHT_IMG.png")
# Car image uses (.transform.scale) to resize (.image.load) of the car

# Load Sound
BG_AUDIO = pygame.mixer.music.load("Audio/Call_to_Adventure.mp3")
pygame.mixer.music.set_volume(0.1)  #Sets the game audio(0.0-1.0)
START_AUDIO = pygame.mixer.Sound("Audio/Zapsplat_Nissan_Start.mp3")
ENGINE_AUDIO = pygame.mixer.Sound("Audio/AudiV8.mp3")
BRAKE_AUDIO = pygame.mixer.Sound("Audio/Brake_Audio.mp3")
CAR_LOCK = pygame.mixer.Sound("Audio/Car_Lock.mp3")

### Game Constant Variables ###
## Car's state ##
CAR_X = 350  # Cars x position
CAR_Y = 350  # Cars y position
CAR_SPEED = 10  # How fast we want the car to "move" in pixels
MOVING = False  # Car stopped before beginning game
CAR_LOCK_PLAYED = False  # Allows car lock audio to play once

## Traffic Light State ##
LIGHT_COLOR = "green"  # Light set to green to begin game
# Creates a variable for the milliseconds since the game started
LAST_SWITCH_TIME = pygame.time.get_ticks()
LIGHT_DURATION = 18000  # Green through the countdown and instructions

## Game State ##
GAME_OVER = False  # Games ending status
WIN = False  # Games win status
GAME_STARTED = False  # Games start status

## Scrolling ##
SCROLL = 0  # Tracks in pixels how far the background has scrolled
MAX_SCROLL = 20000  # Distance in pixels needed to trigger win
PIXELS_PER_MILES = 1000  # Used to convert pixels to miles

## Colors ##
WHITE = (255, 255, 255)  # These color variables were
BLACK = (0, 0, 0)  # Created to organize coloring of items
RED = (200, 0, 0)  # Used in fonts, backgrounds, and fills
GREEN = (0, 200, 0)  # Used to make later code easier to read
GRAY = (100, 100, 100)

# Load background & fill
# Creates variable creating the games road surface
road_surface = pygame.Surface((width, height))
road_surface.fill(GRAY)  # Fills the surface with GRAY

# Stripe will become 0, 40, 80... until stripe reaches width
for stripe in range(
    0,
    width,
    40,
):
    # Draws road stripes on road_surface
    pygame.draw.rect(road_surface, WHITE, (stripe, height // 2, 20, 10))
    # Every 40th x position half(//2) the height
    # Each road stripe is w=20 and h=10

# Game Instructions


def game_instructions():
    """
    Loops through an instructions list, displays a black background,
    and displays the centered text in white.
    """
    instructions = [
        "Press the space-bar to move forward",
        "Release to stop",  # List of instructions
        "Good luck making it home!",
    ]
    for count in instructions:  # Loops through the instructions list
        screen.fill(BLACK)  # Fills screen black
        # Creates a variable for the WHITE countdown text
        text_surface = font.render(count, True, WHITE)
        text_rect = text_surface.get_rect(
            center=(width // 2, height // 2)
        )  # Centers the text
        screen.blit(text_surface, text_rect)  # Adds the text to the screen
        pygame.display.flip()  # Updates the display
        # Delays 3 seconds to allow user to read instructions
        pygame.time.delay(3000)


# Countdown Function


def show_countdown():
    """
    Loops through a countdown list, displays a black background,
    and displays the centered text in white.
    """
    for count in ["3", "2", "1", "GO!"]:  # Loops through countdown list
        screen.fill(BLACK)  # Fills screen black
        # Creates a variable for the WHITE countdown text
        text_surface = font.render(count, True, WHITE)
        text_rect = text_surface.get_rect(
            center=(width // 2, height // 2)
        )  # Centers text
        screen.blit(text_surface, text_rect)  # Adds the text to the screen
        pygame.display.flip()  # Updates the display
        pygame.time.delay(1500)  # Delays 1.5 seconds to simulate countdown


# Reset Game Function


def reset_game():
    """
    Resets globally defined variables to reset the game.
    This function is called when the game ends and restarts the game.
    """
    global LIGHT_COLOR, LAST_SWITCH_TIME, LIGHT_DURATION
    global MOVING, GAME_OVER, SCROLL, WIN, GAME_STARTED

    LIGHT_COLOR = "green"  # Reset traffic light color to green
    # Reset the time of the last traffic light switch
    LAST_SWITCH_TIME = pygame.time.get_ticks()
    LIGHT_DURATION = 18000  # Reset the traffic light duration
    MOVING = False  # Reset the car's movement state
    GAME_OVER = False  # Reset the game over state
    SCROLL = 0  # Reset the scroll state
    WIN = False  # Reset the win state
    GAME_STARTED = False  # Reset the game started state


# Main Game Loop
# Keeps the game in a constant loop until the user quits (running = False)
RUNNING = True
while RUNNING:
    # If not game_started == True: (at this point it is not)
    if not GAME_STARTED:
        pygame.mixer.music.play(-1, 0.0)  # Play the music from the beginning
        START_AUDIO.play()  # Plays engine start-up audio
        game_instructions()  # And the instructions are displayed
        show_countdown()  # So the countdown begins
        GAME_STARTED = True  # And the game_started variable is turned to True
        START_AUDIO.stop()  # Stops engine start-up audio

    # Keeps game running at fps for constant gameplay across devices
    clock.tick(60)

    # Event Handler
    for event in pygame.event.get():  # Process all events in the event queue
        # Checks if users event is QUIT
        if event.type == pygame.QUIT:  # pylint: disable=no-member
            RUNNING = False  # Stops running if so

        if not GAME_OVER:  # If game_over is not currently True
            # If event is user pressing key
            if event.type == pygame.KEYDOWN:  # pylint: disable=no-member
                # Only if it is the space-bar key
                if event.key == pygame.K_SPACE:  # pylint: disable=no-member
                    MOVING = True  # Set moving to True
                    ENGINE_AUDIO.play()  # Plays the engine audio
            # If event is user releasing key
            if event.type == pygame.KEYUP:  # pylint: disable=no-member
                # Only if it is the space-bar key
                if event.key == pygame.K_SPACE:  # pylint: disable=no-member
                    MOVING = False  # Set moving back to False
                    ENGINE_AUDIO.stop()  # Stops the engine audio
                    BRAKE_AUDIO.play()  # Plays brake audio
        else:  # If game_over is True
            # If event is user pressing key
            if event.type == pygame.KEYDOWN:  # pylint: disable=no-member
                # Only if it is the "R" key
                if event.key == pygame.K_r:  # pylint: disable=no-member
                    reset_game()  # Calls function to reset the game

    # Update Light
    current_time = pygame.time.get_ticks()  # Captures the current time
    # If enough time has passed and difference > light duration
    # It's time to switch the light
    if current_time - LAST_SWITCH_TIME > LIGHT_DURATION:
        if LIGHT_COLOR == "green":  # Light is green
            LIGHT_COLOR = "yellow"  # Then changes to yellow
            LIGHT_DURATION = random.randint(200, 1000)  # For a random duration
        elif LIGHT_COLOR == "yellow":  # Light is yellow
            LIGHT_COLOR = "red"  # Then changes to red
            LIGHT_DURATION = random.randint(1000, 5000)  # For a random duration
        elif LIGHT_COLOR == "red":  # Light is red
            LIGHT_COLOR = "green"  # Then changes to green
            LIGHT_DURATION = random.randint(500, 6000)  # For a random duration
        # Next light change happens based on new current time
        LAST_SWITCH_TIME = current_time

    # Update Scroll
    if MOVING and not GAME_OVER:  # If moving is True and game_over is False
        SCROLL -= CAR_SPEED  # Scroll starts at 0 and decreases by car_speed
    if SCROLL <= -MAX_SCROLL and not GAME_OVER:  # If scroll reaches -max_scroll
        GAME_OVER = True  # Game is over
        WIN = True  # User wins

    # Check Violation
    if MOVING and LIGHT_COLOR == "red":  # If moving is True during "red"
        GAME_OVER = True  # Game is over

    # Draw Scrolling Background
    SCROLL_X = SCROLL % width  # Creates a variable that loops 999-0
    # Draws one surface off-screen to the left
    screen.blit(road_surface, (SCROLL_X - width, 0))
    # Draws another surface on-screen
    screen.blit(road_surface, (SCROLL_X, 0))
    # Together these surfaces loop repeatedly using our scroll_x variable
    ## Draw Car
    # Draws the car image at the designated x and y position
    screen.blit(CAR_IMG, (CAR_X, CAR_Y))

    # Car animation
    if MOVING:  # If moving is True
        # This equation helps create a bouncing effect
        # As time increases, car_y will change from 354 to 346
        CAR_Y = 350 + math.sin(pygame.time.get_ticks() / 100) * 4
        # Dividing by 100 allows slowing of the bounce

    # Draw Traffic Light
    # Creates a variable for the position of the stoplight
    light_pos = (width - 120, 50)
    if LIGHT_COLOR == "green":  # If the light_color variable is green
        # Draw the green light image in the light_pos
        screen.blit(GREEN_LIGHT_IMG, light_pos)
    elif LIGHT_COLOR == "yellow":  # Elif the light_color variable is yellow
        # Draw the yellow light image in the light_pos
        screen.blit(YELLOW_LIGHT_IMG, light_pos)
    elif LIGHT_COLOR == "red":  # Elif the light_color variable is red
        # Draw the red light image in the light_pos
        screen.blit(RED_LIGHT_IMG, light_pos)

    # Calculate Miles Left
    # Variable calculating how far is left in pixels,
    # then we convert that to miles, and use max to not go negative
    miles_left = max(0, (MAX_SCROLL + SCROLL) // PIXELS_PER_MILES)
    # Creates f"" to update variable
    miles_text = font.render(f"Miles to home: {miles_left}", True, BLACK)
    # Draws "Miles to home: XX" at x = 20 y = 20
    screen.blit(miles_text, (20, 20))

    # Show Game Over
    if GAME_OVER:  # If game_over is True
        pygame.mixer.music.stop()  # Stop the background music
        ENGINE_AUDIO.stop()  # Stops car audio
        if not WIN:  # If win is False
            text = font.render("You moved on RED!", True, RED)  # Losing text
            # Draws the text on the screen
            screen.blit(text, (width // 2 - 160, height // 2 - 150))
        else:  # If win is True
            text = font.render(
                "Welcome home! Enjoy your evening!", True, GREEN
            )  # Winning text
            # Draws the text on the screen
            screen.blit(text, (width // 2 - 300, height // 2 - 150))
        restart_text = font.render("Press 'R' to restart", True, BLACK)  # Restart text

        # Draws text on screen in both cases
        screen.blit(restart_text, (width // 2 - 150, height // 2 - 100))

    # Updates the entire screen to display all changes made to the surface
    pygame.display.flip()

# Shuts down pygame modules
pygame.quit()  # pylint: disable=no-member


# Exits the python script
sys.exit()  # pylint: disable=no-member
