# Red Light, Green Light - Home From Work

A simple Pygame-based, 2D, road scrolling game. The user controls a car driving home from work.
If the user moves on a red light the game will end. The game focuses on testing the users reflexes until the "Miles to home:" counter reaches 0.

# Key Features

- Instructions & countdown: Displays the centered instructions and gives the user a countdown.

- Traffic Lights: Random durations each time the light changes from green to yellow to red.

- Scrolling Background: The road scrolls in the background. Giving the illusion of movement.

- Car Animation: The car bounces up and down using a simple trigonometry equation. Furthering the illusion of movement.

- Miles to Home: Tracks the distance the car drives in miles based off of pixel movement.

- Game Over Condition: Game triggers a game over message if the car moves during red.

- Restarting Condition: This feature allows the user to restart the game after each loss.

## Requirements

- Python 3.13
- Pygame: To install this dependency use 'pip install pygame' or 'pip3 install pygame'.

## Acknowledgements

**A BIG THANK YOU TO...**

- VECTEEZY: For their car image. (https://www.vecteezy.com/)
- Pixabay: For their stock mp3 audio. (https://pixabay.com/)
- NCLab: For getting me started on my coding journey. (https://nclab.com/)
- Pygame: For providing a fantastic framework for creating 2D games in Python. (https://www.pygame.org/)

# Deep Dive the Code

**The first five sections(1-5) set up the core foundation for "Red Light, Green Light - Home From Work" using Pygame. They import essential libraries, initialize Pygame and its sound system, and configure the game window, fonts, images, and audio assets. Together, they make up the visual and audio environment needed for the gameplay, ensuring the game runs smoothly within a controlled window and frame rate.**

1. Imports

   ```sh
   import sys  # Imports sys library for safe exit of the game
   import random  # Imports random to create random stoplight intervals
   import math  # Imports math used only for visual effects in cars movement
   import pygame  # Imports pygame package to create the game
   ```

2. Initialize Pygame

   ```sh
   # Initializes all pygame modules (Fonts, images, graphics, events)
   pygame.init()  # pylint: disable=no-member
   # Initializes the sound module in Pygame
   pygame.mixer.init()  # pylint: disable=no-member
   ```

3. Set up the game window

   ```sh
   # Creates variables that set the game window
   width, height = 1000, 600
   screen = pygame.display.set_mode((width, height))  # Displays the window
   # Sets a caption for the window
   pygame.display.set_caption("Red Light, Green Light - Home From Work")
   clock = pygame.time.Clock()  # Creates variable allowing use of internal clock
   font = pygame.font.SysFont(None, 48)  # Creates variable for users system font
   ```

4. Load Images

   ```sh
   CAR_IMG = pygame.transform.scale(
   pygame.image.load("Images/VECTEEZY_CAR_IMG.png"), (250, 200)
   )
   RED_LIGHT_IMG = pygame.image.load("Images/RED_LIGHT_IMG.png")
   YELLOW_LIGHT_IMG = pygame.image.load("Images/YELLOW_LIGHT_IMG.png")
   GREEN_LIGHT_IMG = pygame.image.load("Images/GREEN_LIGHT_IMG.png")
   # Car image uses (.transform.scale) to resize (.image.load) of the car
   ```

5. Load Sound

   ```sh
   BG_AUDIO = pygame.mixer.music.load("Audio/Call_to_Adventure.mp3")
   pygame.mixer.music.set_volume(0.1)
   START_AUDIO = pygame.mixer.Sound("Audio/Zapsplat_Nissan_Start.mp3")
   ENGINE_AUDIO = pygame.mixer.Sound("Audio/AudiV8.mp3")
   BRAKE_AUDIO = pygame.mixer.Sound("Audio/Brake_Audio.mp3")
   CAR_LOCK = pygame.mixer.Sound("Audio/Car_Lock.mp3")
   ```

**These next five sections(6-10) define the game's dynamic elements and visual settings. They set the initial state of the car, including its position, speed, and whether it's moving. The traffic light system is initialized with a default green state and timing logic for when it should change. Game state variables track whether the game has started, ended, or been won, while the scroll system measures the car’s progress across the screen. Finally, predefined color values are established to simplify and organize the use of color throughout the game’s interface and visual elements.**

6. Car state

   ```sh
   CAR_X = 350  # Cars x position
   CAR_Y = 350  # Cars y position
   CAR_SPEED = 10  # How fast we want the car to "move" in pixels
   MOVING = False  # Car stopped before beginning game
   CAR_LOCK_PLAYED = False  # Allows car lock audio to play once
   ```

7. Traffic Light State

   ```sh
   LIGHT_COLOR = "green"  # Light set to green to begin game
   # Creates a variable for the milliseconds since the game started
   LAST_SWITCH_TIME = pygame.time.get_ticks()
   LIGHT_DURATION = 18000  # Green through the countdown and instructions
   ```

8. Game State

   ```sh
   GAME_OVER = False  # Games ending status
   WIN = False  # Games win status
   GAME_STARTED = False  # Games start status
   ```

9. Scrolling

   ```sh
   SCROLL = 0  # Tracks in pixels how far the background has scrolled
   MAX_SCROLL = 1000  # Distance in pixels needed to trigger win
   PIXELS_PER_MILES = 1000  # Used to convert pixels to miles
   ```

10. Colors

    ```sh
    WHITE = (255, 255, 255)  # These color variables were
    BLACK = (0, 0, 0)  # Created to organize coloring of items
    RED = (200, 0, 0)  # Used in fonts, backgrounds, and fills
    GREEN = (0, 200, 0)  # Used to make later code easier to read
    GRAY = (100, 100, 100)
    ```

**Section 11 creates the game's background by generating a gray road surface that fills the entire game window. It then adds white road stripes at regular intervals across the center of the screen to simulate lane markers.**

11. Load background & fill

    ```sh
    # Creates variable creating the games road surface
    road_surface = pygame.Surface((width, height))
    road_surface.fill(GRAY) # Fills the surface with GRAY

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
    ```

**Sections 12-14 are dedicated to functions. These three functions support the game's user experience and flow. The game_instructions() function introduces the player to the controls and objective with clear, centered messages shown one at a time. The show_countdown() function builds anticipation and readiness by displaying a timed countdown before gameplay begins. The reset_game() function reinitializes all key game state variables, allowing the player to restart from the beginning after a win or loss. Together, these functions manage game pacing, player guidance, and replayability, ensuring a smooth and engaging experience.**

12. Game Instructions Function

    ```sh
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
    ```

13. Show Countdown Function

    ```sh
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
    ```

14. Reset Game Function

    ```sh
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
    ```

**This part of the main game loop handles the initial setup for the game. When the loop first starts, it checks if the game hasn't started (not GAME_STARTED). If true, it plays the background music on a loop, triggers the car start-up sound, displays game instructions and a countdown, then marks the game as started. After this setup, the loop continues to run, regulated by clock.tick(60), which limits updates to 60 frames per second for smooth and consistent gameplay.**

15. Main Game Loop

    ```sh
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
    ```

**Sections 16-19 make up the core gameplay logic, checking for player input, updating traffic light states, scrolling the background to simulate movement, and enforcing game rules. The event handler listens for space-bar presses to control car motion and checks if the player attempts to move on a red light. The traffic light changes color based on timers and random intervals, creating unpredictable gameplay. As the car moves, the background scrolls to simulate progress. If the car scrolls far enough, the player wins. But if the car moves during a red light, the game ends immediately.**

16. Event Handler

    ```sh
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
    ```

17. Update Light

    ```sh
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
    ```

18. Update Scroll

    ```sh
    if MOVING and not GAME_OVER:  # If moving is True and game_over is False
        SCROLL -= CAR_SPEED  # Scroll starts at 0 and decreases by car_speed
    if SCROLL <= -MAX_SCROLL and not GAME_OVER:  # If scroll reaches -max_scroll
        GAME_OVER = True  # Game is over
        WIN = True  # User wins
    ```

19. Check Violation

    ```sh
    if MOVING and LIGHT_COLOR == "red":  # If moving is True during "red"
        GAME_OVER = True  # Game is over
    ```

**Sections 20-23 manage how the game looks on-screen during play. A repeating background surface is drawn to simulate a road, while the car image stays in place. A bounce animation gives the car a more lively motion effect while it's moving. The current traffic light color is rendered in the corner, and the game displays how many "miles" remain until the player gets home.**

20. Draw Scrolling Background

    ```sh
    SCROLL_X = SCROLL % width  # Creates a variable that loops 999-0
    # Draws one surface off-screen to the left
    screen.blit(road_surface, (SCROLL_X - width, 0))
    # Draws another surface on-screen
    screen.blit(road_surface, (SCROLL_X, 0))
    # Together these surfaces loop repeatedly using our scroll_x variable
    ## Draw Car
    # Draws the car image at the designated x and y position
    screen.blit(CAR_IMG, (CAR_X, CAR_Y))
    ```

21. Car Animation

    ```sh
    if MOVING:  # If moving is True
        # This equation helps create a bouncing effect
        # As time increases, car_y will change from 354 to 346
        CAR_Y = 350 + math.sin(pygame.time.get_ticks() / 100) * 4
        # Dividing by 100 allows slowing of the bounce
    ```

22. Draw Traffic Light

    ```sh
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
    ```

23. Calculate Miles Left

    ```sh
    # Variable calculating how far is left in pixels,
    # then we convert that to miles, and use max to not go negative
    miles_left = max(0, (MAX_SCROLL + SCROLL) // PIXELS_PER_MILES)
    # Creates f"" to update variable
    miles_text = font.render(f"Miles to home: {miles_left}", True, BLACK)
    # Draws "Miles to home: XX" at x = 20 y = 20
    screen.blit(miles_text, (20, 20))
    ```

**In the last two sections(24&25), the final part of the game loop checks whether the game is over and displays a win or loss message accordingly. All audio is then shut off. Players are prompted to press "R" to restart. Once the player quits the game, all Pygame modules are shut down and the script exits cleanly.**

24. Show Game Over

    ```sh
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
    ```

25. Shutdown & Exit

    ```sh
    # Shuts down pygame modules
    pygame.quit()  # pylint: disable=no-member


    # Exits the python script
    sys.exit()  # pylint: disable=no-member
    ```
