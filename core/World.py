import random
import pickle
from core.Structures import *
from pygame.locals import *

# x, y - upper left corner coordinates; w, h - displacement to the lower right
# corner.
# A rectangle on the map. Used to characterize a room.
class Rect(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.ax = x + w
        self.ay = y + h

    # Finds the center of a rectangle.
    def center(self):
        center_x = (self.x + self.ax) // 2
        center_y = (self.y + self.ay) // 2
        return (center_x, center_y)

class Map(object):
    def __init__(self, width, height):
        self.width  = width
        self.height = height
        self.map    = [[]]

    # Creates map with random dungeon.
    def make_map(self):
        self.map = [[ Tile('wall', True)
            for y in range(self.height) ]
                for x in range(self.width) ]

        rooms = []
        num_rooms = 0
        max_rooms = self.height

        for room in range(max_rooms):
            w = random.randint(3, max_rooms // 2)
            h = random.randint(3, max_rooms // 2)

            x = random.randint(0, self.width - w - 1)
            y = random.randint(0, self.height - h - 1)

            new_room = Rect(x, y, w, h)

            overlap = False

            for other_room in rooms:
                if self.intersect(new_room, other_room):
                    overlap = True
                    break

            if not overlap:
                self.create_room(new_room)

            (new_x, new_y) = new_room.center()

            if num_rooms > 0:
                (prev_x, prev_y) = rooms[num_rooms - 1].center()
                if random.randint(0, 1) == 1:
                    self.create_h_tunnel(prev_x, new_x, prev_y)
                    self.create_v_tunnel(prev_y, new_y, new_x)
                else:
                    self.create_v_tunnel(prev_y, new_y, new_x)
                    self.create_h_tunnel(prev_x, new_x, prev_y)

            rooms.append(new_room)
            num_rooms += 1

    # Goes through the tiles in rectangle and makes them passable.
    def create_room(self, room):
        for x in range(room.x + 1, room.ax):
            for y in range(room.y + 1, room.ay):
                self.map[x][y].blocked = False
                self.map[x][y].type = 'ground'

    # Creates horizontal tunnel of passable tiles.
    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.map[x][y].blocked = False
            self.map[x][y].type = 'ground'

    # Creates vertical tunnel of passable tiles.
    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.map[x][y].blocked = False
            self.map[x][y].type = 'ground'

    # Returns True if two rooms overlap.
    def intersect(self, room_a, room_b):
        return (room_a.x <= room_b.ax and room_a.ax >= room_b.x and
                room_a.y <= room_b.ay and room_a.ay >= room_b.y)

class World(object):
    def __init__(self, map_width, map_height):

        self.textures = {}
        self.map = Map(map_width, map_height)
        self.map.make_map()

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

