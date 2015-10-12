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
        'dark_ground': (45, 72, 111),
        'highlight': (70, 70, 70)
    }

    return colors[name]

bg_color = (0, 0, 0)
textures = {}
# textures['player']   = Globals.FONT.render('@', True, get_color('player'))
# textures['npc']      = Globals.FONT.render('@', True, get_color('npc'))
# textures['wall']     = Globals.FONT.render('#', True, get_color('dark_wall'))
# textures['wall_l']   = Globals.FONT.render('#', True, Funcs.sum_tuples(get_color('dark_wall'), get_color('highlight')))
# textures['ground']   = Globals.FONT.render('.', True, get_color('dark_ground'))
# textures['ground_l'] = Globals.FONT.render('.', True, Funcs.sum_tuples(get_color('dark_ground'), get_color('highlight')))

def draw_Tile(Tile, game, x, y):

    cords = Funcs.ind2cord(x, y)
    if Tile.on_view:
        game.screen.blit(textures[Tile.type + '_l'], cords)
    else:
        game.screen.blit(textures[Tile.type], cords)

def draw_all(self):

    if self.link == 'main_menu':
        for obj in self.draw_queue:
            obj.draw(self)

    elif self.link == 'game':
        from core.Structures import Tile
        # print(len(self.draw_queue))
        if self.draw_queue:
            if Globals.FIELD_NUM_X < Globals.RENDER_NUM_X: Globals.RENDER_NUM_X = Globals.FIELD_NUM_X
            if Globals.FIELD_NUM_Y < Globals.RENDER_NUM_Y: Globals.RENDER_NUM_Y = Globals.FIELD_NUM_Y
            for i in range(Globals.RENDER_NUM_X):
                for j in range(Globals.RENDER_NUM_Y):
                    map_obj = self.draw_queue[i * Globals.RENDER_NUM_Y + j]
                    if map_obj.on_view:
                        map_obj.draw(self, i, j)
                        map_obj.on_view = False
                    else:
                        if type(map_obj) is Tile:
                            if map_obj.explored:
                                map_obj.draw(self, i, j)
                        else:
                            if map_obj.stand_on.explored:
                                map_obj.stand_on.draw(self, i, j)

    self.draw_queue.clear()