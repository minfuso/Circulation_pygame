# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 16:20:40 2023

@author: snayk
"""

# import the pygame module, so you can use it

import pygame
import os

# Start to create the main window; main surface called WIN
# Defining the constant geometric parameters of the window
WIDTH = 537
HEIGHT = 260

# Declaring the window WIN
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Setting na,e for the window
pygame.display.set_caption("The caption")

# Setting RGB colors
WHITE = (255, 255, 255)

# Setting FPS
FPS = 60

# Background location
BACKGROUND_PICTURE = os.path.join("pictures", "crossroad.png")

# Red car location
RED_CAR = os.path.join("pictures", "red_car.png")


# Background
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

# Car
class Car(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (34.5, 17))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def draw_window(red_car):
    # Fill background with a specific color (RGB format)
    WIN.fill(WHITE)
    # Put a background picture
    background = Background(BACKGROUND_PICTURE, [0, 0])
    WIN.blit(background.image, background.rect)
    # Draw the car
    WIN.blit(red_car.image, red_car.rect)
    # Do not forget to update things to make them appear
    pygame.display.update()


def main():
    # Initialize pygame
    pygame.init()  # initialize pygame
    # Defining the clock
    clock = pygame.time.Clock()
    # parameter / says that the display is running
    run = True
    # Put a car
    red_car = Car(RED_CAR, [1, 154])

    while run:
        # Setting the FPS inside the loop
        clock.tick(FPS)

        # Initial draw
        draw_window(red_car)

        # Check for different events in pygame
        # Looping over a list of different events qnd looping through them
        for event in pygame.event.get():

            # Stopping the loop if user quits the program
            if event.type == pygame.QUIT:
                run = False

        red_car.rect.x += 1

    # Quit pygame window
    pygame.quit()

    # Making sure to run the script only if ran as name


if __name__ == "__main__":
    main()
