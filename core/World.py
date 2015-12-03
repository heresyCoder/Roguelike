import random
import pickle
from core import World_gen
from core.Structures import *
from pygame.locals import *

class World(object):
    def __init__(self, map_width, map_height):

        self.textures = {}
        self.map = World_gen.Map2(map_width, map_height)
        self.map.make_map(Tile)
        self.render_x = 0
        self.render_y = 0

        self.player = Object('player', self.map.map, self.find_free())
        self.npc = Object('npc', self.map.map, self.find_free())

        self.objects = [self.player, self.npc]

    # Returns true if the tile is free.
    def is_free(self, x, y):
        return not self.map.map[x][y].blocked

    # Finds random free place.
    def find_free(self):
        while(True):
            rand_x = random.randint(0, self.map.width - 1)
            rand_y = random.randint(0, self.map.height - 1)

            if self.is_free(rand_x, rand_y):
                return (rand_x, rand_y)

def save_world(world):
    with open('./saves/1.pickle', 'wb') as f:
        pickle.dump(world, f)

def load_world():
    with open('./saves/1.pickle', 'rb') as f:
        return pickle.load(f)

