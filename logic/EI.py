from core.Structures import Object, Tile
from logic import Funcs
import random

def rand_move(npc, world):
    x = npc.x
    y = npc.y

    for i in range(5):
        direct = random.randint(1, 8)

        if direct == 0:
            return

        elif direct == 1:
            if Funcs.is_free(world, x - 1, y - 1):
                x -= 1
                y -= 1

        elif direct == 2:
            if Funcs.is_free(world, x, y - 1):
                y -= 1

        elif direct == 3:
            if Funcs.is_free(world, x + 1, y - 1):
                x += 1
                y -= 1

        elif direct == 4:
            if Funcs.is_free(world, x + 1, y):
                x += 1

        elif direct == 5:
            if Funcs.is_free(world, x + 1, y + 1):
                x += 1
                y += 1

        elif direct == 6:
            if Funcs.is_free(world, x, y + 1):
                y += 1

        elif direct == 7:
            if Funcs.is_free(world, x - 1, y + 1):
                x -= 1
                y += 1

        elif direct == 8:
            if Funcs.is_free(world, x - 1, y):
                x -= 1

        if npc.x != x or npc.y != y:
             break

    world.map.map[npc.x][npc.y] = npc.stand_on
    npc.stand_on = world.map.map[x][y]
    world.map.map[x][y] = npc
    npc.x = x
    npc.y = y