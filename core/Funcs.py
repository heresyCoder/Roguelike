from core import Globals
import pygame
import sys
from pygame.locals import *

def ind2cord(ix, iy):                       # Converts indexes of cells to real screen coordinates

    cx = ix * Globals.FONT_X * 2
    cy = iy * Globals.FONT_Y
    return cx, cy

# def cord2ind(cx, cy):
#
#     ix = cx // (Globals.FONT_X * 2)
#     iy = cy // Globals.FONT_Y
#     return ix, iy

def event_handler(events):

    for event in events:
        if event.type == pygame.KEYDOWN:                # Changed. Pretty the same, but simpler
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit(0)

            elif   event.key == K_w or event.key == K_SPACE:

                return Globals.K_MENU | Globals.K_NAVIGATE, event.key

            elif   event.key == K_s:

                return Globals.K_MENU, event.key

            elif   event.key == K_e \
                or event.key == K_d \
                or event.key == K_c \
                or event.key == K_x \
                or event.key == K_z \
                or event.key == K_a \
                or event.key == K_q:

                return Globals.K_NAVIGATE, event.key

    return Globals.K_NONE, None

