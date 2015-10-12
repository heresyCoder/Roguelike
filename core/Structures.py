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


class String(object):

    def __init__(self, name, text, cords, color):

        self.name = name
        self.x, self.y = cords
        self.color = color
        self.text = text

    def draw(self, game):

        game.screen.blit(Globals.FONT.render(self.text, True, self.color), ind2cord(self.x, self.y))

    def make_patch(self, game):
        patch = pygame.Surface((len(self.text) * Globals.FONT_X, Globals.FONT_Y))
        patch.fill(Graphics.bg_color)
        game.screen.blit(patch, ind2cord(self.x, self.y))