# Red Light, Green Light - Home From Work

A simple Pygame-based, 2D, road scrolling game. User controls a car driving home from work.
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

**The first five sections set up the core foundation for "Red Light, Green Light - Home From Work" using Pygame. They import essential libraries, initialize Pygame and its sound system, and configure the game window, fonts, images, and audio assets. Together, they make up the visual and audio environment needed for the gameplay, ensuring the game runs smoothly within a controlled window and frame rate.**

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
   # Creates variables that set game the window
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

**These next five sections define the game's dynamic elements and visual settings. They set the initial state of the car, including its position, speed, and whether it's moving. The traffic light system is initialized with a default green state and timing logic for when it should change. Game state variables track whether the game has started, ended, or been won, while the scroll system measures the car’s progress across the screen. Finally, predefined color values are established to simplify and organize the use of color throughout the game’s interface and visual elements. Together, these components manage the logic and appearance needed for gameplay to function correctly.**

6. Car's state
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
