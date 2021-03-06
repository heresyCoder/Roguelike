from core import Globals
import pygame
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

def sum_tuples(tuple1, tuple2):
    t1 = list(tuple1)
    t2 = list(tuple2)

    for i in range(len(t1)):
        t2[i] += t1[i]
    return tuple(t2)

def event_handler(events):

    for event in events:
        if event.type == pygame.KEYDOWN:
            if   event.key == K_w or event.key == K_SPACE:

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

            elif event.key == K_ESCAPE:

                return Globals.K_QUIT, None

        elif event.type == VIDEORESIZE:

            return Globals.E_RESIZE, event.dict['size']

    return Globals.K_NONE, None


