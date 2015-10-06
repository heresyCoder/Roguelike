# import pygame, sys
from core import Funcs
from core import Globals
# from pygame.locals import *

def get_color(name):
    colors = {
        'bg': (5, 26, 56),
        'player': (126, 167, 137),
        'npc': (175, 131, 159),
        'dark_wall': (76, 102, 140),
        'dark_ground': (45, 72, 111)
    }

    return colors[name]

def render_text(text, color):
    rend_text = Globals.FONT.render(text, True, color)
    return rend_text

bg_color = (0, 0, 0)
textures = {}
textures['player'] = render_text('@', get_color('player'))
textures['npc']    = render_text('@', get_color('npc'))
textures['wall']   = render_text('#', get_color('dark_wall'))
textures['ground'] = render_text('.', get_color('dark_ground'))

def draw_Tile(Tile, game, x, y):

    cords = Funcs.ind2cord(x, y)
    game.screen.blit(textures[Tile.type], cords)

def draw_all(self):
    if self.link == 'main_menu':
        for obj in self.draw_queue:
            obj.draw(self)

    elif self.link == 'game':
        # print(len(self.draw_queue))
        if self.draw_queue:
            for i in range(Globals.RENDER_NUM_X):
                for j in range(Globals.RENDER_NUM_Y):
                    if self.draw_queue[i * Globals.RENDER_NUM_Y + j].on_view:
                        self.draw_queue[i * Globals.RENDER_NUM_Y + j].draw(self, i, j)

    self.draw_queue.clear()