from core import Globals
from core import View_zone
from core.Funcs import sum_tuples
from logic.Funcs import is_free
from logic import EI
from pygame.locals import *
from core import Graphics as Gr

def load_game(game):

    Gr.textures['player']   = Globals.FONT.render('@', True, Gr.get_color('player'))
    Gr.textures['npc']      = Globals.FONT.render('@', True, Gr.get_color('npc'))
    Gr.textures['wall']     = Globals.FONT.render('#', True, Gr.get_color('dark_wall'))
    Gr.textures['wall_l']   = Globals.FONT.render('#', True, sum_tuples(Gr.get_color('dark_wall'), Gr.get_color('highlight')))
    Gr.textures['ground']   = Globals.FONT.render('.', True, Gr.get_color('dark_ground'))
    Gr.textures['ground_l'] = Globals.FONT.render('.', True, sum_tuples(Gr.get_color('dark_ground'), Gr.get_color('highlight')))

    key = Globals.E_RESIZE, None
    game_process(game, key)

def game_process(game, key):

    if not (key[0] & Globals.K_NAVIGATE or key[0] & Globals.E_RESIZE): return 'game', False

    game.screen.fill(Globals.BG_COLOR)

    if not key[0] & Globals.E_RESIZE:
        move(game.world.player, key[1], game.world)
        EI.rand_move(game.world.npc, game.world)

    View_zone.view(game.world.map.map, game.world.player)

    if game.world.map.width  < game.render_map_x: game.render_map_x = game.world.map.width
    if game.world.map.height < game.render_map_y: game.render_map_y = game.world.map.height

    player_cord = game.world.player.x, game.world.player.y
    x_beg = player_cord[0] - game.render_map_x // 2
    y_beg = player_cord[1] - game.render_map_y // 2
    print(player_cord)
    #print('x, y beg:', x_beg, y_beg)

    if x_beg < 0: x_beg = 0
    elif x_beg + game.render_map_x > game.world.map.width: x_beg = game.world.map.width - game.render_map_x

    if y_beg < 0: y_beg = 0
    elif y_beg + game.render_map_y > game.world.map.height: y_beg = game.world.map.height - game.render_map_y


    for x in range(game.render_map_x):
        for y in range(game.render_map_y):
            game.draw_queue.append(game.world.map.map[x + x_beg][y + y_beg])


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

