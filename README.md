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

## The first five sections set up the core foundation for "Red Light, Green Light - Home From Work" using Pygame. They import essential libraries, initialize Pygame and its sound system, and configure the game window, fonts, images, and audio assets. Together, they make up the visual and audio environment needed for the gameplay, ensuring the game runs smoothly within a controlled window and frame rate.

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

##

6. Car's state
   ```sh

   ```
