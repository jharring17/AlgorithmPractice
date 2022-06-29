# Import necessary libraries.
from curses import window
import pygame
pygame.init()

# Sets the starting window dimensions for the game.
window = (400, 400)
screen = pygame.display.set_mode(window)
background = pygame.Surface(window)

# Load in the image for the sprite.
image = pygame.image.load("stickman.png").convert_alpha

class Player:

    # Definitions for the variables of the player class.
    def __init__(self, x, y, image, speed):
        self.x = x
        self.y = y
        self.image = image
        self.speed = speed

    # Method to draw the sprite on the screen.
    def draw(self):
        screen.blit(background,(self.x, self.y))

    # Method to move in x or y direction by speed.
    # It is assumed that one of the positional values will be integers.
    def move(self, speedx, speedy):
        self.x += speedx
        self.y += speedy

    # Method to fight between sprites with a random win algorithm.
    def fight(self):
        return

player = Player(0, 0, image, 0)
player.draw()

for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            speedy = -5
            speedx = 0
        elif event.key == pygame.K_DOWN:
            speedy = 5
            speedx = 0
        elif event.key == pygame.K_LEFT:
            speedy = 0
            speedx = -5
        elif event.key == pygame.K_RIGHT:
            speedy = 0
            speedx = -5
    elif event.type == pygame.KEYDOWN:
        speedy = 0
        speedx = 0

pygame.quit()