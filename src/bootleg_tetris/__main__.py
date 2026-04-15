#!/usr/bin/python3

# Hiding pygame support message
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import pygame

from .game import start_game

if __name__ == '__main__':
    '''Runs the game of Tetris as well as initializing Pygame and the game display'''

    # Starting up PyGame
    pygame.init()
    pygame.font.init()

    # Setting up display (750 x 500px)
    display = pygame.display.set_mode((750, 500))
    pygame.display.set_caption('Tetris')

    # Running the game
    start_game(display)
