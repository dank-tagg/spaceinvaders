import pygame
import random

from pygame import mixer

#Set up window
pygame.init()
width, height = 750, 750
window = pygame.display.set_mode((width, height))
background = pygame.transform.scale(pygame.image.load('./assets/background.png'), (width, height))
pygame.display.set_caption('Space Invaders')

mixer.music.load('./assets/sounds/background.wav')
mixer.music.play(-1)
pygame.font.init()







