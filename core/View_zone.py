import math
from core import Funcs
from core import Globals
from core import World

def view(map, object):

    # Searching for walls in circle. Using lines, made from player, to VIEW_RADIUS.
    # Whole circle divided for num_of_lines. Each line searching for visible blocks.

    num_of_lines = Globals.VIEW_RADIUS * 10

    # Each line divided by line_parts. Points on the line would be checked for block ownership

    line_parts = Globals.VIEW_RADIUS * 10

    di = math.pi * 2 / num_of_lines

    # Local coordinates
    for i in range(num_of_lines):
        angle = di * i
        line_x1 =  math.cos(angle) * Globals.VIEW_RADIUS
        line_y1 = -math.sin(angle) * Globals.VIEW_RADIUS

        line_dx = line_x1 / line_parts
        line_dy = line_y1 / line_parts

        last_cord = (0, 0)
        blocked = False

        for j in range(line_parts):

            point_x = line_dx * j
            point_y = line_dy * j

            point_x = round(point_x)
            point_y = round(point_y)

            point_x += object.x
            point_y += object.y

            indexes = (point_x, point_y)
            if indexes != last_cord:
                last_cord = indexes

                found_obj = map[indexes[0]][indexes[1]]
                found_obj.on_view = True
                if found_obj.blocked and not type(found_obj) is World.Object:
                    blocked = True
                    break

                if type(found_obj) is World.Tile:
                    found_obj.explored = True
            if blocked: break









