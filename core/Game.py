from core import Globals
from core import View_zone
from logic.Funcs import *
from logic import EI
#import World
from pygame.locals import *
from core import Graphics

def load_game(game):

    key = Globals.K_NAVIGATE, None
    game_process(game, key)

def game_process(self, key):

    if not key[0] & Globals.K_NAVIGATE: return 'game', False

    self.screen.fill(Graphics.bg_color)

    move(self.world.player, key[1], self.world)
    player_cord = self.world.player.x, self.world.player.y
    EI.rand_move(self.world.npc, self.world)

    x_beg = player_cord[0] - Globals.RENDER_NUM_X // 2
    y_beg = player_cord[1] - Globals.RENDER_NUM_Y // 2
    print(player_cord)

    if x_beg < 0: x_beg = 0
    elif x_beg + Globals.RENDER_NUM_X > Globals.FIELD_NUM_X: x_beg = Globals.FIELD_NUM_X - Globals.RENDER_NUM_X

    if y_beg < 0: y_beg = 0
    elif y_beg + Globals.RENDER_NUM_Y > Globals.FIELD_NUM_Y: y_beg = Globals.FIELD_NUM_Y - Globals.RENDER_NUM_Y

    View_zone.view(self.world.map.map, self.world.player)

    for x in range(Globals.RENDER_NUM_X):
        for y in range(Globals.RENDER_NUM_Y):
            self.draw_queue.append(self.world.map.map[x + x_beg][y + y_beg])


    return 'game', False

def move(object, key, world):

    obj_cords = []
    obj_cords.append(object.x)
    obj_cords.append(object.y)

    if key == K_q:
        if is_free(world, obj_cords[0] - 1, obj_cords[1] - 1):
            obj_cords[0] -= 1
            obj_cords[1] -= 1
    elif key == K_w:
        if is_free(world, obj_cords[0], obj_cords[1] - 1):
            obj_cords[1] -= 1
    elif key == K_e:
        if is_free(world, obj_cords[0] + 1, obj_cords[1] - 1):
            obj_cords[0] += 1
            obj_cords[1] -= 1
    elif key == K_a:
        if is_free(world, obj_cords[0] - 1, obj_cords[1]):
            obj_cords[0] -= 1
    elif key == K_d:
        if is_free(world, obj_cords[0] + 1, obj_cords[1]):
            obj_cords[0] += 1
    elif key == K_z:
        if is_free(world, obj_cords[0] - 1, obj_cords[1] + 1):
            obj_cords[0] -= 1
            obj_cords[1] += 1
    elif key == K_x:
        if is_free(world, obj_cords[0], obj_cords[1] + 1):
            obj_cords[1] += 1
    elif key == K_c:
        if is_free(world, obj_cords[0] + 1, obj_cords[1] + 1):
            obj_cords[0] += 1
            obj_cords[1] += 1

    world.map.map[object.x][object.y] = object.stand_on
    object.stand_on = world.map.map[obj_cords[0]][obj_cords[1]]
    world.map.map[obj_cords[0]][obj_cords[1]] = object
    object.x = obj_cords[0]
    object.y = obj_cords[1]

