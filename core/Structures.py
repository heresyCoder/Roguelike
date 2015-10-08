import pygame
from core import Globals
from core.Funcs import ind2cord
from core import Graphics

class Tile(object):
    def __init__(self, type, blocked):      # ,block_sight = None
        self.type = type
        self.blocked  = blocked
        self.explored = False
        self.on_view  = False

    def draw(self, game, x, y):
        Graphics.draw_Tile(self, game, x, y)


class Object(object):
    def __init__(self, type, map, cords):
        self.type = type
        self.stand_on = map[cords[0]][cords[1]]
        map[cords[0]][cords[1]] = self
        self.blocked = True
        self.on_view = False
        self.x = cords[0]
        self.y = cords[1]

    def draw(self, game, x, y):
        game.screen.blit(Graphics.textures[self.type], ind2cord(x, y))



class String(object):           # Never update cords or text if last wasn't drew

    def __init__(self, name):

        self.name = name
        self.x = 0
        self.y = 0
        self.buf_x = 0
        self.buf_y = 0
        self.text = []
        self.buf_text = []
        self.color = (255, 255, 255)
        self.attr_changed = False

    def set_text(self, text):

        self.text = list(text)
        self.attr_changed = True

    def set_cords(self, x, y):

        self.x = x
        self.y = y
        self.attr_changed = True

    def set_color(self, color):

        self.color = color
        self.attr_changed = True

    def get_size(self):

        return len(self.text)

    def draw(self, game):

        if self.attr_changed:
            patch = pygame.Surface((len(self.buf_text) * Globals.FONT_X, Globals.FONT_Y))
            patch.fill(Graphics.bg_color)
            game.screen.blit(patch, ind2cord(self.buf_x, self.buf_y))
            self.buf_text = self.text
            self.buf_x    = self.x
            self.buf_y    = self.y
            self.attr_changed = False

        actual_cord = list(ind2cord(self.x, self.y))
        for char_ in self.text:
            foo = Globals.FONT.render(char_, True, self.color)
            game.screen.blit(foo, actual_cord)
            actual_cord[0] += Globals.FONT_X