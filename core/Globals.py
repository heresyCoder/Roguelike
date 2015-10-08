# import sys
import pygame
import configparser
# from pygame.locals import *

pygame.init()
pygame.display.set_caption('SOMMETHING')
Config = configparser.ConfigParser()
Config.read('./core/config.ini')

# Constants
SCREEN_WIDTH        = int(Config.get('Main', 'SCREEN_WIDTH'))
SCREEN_HEIGHT       = int(Config.get('Main', 'SCREEN_HEIGHT'))
FRAME_RATE          = int(Config.get('Main', 'FRAME_RATE'))

VIEW_RADIUS         = 5

# FONT_X                  # Width of one symbol
# FONT_Y                  # Height of one symbol
# FIELD_NUM_X             # Number of horizontal symbols
# FIELD_NUM_Y             # Number of vertical symbols
# FONT                    # Font object

WAIT_TIME = 1000 // FRAME_RATE
font_path = "./fonts/Droid_Sans_Mono/DroidSansMono.ttf"
FONT = pygame.font.Font(font_path, int(Config.get('Main', 'font_size')))

FONT_X, FONT_Y = FONT.size("B")


RENDER_NUM_X          = SCREEN_WIDTH  // FONT_X // 2
RENDER_NUM_Y          = SCREEN_HEIGHT // FONT_Y
# NUM_CELLS_ON_SCREEN   = RENDER_NUM_X * RENDER_NUM_Y

FIELD_NUM_X = int(Config.get('World', 'FIELD_NUM_X'))
FIELD_NUM_Y = int(Config.get('World', 'FIELD_NUM_Y'))

K_NONE      = 0b1
K_MENU      = 0b10
K_NAVIGATE  = 0b100
E_RESIZE    = 0b1000
